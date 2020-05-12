# coding:utf-8
import logging


def log():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"
    logging.basicConfig(filename="F:\\UI_auto_project\\Logs\\test_log.txt", level=logging.DEBUG, format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-3s: %(levelname)-3s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def log_INFO(value):
    log()
    logging.log(logging.INFO, value)


def log_DEBUG(value):
    log()
    logging.log(logging.DEBUG, value)


def log_WARNING(value):
    log()
    logging.log(logging.WARNING, value)


def log_ERROR(value):
    log()
    logging.log(logging.ERROR, value)
