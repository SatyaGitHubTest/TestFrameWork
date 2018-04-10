import os

class HostData:
  """ this is host class which reads hosts.conf file """
  file = "..\config\host_list.conf"
  os
  hosts = {}
  def __init__ (self, filename):
    fd = open(self.file, mode="r")
    for line in fd:
        print(line)
#    except IOError:
#        print("IOError while opening the file {}".format(self.file))
##    except FileNotFoundError:
#        print("File not found {}".format(file))
    