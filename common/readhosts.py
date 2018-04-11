# This class reads hosts config file

import re 

class HostsData:
  """ this is host class which reads hosts.conf file
      and create host objects """
  
  hosts = {}
  def __init__ (self, filename='../config/host_list.conf'):
    with open(filename, mode="r") as fd:
        for line in fd:
          if (line == "\n"):
            continue 
          if (re.match(r'^#', line)):
            continue
          temp = line.split(':')
          self.hosts[temp[0]] = temp[1]
        else:
          print("finished processing host file") 
