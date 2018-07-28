#coding=utf-8
import Protocol as P

DE_LOCALS = {}
LOCAL_V = P.LOCAL_V

def dede():
    ''' 对该py文件中的 变量 反向查找 解码 '''
    global DE_LOCALS
    for i in LOCAL_V.items():
        if type(i[1]) == str or type(i[1]) == int:
            DE_LOCALS[i[1]] = i[0]
            DE_LOCALS[i[0]] = i[1]

def getde(key):
    ''' 获取value对应的key'''
    return DE_LOCALS.get(key, key)





def read( obj ):
    
    #print obj
    if type(obj) == dict:
        result = dict()
        for k, v in obj.items():
            
            if type(v) == dict or type(v) == list:
                v = read(v)
            else :
                v = getde(v)

            result[ getde(k) ] = v

    elif type(obj) == list:
        result = list()
        for v in obj:
            v = read( v )
            result.append(v)

    else:
        result = obj


    return result


dede()



