# this file is top level executor
 
import os,sys,inspect
# add script directory to python sreachable locations
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from common.readhosts import *
from common.readtestcases import *
from common.readproperties import *

#change working directory to script location
cwd = os.getcwd()
os.chdir('TestFrameWork/testcases')
cwd = os.getcwd()
print(cwd)
print('path to the script {}'.format(currentdir))

h1 = HostsData("../config/host_list.conf")
for key, value in h1.hosts.items():
    print ("host {} and credentials {}".format(key, h1.hosts[key]))

cases = TestCasesData('../config/testcase_list.conf')
for key, value in cases.testcases.items():
    print("host {} and testcase on this host {}".format(key, cases.testcases[key]))
        
propty = PropertiesData('../config/properties.conf')
for key, value in propty.properties.items():
    print("property {} and its value is {}".format(key, propty.properties[key]))


