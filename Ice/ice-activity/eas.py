#coding:utf8

import logging

import imp
import sys
import os

_BASIC_PATH_ = os.path.abspath(__file__)
_BASIC_PATH_ = _BASIC_PATH_[:_BASIC_PATH_.rfind('/bin')]
# print('_BASIC_PATH_ is '+_BASIC_PATH_)
sys.path.append(_BASIC_PATH_+'/'+'mod')
# print(sys.path)
# print(_BASIC_PATH_)
logging.basicConfig(filename='./jsinfo.log', level=logging.DEBUG)
# import activity.activity as ac
def _import(path):
    comps = path.split('.')
    if sys.path.count(_BASIC_PATH_+'/'+comps[0])==0:
        sys.path.append(_BASIC_PATH_+'/'+comps[0])
    i, model = 1, None
    # model = '.'.join(comps[1:3])
    # print(model)

    while(i<=len(comps[1:])):
        try:
            pass
            # model = __import__('.'.join(comps[1:i+1]))
        except:
            print('except')
        i = i+1
    m = imp.load_source(path.replace('.','_'), _BASIC_PATH_+'/'+'/'.join(comps)+'.py')
    return m

def _load(model, path):
    # print(model)
    # print(path)
    model = _import(path)
    return model

if __name__ == '__main__':
    models = {
                'activity': {'path': 'mod.activity.activity'},
                'activityApi': {'path': 'mod.activity.activityApi'}
              }
    for model in models:
        if type(model)=='dict':
            for m in model:
                pass
                # _load(m, model[m]['path'])
            # logging.info('111111')
        else:
            activity = _load(model, models[model]['path'])
            act_obj = activity.reg_interface(1)
            # act_obj.printer()
            if hasattr(act_obj, 'printer'):
                getattr(act_obj, 'printer')()
