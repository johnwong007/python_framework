#coding=gbk
import os
import sys
import time
import signal
import threading


def load_module(mod_name, paths=None):
    """（在指定路径里面）加载一个module"""
    import imp
    mod_data = imp.find_module(mod_name, paths)
    mod_obj = imp.load_module(mod_name, *mod_data)
    if mod_data[0]:
        mod_data[0].close()
    return mod_obj


def createDaemon(**kwargs):
    """使本进程进入daemon状态"""
    conf = {
        'stdin': os.devnull,
        'stdout': os.devnull,
        'stderr': os.devnull,
    }
    conf.update(kwargs)
    pid = os.fork()
    if pid:
        os._exit(0)
    os.setsid()
    pid = os.fork()
    if pid:
        os._exit(0)
    os.chdir('/')
    os.umask(0)
    for i in (('stdin', 'r'), ('stdout', 'a+'), ('stderr', 'a+')):
        f = conf[i[0]]
        if not hasattr(f, 'fileno'):
            f = open(f, i[1])
        fd = getattr(sys, i[0]).fileno()
        os.close(fd)
        os.dup2(f.fileno(), fd)
    return os.getpid()

daemonize = createDaemon


class ServiceX:
    """服务pid小工具"""

    def __init__(self, id):
        self.id = id
        self.pidFile = os.environ['_BASIC_PATH_'] + '/var/run/' + id + '.pid'

    def status(self):
        if not os.path.isfile(self.pidFile):
            return 0
        f = open(self.pidFile, 'r')
        pid = f.read()
        f.close()
        fname = '/proc/' + pid
        if not os.path.isdir(fname):
            return 0
        if os.stat(fname)[4] != os.getuid():
            return 0
        return int(pid)

    def start(self):
        pid = os.getpid()
        dname = os.path.dirname(self.pidFile)
        if not os.path.isdir(dname):
            os.makedirs(dname, 0755)
        f = open(self.pidFile, 'w')
        f.write(str(pid))
        f.close()
        return pid

    def clear(self):
        os.remove(self.pidFile)

    def stop(self):
        pid = self.status()
        if pid == 0:
            return -1
        for i in range(20):
            os.kill(pid, signal.SIGTERM)
            time.sleep(0.3)
            if self.status() == 0:
                return 0
        return -2
        
        
############################################################


class IdManager:
    
    def __init__(self):
        self.lock = threading.Lock()
        self.time = time.localtime()
        self.timeFormat = '%Y%m%d%H%M%S'
        self.id = 1
        self.idFormat = '%04d'

    def allocate(self):
        self.lock.acquire()
        t = time.localtime()
        if t != self.time:
            self.time = t
            self.id = 1
        id = self.idFormat % self.id
        self.id += 1
        self.lock.release()
        return time.strftime(self.timeFormat, t) + id


############################################################

