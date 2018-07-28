#coding=gbk

import threading
import zlog as logging
from .. import Label
from . import Match
from . import Table

END_EVENT = threading.Event()

def endSignalHandler(signum, frame):
    matchs = Match.get_all_match()
    for match_id, match in matchs.items():
        sq_regroup_table = match.sq_regroup_table
        if not Label.unset( sq_regroup_table ):
            logging.error( 'regrouping, try later [ match : %s ]'%match_id )
            #return False # 测试的时候注销掉
    
    END_EVENT.set()
    return True

def try_to_set_end_event():
    matchs = Match.get_all_match()
    for match_id, match in matchs.items():
        sq_regroup_table = match.sq_regroup_table
        if not Label.unset( sq_regroup_table ):
            logging.error( 'regrouping, try later [ match : %s ]'%match_id )
            return False

    tables = Table.get_all_table()
    for table_id, table in tables.items():
        if len( table.zombie_players ) > 0:
            logging.error( 'there are zombie players, try later  [ table : %s ]'%table_id )
            return False

    END_EVENT.set()
    return True

def force_to_end_event():
    END_EVENT.set()
    return True
