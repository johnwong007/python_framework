#coding=gbk
import os
import logging
import logging.handlers


def addTimedRotatingFileHandler(filename, **kwargs):
    """给logger添加一个时间切换文件的handler。
    默认时间是0点，30个备份。如果不指定logger，则使用logging.getLogger()，也就是RootLogger。
    """
    dname = os.path.dirname(filename)
    if dname and not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    conf = {
        'when': 'midnight',
        'backupCount': 30,
        'format': '[%(asctime)s][%(filename)s:%(lineno)d] %(levelname)s: %(message)s',
        'logger': logging.getLogger(),
    }
    conf.update(kwargs)
    if conf.has_key('logLevel'):
        if isinstance(conf['logLevel'], str):
            conf['logLevel'] = getattr(logging, conf['logLevel'])
        conf['logger'].setLevel(conf['logLevel'])
    handler = logging.handlers.TimedRotatingFileHandler(
        filename = filename,
        when = conf['when'],
        backupCount = conf['backupCount'],
    )
    handler.setFormatter(
        logging.Formatter(conf['format'])
    )
    conf['logger'].addHandler(handler)


def addRotatingFileHandler(filename, **kwargs):
    """给logger添加一个大小切换文件的handler。
    默认大小是10M，30个备份。如果不指定logger，则使用logging.getLogger()，也就是RootLogger。
    """
    dname = os.path.dirname(filename)
    if dname and not os.path.isdir(dname):
        os.makedirs(dname, 0755)
    conf = {
        'maxBytes': 1024 * 1024 * 10,
        'backupCount': 30,
        'format': '[%(asctime)s] %(levelname)s: %(message)s',
        'logger': logging.getLogger(),
    }
    conf.update(kwargs)
    if conf.has_key('logLevel'):
        if isinstance(conf['logLevel'], str):
            conf['logLevel'] = getattr(logging, conf['logLevel'])
        conf['logger'].setLevel(conf['logLevel'])
    handler = logging.handlers.RotatingFileHandler(
        filename = filename,
        maxBytes = conf['maxBytes'],
        backupCount = conf['backupCount'],
    )
    handler.setFormatter(
        logging.Formatter(conf['format'])
    )
    conf['logger'].addHandler(handler)

