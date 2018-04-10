# class file to cread properties 
class PropertiesClass:
    def __init__ (self, filename):
        try: 
            fd = open(filename, mdoe='r')
            for line in fd:
                print(line)
        exception: FileNotFoundError || IOError
            print(problem with properties files please check) 
            