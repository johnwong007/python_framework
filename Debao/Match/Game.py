#coding=utf-8
import zlog as logging
import threading

import sys
from . import Config
from . import Memory
from . import Match
import Object.Match as MatchObject
import Object.Cash as CashObject


_GAMEROUTER_ = []

router_lock = threading.Lock()



class Router:
    '''
        �������������������Ϸ����
        1.֧�ֱ��������ֽ�������
        2.֧��ָ������ָ��Game����
        3.֧��ָ���ֽ���ָ��Game����
        4.֧����
    '''
    def __init__( self ):
        '''
            ��������
        '''
        self.rlock = router_lock            # �߳�������ֹ�����߳�ͬʱ����һ��Router����
        
        self.game_list              = {}    # ��Ϸ�����б� {game1 : table_num, game2 : table_num, ...}
        
        self.config_cash_server     = []    # ���ã��ֽ�������
        self.config_match_server    = []    # ���ã����·���
        self.config_gold_server     = []    # ���ã���ҳ�
        self.config_rakepoint_server= []    # ���ã����ֳ�
        self.config_tourney         = []    # ���ã�������
        self.config_sitandgo        = []    # ���ã���������
        
        self.load_config()
                
        
    def load_config( self ):
        '''
            ���ط���������÷���
        '''
        try:
            self.config_cash_server         = Config.GAMEADDR_CASH.split( ',' )     #�����ֽ�������
            self.config_match_server        = Config.GAMEADDR_MATCH.split( ',' )    #���ر�������
            self.config_gold_server         = Config.GAMEADDR_GOLD.split( ',' )     #���ؽ�ҳ�����
            self.config_rakepoint_server    = Config.GAMEADDR_RAKEPOINT.split( ',' )   #���ػ��ֳ�����
            self.config_tourney             = Config.GAMEADDR_TOURNEY.split( ',' )  #���ؽ���������
            self.config_sitandgo            = Config.GAMEADDR_SITANDGO.split( ',' ) #����������������
        except:
            logging.error('Game router load config failed!')
            return False
            
            
    def add_gameaddr( self, server_name ):
        '''
            ���һ����Ϸ����
        '''
        if self.game_list.has_key( server_name ):
            return 
            
        logging.info('add a gameaddr [%s]'%server_name)
        self.game_list[server_name] = 0                    #��ʼ���÷����¹�����������Ϊ0
        
        
    def remove_gameaddr( self, server_name ):
        ''''''
        if self.game_list.has_key( server_name ):
            if self.game_list[server_name] != 0:
                logging.error('can not remove gameaddr[%s], table_num != 0'%server_name)
                return False
            del self.game_list[server_name]
        else:
            logging.error('from remove_gameaddr : no exist server_name[%s]'%server_name)
        
        
    def inc_table_count(self, game_name, count = 1):
        '''
            ����game�����¹��ص���������
        '''
        try:
            self.rlock.acquire()                    #������
            if game_name not in self.game_list:
                logging.error('from inc_table_count : game_name [%s] not in game_list'%game_name)
                return False
                        
            self.game_list[game_name] += count
            logging.info('%s table_num + %s'%(game_name, count))
        finally:
            self.rlock.release()                    #�ͷ���
        
        
    def del_talbe_count(self, game_name, count = 1):
        '''
            ����game�����¹��ص���������
        '''
        try:
            self.rlock.acquire()
            if game_name not in self.game_list:
                logging.error('from del_talbe_count : game_name [%s] not in game_list'%game_name)
                return False
                
            self.game_list[game_name] -= count
            
            logging.info('del_talbe_count : %s realtime table_num %s : '%( game_name, self.game_list[game_name] ))
            #if self.game_list[game_name] < 0:
            #    self.game_list[game_name] = 0
            
        finally:
            self.rlock.release()
        
        
    def get_total_tablenum( self ):
        '''
            ������������
        '''
        count = 0
        
        for name in self.game_list.keys():
            count += self.game_list[name]
            
        return count
        
    def get_target_gameaddr(self, table_num_create, sort, type):
        '''
            ��ȡ������������Ϸ�����б�
        '''
        #������
        if Config.GAMEADDR_CASH == 'NO' or Config.GAMEADDR_MATCH == 'NO':
            game_list = game_filter( self.game_list, self.game_list.keys() )
            return game_list
            
        #�д�������    
        else:
            #����������
            if Config.GAMEADDR_RAKEPOINT == 'NO' or Config.GAMEADDR_GOLD == 'NO':
                if sort == 'CASH':
                    res = game_filter( self.game_list, self.config_cash_server )
                    return res
                elif sort == 'TOURNEY' or sort == 'SITANDGO':
                    res = game_filter( self.game_list, self.config_match_server )
                    return res
            else:
                #����������
                config_limit = None
                if sort == 'CASH':
                    if type == 'GOLD':
                        config_limit = self.config_gold_server
                    elif type in ('RAKEPOINT', 'VGOLD', 'POINT'):
                        config_limit = self.config_rakepoint_server
                    
                    res = game_filter( self.game_list, self.config_cash_server )
                    right_list = game_filter( res, config_limit)
                    return right_list
                    
                elif sort == 'TOURNEY' or sort == 'SITANDGO':
                    if sort == 'TOURNEY':
                        config_limit = self.config_tourney
                    elif sort == 'SITANDGO':
                        config_limit = self.config_sitandgo
                    
                    res = game_filter( self.game_list, self.config_match_server )
                    right_list = game_filter( res, config_limit)
                    return right_list

    def generate_game_list( self, table_num_create, target_gameaddr = None, sort = 'NO', type = 'NO' ):
        '''
            ���ܣ�����Ҫ����������������������Ϸ�����б�
            ��Σ�sort �� ��������   CASH/MATCH
                  type :  ��������   RAKEPOINT/GOLD    TOURNEY/SITANDGO
            ���Σ�glist
        '''
        logging.info('table_num = %s, target_gameaddr = %s, sort = %s, type = %s'
                        %(table_num_create, target_gameaddr, sort, type))
        glist = []
        
        # 1.�����ָ����Game������ֱ�Ӱ�����ȫ���������������ȥ
        if target_gameaddr in self.game_list:
            for i in range( table_num_create ):
                game_name   = target_gameaddr
                remote_addr = (Config.GAME_GROUP_NAME, game_name)
                glist.append( remote_addr )
                
            self.inc_table_count( game_name, table_num_create )
            return glist
        
        #��¼һ�´�����Ϣ
        if target_gameaddr != None:
            logging.error('generate_game_list: not exist gameaddr [%s] '%target_gameaddr)
        
        gameaddr_list = self.get_target_gameaddr(table_num_create, sort, type)
        
        if len( gameaddr_list ) <= 0:
            logging.error( 'there is not single game address!' )
            return self

        # 2.ֻ��һ����ַ������£��ܺô���
        if len( gameaddr_list ) == 1:
            for i in range( table_num_create ):
                game_name   = gameaddr_list.keys()[0]
                remote_addr = (Config.GAME_GROUP_NAME, game_name)
                glist.append( remote_addr )
                
            self.inc_table_count( game_name, table_num_create )
            return glist

        # 3.���������ȡ��ࡢ������������Ϸ
        

        # �㷨�Ļ���˼·�ǣ�
        #     ȡ��С����������Game����
        for i in range( table_num_create ):
            
            max_name, min_name = get_max_and_min_table_game( gameaddr_list )
            # ȡ��һ����Ϸ��ַ
            game_name   = min_name
            remote_addr = (Config.GAME_GROUP_NAME, game_name)

            # �Ǽǵ�����
            glist.append( remote_addr )
            self.inc_table_count( game_name )
            gameaddr_list[ game_name ] += 1
            

        return glist

    

