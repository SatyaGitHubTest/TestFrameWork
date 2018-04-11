# this file is top level executor
 
import os,sys,inspect
# add script directory to python sreachable locations
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import logging
from common.readhosts import *
from common.readtestcases import *
from common.readproperties import *

#change working directory to script location
cwd = os.getcwd()
os.chdir('TestFrameWork/testcases')
cwd = os.getcwd()
print(cwd)

stflogger = logging.getLogger(__name__)
stflogger.setLevel(logging.DEBUG)
loghandle1 = logging.StreamHandler()
#loghandle1.setLevel(logging.WARNING)

loghandle2 = logging.FileHandler('../logs/stflog.log', mode='a')
#loghandle2.setLevel(logging.WARNING)

frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loghandle1.setFormatter(frmt)
loghandle2.setFormatter(frmt)

stflogger.addHandler(loghandle1)
stflogger.addHandler(loghandle2)

stflogger.debug('----- ***** starting simple test ***** -----')

h1 = HostsData("../config/host_list.conf")
for key, value in h1.hosts.items():
    print ("host {} and credentials {}".format(key, h1.hosts[key]))

cases = TestCasesData('../config/testcase_list.conf')
for key, value in cases.testcases.items():
    print("host {} and testcase on this host {}".format(key, cases.testcases[key]))
        
propty = PropertiesData('../config/properties.conf')
for key, value in propty.properties.items():
    print("property {} and its value is {}".format(key, propty.properties[key]))


