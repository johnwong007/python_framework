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
        根据配置情况，分配游戏服务
        1.支持比赛桌与现金桌分离
        2.支持指定赛事指定Game服务
        3.支持指定现金桌指定Game服务
        4.支持锁
    '''
    def __init__( self ):
        '''
            加载配置
        '''
        self.rlock = router_lock            # 线程锁，防止两个线程同时操作一个Router对象
        
        self.game_list              = {}    # 游戏服务列表 {game1 : table_num, game2 : table_num, ...}
        
        self.config_cash_server     = []    # 配置：现金桌服务
        self.config_match_server    = []    # 配置：赛事服务
        self.config_gold_server     = []    # 配置：金币场
        self.config_rakepoint_server= []    # 配置：积分场
        self.config_tourney         = []    # 配置：锦标赛
        self.config_sitandgo        = []    # 配置：坐满即玩
        
        self.load_config()
                
        
    def load_config( self ):
        '''
            加载服务分配配置方案
        '''
        try:
            self.config_cash_server         = Config.GAMEADDR_CASH.split( ',' )     #加载现金桌配置
            self.config_match_server        = Config.GAMEADDR_MATCH.split( ',' )    #加载比赛配置
            self.config_gold_server         = Config.GAMEADDR_GOLD.split( ',' )     #加载金币场配置
            self.config_rakepoint_server    = Config.GAMEADDR_RAKEPOINT.split( ',' )   #加载积分场配置
            self.config_tourney             = Config.GAMEADDR_TOURNEY.split( ',' )  #加载锦标赛配置
            self.config_sitandgo            = Config.GAMEADDR_SITANDGO.split( ',' ) #加载坐满即玩配置
        except:
            logging.error('Game router load config failed!')
            return False
            
            
    def add_gameaddr( self, server_name ):
        '''
            添加一个游戏服务
        '''
        if self.game_list.has_key( server_name ):
            return 
            
        logging.info('add a gameaddr [%s]'%server_name)
        self.game_list[server_name] = 0                    #初始化该服务下挂载牌桌数量为0
        
        
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
            增加game服务下挂载的牌桌数量
        '''
        try:
            self.rlock.acquire()                    #申请锁
            if game_name not in self.game_list:
                logging.error('from inc_table_count : game_name [%s] not in game_list'%game_name)
                return False
                        
            self.game_list[game_name] += count
            logging.info('%s table_num + %s'%(game_name, count))
        finally:
            self.rlock.release()                    #释放锁
        
        
    def del_talbe_count(self, game_name, count = 1):
        '''
            减少game服务下挂载的牌桌数量
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
            计算总牌桌数
        '''
        count = 0
        
        for name in self.game_list.keys():
            count += self.game_list[name]
            
        return count
        
    def get_target_gameaddr(self, table_num_create, sort, type):
        '''
            获取符合条件的游戏服务列表
        '''
        #无限制
        if Config.GAMEADDR_CASH == 'NO' or Config.GAMEADDR_MATCH == 'NO':
            game_list = game_filter( self.game_list, self.game_list.keys() )
            return game_list
            
        #有大类限制    
        else:
            #无子类限制
            if Config.GAMEADDR_RAKEPOINT == 'NO' or Config.GAMEADDR_GOLD == 'NO':
                if sort == 'CASH':
                    res = game_filter( self.game_list, self.config_cash_server )
                    return res
                elif sort == 'TOURNEY' or sort == 'SITANDGO':
                    res = game_filter( self.game_list, self.config_match_server )
                    return res
            else:
                #有子类限制
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
            功能：根据要创建的牌桌个数，生成游戏服务列表
            入参：sort ： 牌桌大类   CASH/MATCH
                  type :  牌桌子类   RAKEPOINT/GOLD    TOURNEY/SITANDGO
            出参：glist
        '''
        logging.info('table_num = %s, target_gameaddr = %s, sort = %s, type = %s'
                        %(table_num_create, target_gameaddr, sort, type))
        glist = []
        
        # 1.如果有指定的Game服务，则直接把桌子全部创到这个服务上去
        if target_gameaddr in self.game_list:
            for i in range( table_num_create ):
                game_name   = target_gameaddr
                remote_addr = (Config.GAME_GROUP_NAME, game_name)
                glist.append( remote_addr )
                
            self.inc_table_count( game_name, table_num_create )
            return glist
        
        #记录一下错误信息
        if target_gameaddr != None:
            logging.error('generate_game_list: not exist gameaddr [%s] '%target_gameaddr)
        
        gameaddr_list = self.get_target_gameaddr(table_num_create, sort, type)
        
        if len( gameaddr_list ) <= 0:
            logging.error( 'there is not single game address!' )
            return self

        # 2.只有一个地址的情况下，很好处理
        if len( gameaddr_list ) == 1:
            for i in range( table_num_create ):
                game_name   = gameaddr_list.keys()[0]
                remote_addr = (Config.GAME_GROUP_NAME, game_name)
                glist.append( remote_addr )
                
            self.inc_table_count( game_name, table_num_create )
            return glist

        # 3.其他情况：取最多、最少牌桌的游戏
        

        # 算法的基本思路是：
        #     取最小牌桌数量的Game服务
        for i in range( table_num_create ):
            
            max_name, min_name = get_max_and_min_table_game( gameaddr_list )
            # 取到一个游戏地址
            game_name   = min_name
            remote_addr = (Config.GAME_GROUP_NAME, game_name)

            # 登记到缓存
            glist.append( remote_addr )
            self.inc_table_count( game_name )
            gameaddr_list[ game_name ] += 1
            

        return glist

    

def init():

    game_router = Router()                  #实例化一个Router对象
    
    game_addr_map = Memory.getall( Config.GAME_ADDR_PREFIX )
    for serv_name in game_addr_map.keys():
        game_router.add_gameaddr( serv_name )
        
    _GAMEROUTER_.append( game_router )      
    
    
def get_gamerouter():
    '''
        目前只有一个gamerouter
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
        游戏服务过滤器
        功能：从src_dict中过滤出符合config的game服务
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
    latest_game_list    = game_addr_map.keys()                          #最新的Game服务列表
    old_game_list       = gamerouter.game_list.keys()                   #旧的Game服务列表

    # 插入没有的
    for serv_name in latest_game_list:
        gamerouter.add_gameaddr( serv_name )

    # 去掉消失的
    for serv_name in old_game_list:
        if serv_name not in latest_game_list:
            gamerouter.remove_gameaddr( serv_name )

    # 更新t_config_match_addr
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




