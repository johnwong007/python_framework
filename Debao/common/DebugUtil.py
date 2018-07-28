#coding=gbk
"""debug工具集
"""
import os
import re
import cProfile
import threading


_PROFILE_ENV_KEY_ = 'PYTHON_PROFILE_PREFIX'
_PROFILE_DATAS_ = {}


def set_profile_prefix(prefix):
    """设置profile文件记录路径的前缀
        注意：只有先执行了这个，profile_thread_call才会有实际效果
    """
    os.environ[_PROFILE_ENV_KEY_] = prefix


def get_profile_prefix():
    """获取profile文件记录路径的前缀
    """
    return os.getenv(_PROFILE_ENV_KEY_)


def profile_thread_call(func):
    """线程profile修饰函数
    """
    if not get_profile_prefix():
        # debug没打开，不需要修饰，直接返回原函数就不会影响效率
        return func
    def deco_func(*args, **kwargs):
        th_name = threading.current_thread().name
        prof = _PROFILE_DATAS_.get(th_name)
        if not prof:
            prof = cProfile.Profile()
            _PROFILE_DATAS_[th_name] = prof
        prof.enable()
        try:
            return func(*args, **kwargs)
        finally:
            prof.disable()
    return deco_func


def save_profile_datas():
    """保存所有profile到文件
    """
    for k, v in _PROFILE_DATAS_.items():
        v.disable()
        v.dump_stats('%s.%s' % (get_profile_prefix(), k))
import atexit
atexit.register(save_profile_datas)


############################################################


class ProfileThread(threading.Thread):
    """可以profiling的线程
    """

    def __init__(self, *args, **kwargs):
        """线程初始化
            增加profile参数，可以指定profile记录的路径，否则参考DebugUtil。
        """
        self._prof_ = kwargs.pop('profile', None)
        threading.Thread.__init__(self, *args, **kwargs)
        if not self._prof_ and get_profile_prefix():
            func = re.search('function (\w+)', str(self._Thread__target)).group(1)
            self._prof_ = get_profile_prefix() + '.' + func

    def run(self):
        if self._prof_:
            prof = cProfile.Profile()
            try:
                prof.runcall(threading.Thread.run, self)
            finally:
                prof.dump_stats(self._prof_)
        else:
            threading.Thread.run(self)

