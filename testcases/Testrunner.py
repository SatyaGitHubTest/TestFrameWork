# this file is top level executor
 
import os,sys,inspect
# add script directory to python sreachable locations
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))

#change working directory to script location
os.chdir(module_dir)

#import logger
#from testcases import logger
from common.readhosts import *
from common.readtestcases import *
from common.readproperties import *
from common.remoteclient import *

#logger = logging.getLogger()
logger.info('----- Starting test runner -----')

logger.info('hosts and their details')
h1 = HostsData("../config/host_list.conf")
for key, value in h1.hosts.items():
    logger.info ("{}-->{}".format(key, h1.hosts[key]))

logger.info('test cases and their details')
cases = TestCasesData('../config/testcase_list.conf')
for key, value in cases.testcases.items():
    logger.info ("host {} and testcase on this host {}".format(key, cases.testcases[key]))

logger.info('properties and their details')
propty = PropertiesData('../config/properties.conf')
for key, value in propty.properties.items():
    logger.info ("property {} and its value is {}".format(key, propty.properties[key]))
try:
  client1 = RemoteClient(hostname='192.168.1.10',port = '22', username = 'vagrant', key_file = None, password='vagrant') 
  out = client1.ex_cmd('ls -al')
  print(out)
except TimeoutError:
    logger.error('SSH timeout for -- {}'.format('hostname'))