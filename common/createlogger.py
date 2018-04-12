# this file creates logger object for the framework

import logging

class TestFrameWorklogger:
    """ returns a logger object """
    stflogger = logging.getLogger('__name__')
    def __init__(self):    
        self.stflogger = logging.getLogger('__name__')
        self.stflogger.setLevel(logging.DEBUG)
        handler1 = logging.StreamHandler()
        handler2 = logging.FileHandler('../logs/stflog.log', mode='a')
        frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler1.setFormatter(frmt)
        handler2.setFormatter(frmt)
        self.stflogger.addHandler(handler1)
        self.stflogger.addHandler(handler2)
        self.stflogger.info('----- logger initialized -----')
        
    def logmessage(self, msg, lvl='INFO'):
        if lvl == "INFO":
            self.stflogger.info(msg)
        if lvl == "DEBUG":
            self.stflogger.debug(msg)
        if lvl == "CRITICAL":
            self.stflogger.critical(msg)
        if lvl == "WARNING":
            self.stflogger.warning(msg)

        
    