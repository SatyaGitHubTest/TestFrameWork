import logging

logger = logging.getLogger(__name__)
print(logger)
logger.setLevel(logging.DEBUG)
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler('../logs/stflog.log', mode='a')
frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler1.setFormatter(frmt)
handler2.setFormatter(frmt)
logger.addHandler(handler1)
logger.addHandler(handler2)
logger.info("logger initialized in __init__ .py file")