def init():

    game_router = Router()                  #ʵ����һ��Router����
    
    game_addr_map = Memory.getall( Config.GAME_ADDR_PREFIX )
    for serv_name in game_addr_map.keys():
        game_router.add_gameaddr( serv_name )
        
    _GAMEROUTER_.append( game_router )      
    
    
def get_gamerouter():
    '''
        Ŀǰֻ��һ��gamerouter
    '''
    if len( _GAMEROUTER_ ) != 0:
        return _GAMEROUTER_[0]
    else:
        return None
        
        
def remove_gamerouter():
    ''''''
    pass
    
    
def game_filter(src_dict, config):
    '''
        ��Ϸ���������
        ���ܣ���src_dict�й��˳�����config��game����
    '''
    if not config:
        return src_dict

    res_dict = {}
    
    for name in src_dict.keys():
        if name in config:
            res_dict[name] = src_dict[name]
          
    return res_dict
    

def check():
    
    gamerouter = get_gamerouter()
    
    logging.info('GameServer: %s'%gamerouter.game_list)

    game_addr_map       = Memory.getall( Config.GAME_ADDR_PREFIX )      
    latest_game_list    = game_addr_map.keys()                          #���µ�Game�����б�
    old_game_list       = gamerouter.game_list.keys()                   #�ɵ�Game�����б�

    # ����û�е�
    for serv_name in latest_game_list:
        gamerouter.add_gameaddr( serv_name )

    # ȥ����ʧ��
    for serv_name in old_game_list:
        if serv_name not in latest_game_list:
            gamerouter.remove_gameaddr( serv_name )

    # ����t_config_match_addr
    total_table_num = gamerouter.get_total_tablenum()
    
    serv_name = sys.argv[1]
    addr = ( Config.LOCAL_GROUP_NAME, serv_name )
    addr = str(addr)
    Match.update_match_addr_config_tnum( total_table_num, addr )



def get_max_and_min_table_game( gameaddr_list ):
    
    
    
    max_name  = gameaddr_list.keys()[0]
    max_cnt   = gameaddr_list[max_name]
    min_name  = gameaddr_list.keys()[0]
    min_cnt   = gameaddr_list[min_name]
    
    for name, cnt in gameaddr_list.items():

        if cnt < min_cnt:
            min_name  = name
            min_cnt   = cnt
        elif cnt > max_cnt:
            max_name  = name
            max_cnt   = cnt

    return max_name, min_name




