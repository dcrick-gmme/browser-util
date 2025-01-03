#!/usr/bin/env python
#===============================================================================
# browser-util for Python
# Copyright (c) 2024, GMM Enterprises, LLC.
# Licensed under the GMM Software License
# All rights reserved 
#===============================================================================
# Author: David Crickenberger
# ------------------------------------------------------------------------------
# Packages - required:
#
# Description:
#===============================================================================

from dataclasses import dataclass
from gmmePylib import *

#import glob
import itertools
import jmespath
import json
import os
import pathlib
import platform
import time


#-------------------------------------------------------------------------------
#-- Module variables
#-------------------------------------------------------------------------------
_cbrowser__ = {
    'os':       {
                    'windows':  {'envusername': 'USERNAME'},
                    'linux':    {'envusername': 'USER'},
                },

    'brave':   {
                    'windows':  {'configPath': "C:\\Users\\{0}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data"},
                    'linux':    {'configPath': "/home/{0}/.config/BraveSoftware/Brave-Browser"},
                },

    'chrome':   {
                    'windows':  {'configPath': "C:\\Users\\{0}\\AppData\\Local\\Google\\Chrome\\User Data"},
                    'linux':    {'configPath': "/home/{0}/.config/google-chrome"},
                },
    'edge':     {
                    'windows':  {'configPath': "C:\\Users\\{0}\\AppData\\Local\\Microsoft\\Edge\\User Data"},
#                            'linux': {'configPath': "/home/{0}/.config/google-chrome"},
                },

    'supported':    ['brave','chrome','edge']
}


#C:\Users\dcrick\AppData\Local\Google\Chrome\User Data

#-------------------------------------------------------------------------------
#-- Class CBrowser
#-------------------------------------------------------------------------------
class CBrowser():
    #---------------------------------------------------------------------------
    #-- Members
    #---------------------------------------------------------------------------
    _m_dbgOn: bool = False
    _m_isInit: bool = False

    _m_browser: str = None
    _m_configpath: str = None
    _m_user: str = None


    #---------------------------------------------------------------------------
    #-- ctor
    #---------------------------------------------------------------------------
    def __init__(self, a_browser:str = None, a_user:str = None, a_dbgOn:bool = False):
        self._m_dbgOn = a_dbgOn

        if a_browser != None: self.Load(a_browser, a_user)


    #---------------------------------------------------------------------------
    #-- Load::
    #--
    #-- Desc:
    #--     Scan browser os folder for all 'Profile *' folders, and load the
    #--     Preferences folder in each 'Profile *' folder, and pull the
    #--     profile.name json value
    #---------------------------------------------------------------------------
    def Load(self, a_browser, a_user = None):
#        self.m_isInit = True

        self._m_browser = a_browser.lower()
        self._m_user = a_user


        #-----------------------------------------------------------------------
        #-- determine location for browser folder
        l_os = platform.system().lower()
        self._m_user = os.environ.get(_cbrowser__['os'][l_os]['envusername'])

        self._m_configpath = _cbrowser__[self.m_browser][l_os]['configPath'].format(self.m_user)
        self.m_pathsep = os.path.sep


        #-----------------------------------------------------------------------
        #-- load profiles, which means:
        #-- 1. glob list of profile folders from browser config location
        #--    including Default profile
        #-- 2. for each profile load preferences file
        self.m_profiles = {'id': {}, 'name': {}}

        l_path = pathlib.Path(self.m_configpath)
        l_glob = list(
            itertools.chain.from_iterable(
                l_path.glob(l_pattern) for l_pattern in ["Default", "Profile *"]
            )
        )

        for l_profilePath in l_glob:
            #-- load json preferences file
            print(l_profilePath)
#            l_preferences = Utils.Other.OSLoadJson(entry + self.m_pathsep + "Preferences")


#        for l_entry in glob.glob(self.m_configpath + self.m_pathsep + "Profile *"):
            #-- load json files
#            l_preferences = Utils.Other.OSLoadJson(l_entry + self.m_pathsep + "Preferences")
##            l_bookmarks  = Utils.Other.OSLoadJson(l_entry + self.m_pathsep + "Bookmarks")

##            with open(os.getcwd() + "\\tests\\bookmarks.json", "w") as f:
##                json.dump(l_bookmarks, f, indent=4)

#            l_id = os.path.basename(l_entry)
#            l_name = jmespath.search("profile.name", l_preferences)

#            self.m_profiles['id'][l_id] = {'name': l_name, 'preferences': l_preferences}
#            self.m_profiles['name'][l_name] = {'id': l_id, 'preferences': l_preferences}


        print("we are here")


##-- map os specific code into Other namespace
#if platform.system() == "Windows":
#elif platform.system() == "Linux":





    #---------------------------------------------------------------------------
    #-- load_
    #---------------------------------------------------------------------------
#    def loadBrowser_(self):
#        


    #---------------------------------------------------------------------------
    #-- Access methods
    #---------------------------------------------------------------------------
    def ProfileCount(self): return len(self.m_profiles['id'])
    #def AccountsCount(self): return len(jmespath.search("profile.name", l_preferences))


#-------------------------------------------------------------------------------
#-- Create functions
#-------------------------------------------------------------------------------
def Create(a_browser = None, a_user = None, a_dbgOn = False):
    return CBrowser(a_browser, a_user, a_dbgOn)


#-------------------------------------------------------------------------------
#-- support functions
#-------------------------------------------------------------------------------
def ConfigPath(a_browser:str, a_os:str = platform.system().lower()):    return _cbrowser__[a_browser]['config']


#-------------------------------------------------------------------------------
#-- dataclass:
#--     CBrowsersSupportedItem
#--     CBrowsersSupported
#-------------------------------------------------------------------------------
@dataclass
class CBrowsersSupportedItem:
    name: str = None
    configpath: str = None

    def __init__(self, a_name: str, a_configpath: str):
        self.name = a_name
        self.configpath = a_configpath

@dataclass
class CBrowsersSupported:
    items: list = None
    os: str = platform.system().lower()
    user: str = None

    def __init__(self, a_user: str = None):
        self.items = []
        if a_user != None:
            self.user = a_user
        else:
            self.user = os.environ.get(_cbrowser__['os'][self.os]['envusername'])
        for l_browser in _cbrowser__['supported']:
            self.items.append(CBrowsersSupportedItem(l_browser, _cbrowser__[l_browser][self.os]['configPath'].format(self.user)))






#@dataclass(frozen=True)
#@dataclass
#class CBrowsersSupported:
#    blist: list[int] = []
#    blist: list[CBrowsersSupportedItem] = []
#    user: str = None

#    def __init__(self, a_user: str = None):
#        self.user = a_user


#def Supported(a_user:str = None):
#    return _cbrowser__['supported']
