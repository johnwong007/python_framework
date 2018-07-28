#时间限制
table_unstart_dict={
2:["7","6"],
3:["1","3","8"],
4:["2","4"],
7:["5","15"],
8:["76","16"]
}
__MAX_PLAYRNUM_TABLE__ = 9

class TableManger:    
    
    def __init__(self):
        pass
    
    # <<<TODO
    def check_dismiss_is_ok(dismiss_num, table_unstart_dict):
        '''检测是否可以解散牌桌'''
        remain_sum = 0
        for i in table_unstart_list.keys():   
            if i == dismiss_num:
                pass
            else:
                remain_i = len(table_unstart_list[i])*(__MAX_PLAYRNUM_TABLE__ - i)         
            remain_sum = remain_sum + remain_i
        if dismiss_num < remain_sum:
            return False
        return True

    
    def add_tactics_group(target_table, from_key, to_key):
        '''加入新的策略组'''
        table_unstart_dict[from_key].remove(target_table)
        target_table_list = table_unstart_dict.get(to_key)
        if target_table_list == None:
            table_unstart_dict[to_key]=[target_table]
        else:
            target_table_list.append(target_table)
    
    
    def autoreset_dismiss(self, dismiss_key):
        '''解散人数较少的赛桌并分配到其他桌中'''
        table_list = table_unstart_dict.get(dismiss_key)
        if None == table_list:
            return None
        
        for table in table_list:
            if not self.check_dismiss_is_ok(dismiss_key, table_unstart_dict):
                return None
            
            # 获取牌桌上的玩家列表
            players = get_table_player(table)            
            for player in players:
                # 加入新的房间
                union_key, target_table = choose_one_table(table_unstart_dict， dismiss_key)
                
                join_table(target_table, player)
                
                # 加入新的策略组
                add_tactics_group(target_table, union_key, union_key+1)
            
            # table添加到人数为0的策略组
            add_tactics_group(table, 0)
            
                
    def autoreset_union(self, union_key):
        '''合并人数较少的牌桌'''
        table_list = table_unstart_dict.get(union_key)
        
    
    def autoreset_table(self):
        '''重置赛桌'''
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        
        # 解散人数少的牌桌并重新分配
        for item in list_of_num:
            if item < __LIMIT__AUTOSET__:
                autoreset_dismiss(item)
        
        # 合并可以合并的牌桌
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        for item in list_of_num:
            autoreset_union(item)
            
        
        # 合并可以合并的牌桌
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        for item in list_of_num:
            autoreset_union(item)
        
        
        # 增加牌桌数目
        if table_unstart_list.get(0, 0) < __FREE_TABLE__:
            create_table()
        