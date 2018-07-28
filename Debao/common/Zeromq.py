#coding=gbk
import threading
import XmlConfig
import zmq
import errno

_ZMQ_LOCK_ = threading.RLock() # 锁保护
_ZMQ_POOL_ = {}# 连接池
class Zeromq:
    def __init__(self):
        self.zmq_context = None
        self.zmq = None
        self.is_read_block = None
        self.is_write_block= None
        self.zmq_id = None

    def connect(self, zmq_id):
        self.zmq_id = zmq_id

        if "" == _ZMQ_POOL_.get(zmq_id, ""):
            conf = XmlConfig.get('/resource/msgQue/zmq/' + zmq_id)
            if conf == None:
                print "没有%s相关的配置"%zmq_id
                return  
            conn_str = conf.get("connection")
            module = int(conf.get("module"))
            self.receivce_block = int(conf.get("recvice_block", 0))
            self.zmq_context = zmq.Context()
            self.zmq = self.zmq_context.socket(module)  
            self.zmq.connect(conn_str)
            _ZMQ_POOL_[zmq_id] = self
            
        else:
            self.zmq = _ZMQ_POOL_.get(zmq_id)
            
    def bind(self, zmq_id):
        self.zmq_id = zmq_id

        if "" == _ZMQ_POOL_.get(zmq_id, ""):
            conf = XmlConfig.get('/resource/msgQue/zmq/' + zmq_id)
            if conf == None:
                print "没有%s相关的配置"%zmq_id
                return  
            conn_str = conf.get("connection")
            module = int(conf.get("module"))
            self.receivce_block = int(conf.get("recvice_block", 0))
            self.zmq_context = zmq.Context()
            self.zmq = self.zmq_context.socket(module)    
            self.zmq.bind(conn_str)
            _ZMQ_POOL_[zmq_id] = self            
        else:
            self.zmq = _ZMQ_POOL_.get(zmq_id)
 
    def receivce(self):
        try:
            print self.receivce_block
            msg = self.zmq.recv(self.receivce_block)
            return msg
        except zmq.ZMQError, err:
            if err.errno == errno.EAGAIN:
                return None
            else:
                raise Exception("receive from connect server failed, because %s" % err)

    def send(self, msg):
        try:
            self.zmq.send(msg)
        except zmq.ZMQError, err:
            print "Error: send to connect server failed, because %s" % err


