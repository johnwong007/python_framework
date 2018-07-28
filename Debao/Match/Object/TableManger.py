#ʱ������
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
        '''����Ƿ���Խ�ɢ����'''
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
        '''�����µĲ�����'''
        table_unstart_dict[from_key].remove(target_table)
        target_table_list = table_unstart_dict.get(to_key)
        if target_table_list == None:
            table_unstart_dict[to_key]=[target_table]
        else:
            target_table_list.append(target_table)
    
    
    def autoreset_dismiss(self, dismiss_key):
        '''��ɢ�������ٵ����������䵽��������'''
        table_list = table_unstart_dict.get(dismiss_key)
        if None == table_list:
            return None
        
        for table in table_list:
            if not self.check_dismiss_is_ok(dismiss_key, table_unstart_dict):
                return None
            
            # ��ȡ�����ϵ�����б�
            players = get_table_player(table)            
            for player in players:
                # �����µķ���
                union_key, target_table = choose_one_table(table_unstart_dict�� dismiss_key)
                
                join_table(target_table, player)
                
                # �����µĲ�����
                add_tactics_group(target_table, union_key, union_key+1)
            
            # table��ӵ�����Ϊ0�Ĳ�����
            add_tactics_group(table, 0)
            
                
    def autoreset_union(self, union_key):
        '''�ϲ��������ٵ�����'''
        table_list = table_unstart_dict.get(union_key)
        
    
    def autoreset_table(self):
        '''��������'''
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        
        # ��ɢ�����ٵ����������·���
        for item in list_of_num:
            if item < __LIMIT__AUTOSET__:
                autoreset_dismiss(item)
        
        # �ϲ����Ժϲ�������
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        for item in list_of_num:
            autoreset_union(item)
            
        
        # �ϲ����Ժϲ�������
        list_of_num = table_unstart_dict.keys()    
        list_of_num.sort() 
        for item in list_of_num:
            autoreset_union(item)
        
        
        # ����������Ŀ
        if table_unstart_list.get(0, 0) < __FREE_TABLE__:
            create_table()
        