#coding=gbk
'''GAME SERVER 数据结构持久化模块'''

import cPickle as pickle

def dump( fname, obj_list ):
    '''dump'''              
    file_o = file( fname, 'wb')
    
    for obj in obj_list:
        pickle.dump( obj, file_o, True )
        
    file_o.close()              
    return True              
    
def load( fname ):
    '''load'''
    obj_list = []   
    file_o = file( fname,'rb' ) 

    while(True):
        try:
            obj = pickle.load( file_o )        
            obj_list.append( obj )
        except:
            file_o.close()            
            return obj_list
       