#coding:utf-8
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"
logging.basicConfig(filename="test_log.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.log(logging.DEBUG, "debug")
logging.log(logging.INFO, "info")
logging.log(logging.WARNING, "warning")
logging.log(logging.ERROR, "error")
logging.log(logging.CRITICAL, "critical")
str = "hello python"
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.info(str)
