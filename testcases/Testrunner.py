# this file is top level executor
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from common.hosts import *
cwd = os.getcwd()
os.chdir('TestFrameWork/testcases')
cwd = os.getcwd()
print(cwd)
h1 = HostData("..\config\host_list.conf")

