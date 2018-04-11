# class file to cread properties 
import re
class PropertiesData:
    properties = {}
    def __init__ (self, filename='../config/properties.conf'):
        with open(filename, mode='r') as fd:
            for line in fd:
                if (line == "\n"):
                    continue
                if (re.match(r'^#', line)):
                    continue
                temp = line.split('=')
                self.properties[temp[0]]=temp[1]
            else:
                print("processed properties file")
            