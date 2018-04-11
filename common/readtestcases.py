""" this class reads testcases config file """
import re

class TestCasesData:
    testcases = {}
    def __init__(self, filename='../config/testcase_list.conf'):
        with open(filename, mode='r') as fd1:
            for line in fd1:
                # ignore blank line
                if line == '\n':
                    continue
                # ignore comment line
                if (re.match(r'^#', line)) :                 
                    continue
                temp = line.split(r':')
                self.testcases[temp[0]] = temp[1]
            else:
                print('processed test cases file')
    
