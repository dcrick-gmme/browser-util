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
#       -   GmmePylib
#
#===============================================================================
# $Log: $
#===============================================================================

#import json
import os
import sys

from lib import CBrowser as CBrowser


l_test = CBrowser.Create('chrome')
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


print("we are")

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
