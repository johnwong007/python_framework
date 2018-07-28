#coding=utf-8

import sys, os
import time
import json
import threading
import logging
import traceback
import signal

if not os.environ.has_key('_BASIC_PATH_'):
    _BASIC_PATH_ = os.path.abspath(__file__)
    _BASIC_PATH_ = _BASIC_PATH_[:_BASIC_PATH_.rfind('/test/')]
    os.environ['_BASIC_PATH_'] = _BASIC_PATH_
if sys.path.count(os.environ['_BASIC_PATH_'] + '/lib') == 0:
    sys.path.append(os.environ['_BASIC_PATH_'] + '/mod')
    sys.path.append(os.environ['_BASIC_PATH_'] + '/lib')
    sys.path.append(os.environ['_BASIC_PATH_'] + '/lib/common')
    sys.path.append(os.environ['_BASIC_PATH_'] + '/libs')
    sys.path.append(os.environ['_BASIC_PATH_'] + '/libs/pypi')

import XmlConfig
XmlConfig.setEncoding('gbk')
XmlConfig.loadFile(_BASIC_PATH_ + '/etc/service.xml')



import Ice
Ice.loadSlice(_BASIC_PATH_+'/etc/EAS.ice')

import EasClient
import JsonUtil

if __name__ == '__main__':
    eas_instance = EasClient.EasClient().getInstance('account')
    func_name = sys.argv[1]
    if func_name  == 'createTencentOrder':
        params = { 
                    'orderid':'132453453451324'          ,    'uid':'6444'             ,
                                    'username':'holylee1088'         ,    'bank_type':'QQ'       ,
                                    'pay_channel':'QQ'     , 
                                    'charge_type':'DEBAO'      ,    'charge_num':'5'      ,  
                                    'acct_type':'2'        ,    'acct_num':'8'        , 
                                    'reward_num':''       ,    'charge_paramup':'sdfewasdf'  , 'content':''    , 
                                    'admin':''       ,    'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/createTencentOrder',params)
        print res
    if func_name  == 'sendProps':
        params = { 
                    'orderid':'132453453451324'          ,   'charge_paramdown':'sdfewasdf'  , 'content':''    , 
                                    'admin':''       ,    'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/sendProps',params)
        print res
    elif func_name == 'award':
        params = { 
                   'userid':'6444', 'limitid':'19999998'
                 }
        res = eas_instance.invoke('texasAcct/award',params)
        print res
    elif func_name == 'getIncreasePoint':
        params = { 
                   'uid':'543', 'start_time':'2012-11-26 00:00:00', 'end_time':'2012-12-03 00:00:00'
        
                 }
        res = eas_instance.invoke('activity/getIncreasePoint',params)
        print res
    elif func_name == 'getChargingOrderInfo':
        params = { 
                       'orderid':'20121115668899'
                 }
        res = eas_instance.invoke('texasAcct/getChargingOrderInfo',params)
        print res
    elif func_name == 'changeChargingOrderState':
        params = { 
                   'orderid':'20121115668899', 'status':'INIT'
                 }
        res = eas_instance.invoke('texasAcct/changeChargingOrderState',params)
        print res
    elif func_name == 'charging':
        params = { 
                     'orderid':'20121115668899','charge_paramdown':'WWW',
                     'transmoney':'3000', ''   'bank_orderid':'20121115668899'
                 }
        res = eas_instance.invoke('texasAcct/charging',params)
        print res
    elif func_name == 'markChargingError':
        params = { 
                     'orderid':'20121115668899','error_extentsion':'HAHA'
                 }
        res = eas_instance.invoke('texasAcct/markChargingError',params)
        print res
    elif func_name == 'matchApplyDeduct':
        params = { 
                   'orderid':'99999999999', 'userid':'6444', 
                   'username':'holylee1088', 'acct_type':'DEBAO', 
                   'transmoney':'100', 'channel':'LOBBY',
                   'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/matchApplyDeduct',params)
        print res
    elif func_name == 'matchApplyCancel':
        params = { 
                     'acct_orderid':'100272', 'userid':'6444', 'username':'holylee1088', 
                     'acct_type':'DEBAO', 'transmoney':'100'
                 }
        res = eas_instance.invoke('texasAcct/matchApplyCancel',params)
        print res
    elif func_name == 'depositPoint':
        params = { 
                   'orderid':'1979878', 'userid':'6444', 'username':'holylee1088',
                   'transmoney':'100', 'channel':'LOBBY'
                 }
        res = eas_instance.invoke('texasAcct/depositPoint',params)
        print res
    elif func_name == 'cashChipsExchangeIN':
        params = { 
                 'orderid':'9999999999','userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD', 'chips':'99999', 'channel':'LOBBY', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/cashChipsExchangeIN',params)
        print res
    elif func_name == 'matchPrize':
        params = { 
                  'orderid':'9999999999','userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD','transmoney':'100', 'channel':'LOBBY', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/matchPrize',params)
        print res
    elif func_name == 'eventPrize':
        params = { 
                 'orderid':'9999999999','userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD','transmoney':'100', 'channel':'LOBBY', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/eventPrize',params)
        print res
    elif func_name == 'exchangeDebao':
        params = { 
                 'userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD','debao_num':'1000', 'channel':'TEST', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/exchangeDebao',params)
        print res
    elif func_name == 'cashChipsExchangeOUT':
        params = { 
                   'orderid':'9999999999','userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD', 'chips':'99999', 'channel':'LOBBY', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/cashChipsExchangeOUT',params)
        print res
    elif func_name == 'getChargingOrderInfoByUid':
        params = { 
                    'uid':'6444', 'status':'SUC', 'offset':'0', 'fnum':'5'
                 }
        res = eas_instance.invoke('texasAcct/getChargingOrderInfoByUid',params)
        print res
    elif func_name == 'getChargingOrderStatus':
        params = { 
                    'uid':'6444', 'orderid':'20121115668899'
                 }
        res = eas_instance.invoke('texasAcct/getChargingOrderStatus',params)
        print res
    elif func_name == 'deductFromStore':
        params = { 
                 'orderid':'9999999999','userid':'6444', 'username':'holylee1088',
                 'acct_type':'GOLD','transmoney':'100', 'channel':'TEST', 'content':'', 'admin':'', 'adminnote':''
                 }
        res = eas_instance.invoke('texasAcct/deductFromStore',params)
        print res
    elif func_name == 'updateContinuesLoginDay':
        params = { 
                    'uid':'5889'
                 }
        res = eas_instance.invoke('activity/updateContinuesLoginDay',params)
        print res
    elif func_name == 'getContinuesLoginDays':
        params = { 
                   'uid':'6444' 
                 }
        res = eas_instance.invoke('activity/getContinuesLoginDays',params)
        print res
    elif func_name == 'getLotteryChances':
        params = {  
                      'uid':'4170' 
                 }
        res = eas_instance.invoke('activity/getLotteryChances',params)
        print res
    elif func_name == 'addConstantChances':
        params = { 
                      'uid':'6444' ,'chances':'8'
                 }
        res = eas_instance.invoke('activity/addConstantChances',params)
        print res
    elif func_name == 'costChance':
        params = { 
                      'uid':'6444'
                 }
        res = eas_instance.invoke('activity/costChance',params)
        print res
    elif func_name == 'lottery':
        params = { 
                      'uid':'6444'
                 }
        res = eas_instance.invoke('activity/lottery',params)
        print res
    elif func_name == 'addGoodsOrder':
        params = { 
                      'activity_id':'5188', 'uid':'6444', 'username':'holylee1088', 'gain_config':'aa', 'goods_id':'1', 'nums':'1', 'admin':'sys', 'adminnote':'sys'
                 }
        res = eas_instance.invoke('activity/addGoodsOrder',params)
        print res
    elif func_name == 'getConstantChances':
        params = { 
                      'uid':'6444'
                 }
        res = eas_instance.invoke('activity/getConstantChances',params)
        print res
    elif func_name == 'getGoodsOrder':
        params = { 
                      'start_time':'2012-11-26',  'end_time':'2012-12-23'
                 }
        res = eas_instance.invoke('activity/getGoodsOrder',params)
        print res
    elif func_name == 'changeGoodsOrderStatus':
        params = {  
                      'orderid':'2',  'status':'suc' 
                 }
        res = eas_instance.invoke('activity/changeGoodsOrderStatus',params)
        print res
    elif func_name == 'pageHandAward': 
        params = {  
                      'uid':'6144', 'activity_id':'666'
                 }
        res = eas_instance.invoke('activity/pageHandAward',params)
        print res
    elif func_name == 'getShowAward':
        params = { 
                      'activity_id':'5188', 'offset':'0', 'nums':'8'
                 }
        res = eas_instance.invoke('activity/getShowAward',params)
        print res
    elif func_name == 'addInviteRelation':
        params = {
                     'inviter':'esun_test889','invitee':'test_6666' 
                 } 
        res = eas_instance.invoke('activity/addInviteRelation',params)
        print res
    elif func_name == 'getInviteTimes':
        params = {
                     'openid':'holylee1088', 'pf':'asdfsdf','openkey':'asdfe'
                 }
        res = eas_instance.invoke('activity/getInviteTimes',params)
        print res
    elif func_name == 'getHandsConfig':
        params = {
                     'hands_type':'gold'  
                 }     
        res = eas_instance.invoke('activity/getHandsConfig',params)
        print res 
    elif func_name == 'addPropsCard':
        params = {
                    'uid':'6444', 'activity_id':'52', 'card_id':'G0001#1338876744020000SITANDGO1435_0000000049_5_S', 'nums':'5'
                 }
        res = eas_instance.invoke('activity/addPropsCard',params)
        print res
    elif func_name == 'getPropsCard':
        params = {
                    'uid':'6444', 'activity_id':'52'
                 }
        res = eas_instance.invoke('activity/getPropsCard',params)
        print res 
    elif func_name == 'buyPropsCard':
        params = {
                    'uid':'6444', 'activity_id':'52', 'card_id':'2_S', 'nums':'5'
                 }
        res = eas_instance.invoke('activity/buyPropsCard',params)
        print res
    elif func_name == 'prizePropsCard':
        params = {
                    'uid':'6444', 'activity_id':'52', 'prize_type':'CHRISTMAS_FLUSH_PRIZE', 'card_ids':'2_S,5_S,Q_S'
                 }
        res = eas_instance.invoke('activity/prizePropsCard',params)
        print res
    elif func_name == 'activityNotice':
        #'uid':'6444', 'notice_type':'49', 'reward_num':'1000'
        params = { 
                     'uid':'6444', 'notice_type':'exchage', 'reward_num':'1000','cost_num':'10'
                 }
        res = eas_instance.invoke('texasAcct/activityNotice',params)
        print res
    elif func_name == 'gamePropsGain':
        #'uid':'6444', 'notice_type':'49', 'reward_num':'1000'
        params = { 
                       'orderid':'201301160001',      'userid':'6444',       'username':'holylee1088',
                       'acct_type':'GOLD',          'transmoney':'120', 'channel':'ACTIVITY',
                       'content':'活动派奖',                'admin':'SYS',           'adminnote':'SYS'  
                 }
        res = eas_instance.invoke('texasAcct/gamePropsGain',params)
        print res
    elif func_name == 'deductForActivity':
        #'uid':'6444', 'notice_type':'49', 'reward_num':'1000'
        params = { 
                       'orderid':'201301160002',      'userid':'6444',       'username':'holylee1088',
                       'acct_type':'SILVER',          'transmoney':'9000000', 'channel':'ACTIVITY',
                       'content':'活动扣款',                'admin':'SYS',           'adminnote':'SYS'  
                 }
        res = eas_instance.invoke('texasAcct/deductForActivity',params)
        print res
    elif func_name == 'addNotice':
        params = {
                    'userid':'6444', 'template':'28', 'content':'8', 'notice_type':'CHARGING'
                 }
        res = eas_instance.invoke('texasAcct/addNotice',params)
        print res 
    elif func_name == 'addAdminPrize':
        params = {
                    'uid':'3341', 'platform_id':'esun_test61', 'platform':'DEBAO', 'transmoney':'10','admin':'wangfz','adminnote':'test','send_flag':'0','send_msg':''
                 }
        res = eas_instance.invoke('texasAcct/addAdminPrize',params)
        print res 
    elif func_name == 'reviewAdminPrize':
        params = {
                    'orderid':'5', 'reviewer':''
                 }
        res = eas_instance.invoke('texasAcct/reviewAdminPrize',params)
        print res 
    elif func_name == 'getAdminPrizeNum':
        params = {
                   
                 }
        res = eas_instance.invoke('texasAcct/getAdminPrizeNum',params)
        print res 
    elif func_name == 'getAdminPrizeList':
        params = {
                    'offset':'1', 'limit':'2'
                 }
        res = eas_instance.invoke('texasAcct/getAdminPrizeList',params)
        print res 
    elif func_name == 'getAdminPrizeList1':
        params = {
                    'offset':'1', 'limit':'2','uid' : '', 'min_time':'2013-08-12','max_time': '2013-08-15','admin': 'wangfz', 'is_rewarded' : '1'
                 }
        res = eas_instance.invoke('texasAcct/getAdminPrizeList',params)
        print res 
    elif func_name == 'activityPrize':
        params = {
                    'userid':'10838', 'chargingid':'20120720018009'
                 }
        res = eas_instance.invoke('texasAcct/activityPrize',params)
        print res 

#activityPrize( self, userid, chargingid, content='非首次充值活动派奖', admin='SYS', adminnote='SYS')        
        
    # offset,limit ,uid = "", min_time= "",max_time= "",admin = "", is_rewarded = "")