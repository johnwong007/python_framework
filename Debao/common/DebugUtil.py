#coding=gbk
"""debug���߼�
"""
import os
import re
import cProfile
import threading


_PROFILE_ENV_KEY_ = 'PYTHON_PROFILE_PREFIX'
_PROFILE_DATAS_ = {}


def set_profile_prefix(prefix):
    """����profile�ļ���¼·����ǰ׺
        ע�⣺ֻ����ִ���������profile_thread_call�Ż���ʵ��Ч��
    """
    os.environ[_PROFILE_ENV_KEY_] = prefix


def get_profile_prefix():
    """��ȡprofile�ļ���¼·����ǰ׺
    """
    return os.getenv(_PROFILE_ENV_KEY_)


def profile_thread_call(func):
    """�߳�profile���κ���
    """
    if not get_profile_prefix():
        # debugû�򿪣�����Ҫ���Σ�ֱ�ӷ���ԭ�����Ͳ���Ӱ��Ч��
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
    """��������profile���ļ�
    """
    for k, v in _PROFILE_DATAS_.items():
        v.disable()
        v.dump_stats('%s.%s' % (get_profile_prefix(), k))
import atexit
atexit.register(save_profile_datas)


############################################################


class ProfileThread(threading.Thread):
    """����profiling���߳�
    """

    def __init__(self, *args, **kwargs):
        """�̳߳�ʼ��
            ����profile����������ָ��profile��¼��·��������ο�DebugUtil��
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

