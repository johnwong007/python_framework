#coding=gbk
''' 存储游戏服务的内存内容 '''


# 牌桌标识符到牌桌对象引用的映射关系 
table_list = {
    #tableid : table object,
    #...
}


# (用户id + '_' + 赛桌id) 到远处服务名的映射关系
ut2remote = {    
    # ut : ( group_name,server_name )
    # ...
}

# (用户id + '_' + 赛桌id) 到座位号的映射关系
ut2seatid = {
    # ut : seat_pos
}


# 牌桌描述符到赛事server的映射关系
tableid2match    = {
    # tableid ：( group_name,server_name )   
    # ...
}