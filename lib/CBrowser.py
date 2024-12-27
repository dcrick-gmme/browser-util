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

import glob
import jmespath
import json
import os
import platform
import time

from gmmePylib import *


#-------------------------------------------------------------------------------
#-- Module variables
#-------------------------------------------------------------------------------
cbrowser__ = {
    'os':       {
                    'windows':  {'envusername': 'USERNAME'},
                    'linux':    {'envusername': 'USER'},
                },

    'chrome':   {
                    'windows':  {'configPath': "C:\\Users\\{0}\\AppData\\Local\\Google\\Chrome\\User Data"},
                    'linux':    {'configPath': "/home/{0}/.config/google-chrome"},
                },
    'edge':     {
                    'windows':  {'configPath': "C:\\Users\\{0}\\AppData\\Local\\Microsoft\\Edge\\User Data"},
#                            'linux': {'configPath': "/home/{0}/.config/google-chrome"},
                },
}


#-------------------------------------------------------------------------------
#-- Class CmdLine
#-------------------------------------------------------------------------------
class CBrowser():
    #---------------------------------------------------------------------------
    #-- Members
    #---------------------------------------------------------------------------
    m_dbgOn = False
    m_isInit = False

    m_browser = None
    m_user = None


    #---------------------------------------------------------------------------
    #-- ctor
    #---------------------------------------------------------------------------
    def __init__(self, a_browser:str = None, a_user:str = None, a_dbgOn:bool = False):
        self.m_dbgOn = a_dbgOn

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

        self.m_browser = a_browser.lower()
        self.m_user = a_user


        #-----------------------------------------------------------------------
        #-- determine location for browser folder
        l_os = platform.system().lower()
        self.m_user = os.environ.get(cbrowser__['os'][l_os]['envusername'])

        self.m_configpath = cbrowser__[self.m_browser][l_os]['configPath'].format(self.m_user)
        self.m_pathsep = os.path.sep


        #-----------------------------------------------------------------------
        #-- load profiles, which means:
        #-- 1. glob list of profile folders from browser config location
        #-- 2. for each profile load preferences file
        self.m_profiles = {'id': {}, 'name': {}}
        for l_entry in glob.glob(self.m_configpath + self.m_pathsep + "Profile *"):
            #-- load json files
            l_preferences = Utils.Other.OSLoadJson(l_entry + self.m_pathsep + "Preferences")
#            l_bookmarks  = Utils.Other.OSLoadJson(l_entry + self.m_pathsep + "Bookmarks")

#            with open(os.getcwd() + "\\tests\\bookmarks.json", "w") as f:
#                json.dump(l_bookmarks, f, indent=4)

            l_id = os.path.basename(l_entry)
            l_name = jmespath.search("profile.name", l_preferences)

            self.m_profiles['id'][l_id] = {'name': l_name, 'preferences': l_preferences}
            self.m_profiles['name'][l_name] = {'id': l_id, 'preferences': l_preferences}


        print("we are here")


##-- map os specific code into Other namespace
#if platform.system() == "Windows":
#elif platform.system() == "Linux":





    #---------------------------------------------------------------------------
    #-- load_
    #---------------------------------------------------------------------------
#    def loadBrowser_(self):
#        

#-------------------------------------------------------------------------------
#-- Create functions
#-------------------------------------------------------------------------------
def Create(a_browser = None, a_user = None, a_dbgOn = False):
    return CBrowser(a_browser, a_user, a_dbgOn)
