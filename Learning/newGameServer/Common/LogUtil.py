#coding=gbk
import os
import logging
import logging.handlers


def addTimedRotatingFileHandler(filename, **kwargs):
    """��logger���һ��ʱ���л��ļ���handler��
    Ĭ��ʱ����0�㣬30�����ݡ������ָ��logger����ʹ��logging.getLogger()��Ҳ����RootLogger��
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
    """��logger���һ����С�л��ļ���handler��
    Ĭ�ϴ�С��10M��30�����ݡ������ָ��logger����ʹ��logging.getLogger()��Ҳ����RootLogger��
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

