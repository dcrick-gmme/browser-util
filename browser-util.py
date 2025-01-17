#!/usr/bin/env python
#===============================================================================
# browser-util
#===============================================================================
#	Author:	David Crickenberger
# ------------------------------------------------------------------------------
# 	Description:
#		Command line utils to process browser stuff:
#       -   settings
#       -   favorites
#
#   Required packages:
#       -   pywin32
#       -   gmmepylib
#
#===============================================================================

from dataclasses import dataclass
from gmmePylib import *
from lib import CBrowser as CBrowser

import os
import platform
import sys


#print("this is a test")


#-------------------------------------------------------------------------------
#-- program variables
#-------------------------------------------------------------------------------
#g_cmdline = None
#_o_buvars__ = {
#    'action': None,
#    'cmdline': None,
#    'backup': False,
#    'browser': None,
#    'source': None,
#    'user': None,
#}


@dataclass
class _o_buvars__:
    action: str = None,
    cmdline: Utils.CmdLine = None,
    backup: bool =  False,
    browser: str =  None,
    source: str =  None,
    user: str =  None,



#-- cmdline options:
#-- -browser: browser to work with under current user
#-- -user: user to find -browser setting under (default=current user)
#-- -archive, -backup:  archive/backup browser settings files
#-- -source, -src: specifies browser path
#-- -target: path for archive/backup
#-- -profile
#-- -profiles list: list all profiles


#-------------------------------------------------------------------------------
#-- init_: initialize program
#-------------------------------------------------------------------------------
def init_():
    #---------------------------------------------------------------------------
    #-- initialize command line object
    #---------------------------------------------------------------------------
    l_cmdline = Utils.CmdLine.Create()
    l_cmdline.AddArgs(sys.argv[1:])
    _o_buvars__.cmdline = l_cmdline
#    _o_buvars__['cmdline'] = l_cmdline

    #---------------------------------------------------------------------------
    #-- process command line
    #---------------------------------------------------------------------------
    if l_cmdline.IsOpt('archive') or l_cmdline.IsOpt('-backup'):
        _o_buvars__.backup = True
#        _o_buvars__['backup'] = True

    _o_buvars__.browser = l_cmdline.GetOptValue('-browser')
    _o_buvars__.browsers = l_cmdline.IsOpt('-browsers')
    _o_buvars__.profiles = l_cmdline.GetOptValue('-profiles')
#    _o_buvars__['browser'] = l_cmdline.GetOptValue('-browser')
#    _o_buvars__['browsers'] = l_cmdline.IsOpt('-browsers')
#    _o_buvars__['profiles'] = l_cmdline.GetOptValue('-profiles')
                                                                      

#-------------------------------------------------------------------------------
#-- process_: process based on command line options
#-------------------------------------------------------------------------------
def process_(a_user: str = None):
    #-- see if we are listing valid browsers
    if _o_buvars__.browsers:
        l_browsers = CBrowser.CBrowsersSupported(a_user, True)
        print("browsers -- beg:")
        print("   user = " + l_browsers.user)
        print("   os = " + l_browsers.os)
        print("   list -- beg:")
        for l_browser in CBrowser.CBrowsersSupported(a_user).items:
            print("      " + l_browser.name + " ==> " + l_browser.configpath)
        print("   list -- end:")
        print("browsers -- end:")

#    print("we are here")


#-------------------------------------------------------------------------------
#-- main processing
#-------------------------------------------------------------------------------
init_()
process_()
process_("DavidCrickenberger")
print("we are here")



""" 
l_file = os.getcwd() + "\\tests\\bookmarks.json"
l_f = open(l_file, 'r')
l_json = json.load(l_f)

l_1 = "bookmark_bar.[*].name"
l_r = jmespath.search("roots.bookmark_bar.children[?type=='folder'].[name,type,children]", l_json)

print("we are here")
"""

#-- list bookmar_bar items:: "roots.bookmark_bar.children[*].name"
#-- list bookmark_bar items and children:: "roots.bookmark_bar.children[*].[name,type,children]"
#-- list bookmark_bar items and children folders:: "roots.bookmark_bar.children[?type=='folder'].[name,type,children]"
#-- list bookmark_bar items with url and url:: "roots.bookmark_bar.children[?type=='url'].[name,type,url]"


#l_test = CBrowser.Create('chrome')
#l_count = l_test.ProfileCount()
#print("we are here!!")


#from gmmePylib.Utils.Object import Object
#import gmmePylib.Utils.Object
#import gmmePylib.Utils.CmdLine
#from gmmePylib.Utils import *exit
#import gmmePylib.Utils as Utils
#l_cmdline = CmdLine.Create()
#import gmmePylib.Utils as 
from gmmePylib import *
#from gmmePylib.Utils import *

#from gmmePylib.Utils import CmdLine

#o_cmdline = Utils.CmdLine.Create()
#o_cmdline.AddArgs(sys.argv[1:])

#l_file = "C:\\Users\\dcrick\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Preferences"
#l_file = "C:\\Users\\DavidCrickenberger\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 8\\Preferences"
#with open(l_file, 'r', encoding="utf8") as f:
#    data = json.load(f)
#pjson = json.dumps(data, indent=3)
#print(pjson)
#print("we are here!")



#profile name ::  preferences->profile->name
#account info ::  preferences->account_info  [array of hashes ]



#o_cmdline = gmmePylib.Utils.CmdLine.Create()







#import sample
#from sample import simple, simpleclass
#from sample import simpleclass
#import sample.simpleclass
#print("simple.add_one(2) = ", simple.add_one(2))
#print("simple.add_one(4) = ", simple.add_one(4))

#l_class = simpleclass()
#l_class1 = simpleclass.simpleclass()
#l_class2 = simpleclass.simpleclass(5)
#l_class1.AddOne()


#from sample.TestClasses import TestClass1, TestClass2
#import sample.TestClasses as TestClasses
#l_tclass1 = TestClasses.TestClass1()
#l_tclass2 = TestClasses.TestClass2()
#l_tclass1 = sample.TestClasses.TestClass1.TestClass1()
#l_tclass2 = TestClass2.TestClass2()

#l_tclass1 = TestClass1.TestClass1()
#l_tclass2 = TestClass2.TestClass2()

#import sample
#import sample.TestClasses.TestClass1
#import sample.TestClasses.TestClass2
#l_tclass1 = TestClass1.TestClass1()
#l_tclass1 = TestClass1()
#l_tclass2 = TestClass2()


#print("we are")

#import gmmePyLib.BatchApp
#from gmmePyLib import Utils
#from gmmePyLib import BatchApp
#from gmmePyLib import *

#l_batchApp = BatchApp()









#from gmmePyLib.Utils import CmdLine
#import gmmePyLib as gmmelib
#import gmmePyLib.Utils.CmdLine
#print("test")
#from gmmePyLib
#_pylib.Utils.CmdLine

#from sample import simple

#xx = simple.add_one(2)

#print(sample.add_one(2))

#l_cmdLine = CmdLine(True)
#l_cmdline = gmmePyLib.Utils.CmdLine(True)
#l_cmdline.AddArgsArray(sys.argv[1:])

#l_cmdline.Dump()
#quit()

#    if len(sys.argv) == 1 :
#        #-- pass .opt file to process from env or default
#        l_cmdline.AddArgsFile(os.environ.get(s_CmdlineEnvTestOptfile(), "./CmdLineTest/custperf.opt"))
#    else :
#        #-- pass in what is ever on the command line
#        l_cmdline.AddArgsArray(sys.argv[1:])

#l_cmdline.Dump()
#print("we are")
