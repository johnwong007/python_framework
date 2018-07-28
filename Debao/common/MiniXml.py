#encoding=gbk
'''
xml简介简单解析版
使用方法：
res = '<t><a><b x="1" xx="2" /><b x="1" /></a><k><c x="1" xx="2"/><d hh="xxx"></d><e /></k></t>'
ixml = MiniXml.parseString(res)
print ixml.get('/t/a/b') #[{'x': '1', 'xx': '2'}, {'x': '1'}]
print ixml.list('/t/k/') #{'c': {'x': '1', 'xx': '2'}, 'e': '', 'd': {'hh': 'xxx'}}
'''

import re
import hashlib
from xml.dom import minidom

_DATA_BASE_ = {}

class MiniXml:
    
    def __init__(self):
        self._dom_ = None
        self._data_ = None
    
    def parseXml(self):
        '''解析dom对象'''
        d = self.domToDict(self._dom_, self.encoding, None)
        self._data_ = self.loadData(d, '', None)
    
    def loadFile(self, fname):
        '''加载xml文件'''
        f = open(fname, 'r')
        s = f.read()
        f.close()
        self.loadString(s)
        return self
    
    def loadString(self, string):
        '''加载xml源'''
        if string[:5] == '<?xml':
            ss = string.split('?>', 1)
            m = re.search(r'encoding=\W([\w\-]+)\W', ss[0])
            if m:
                self.encoding = m.group(1)
                string = ss[1].decode(m.group(1)).encode('utf8')
            else:
                self.encoding = 'utf8'
                string = ss[1]
        self._dom_ = minidom.parseString(string)
        return self
    
    def domToDict(self, node, encoding='utf8', data=None):
        '''将dom转换成字典格式'''
        if data == None:
            data = {}
        if node.nodeType == node.DOCUMENT_NODE:
            self.domToDict(node.firstChild, encoding, data)
            return data
        d = {}
        if node.hasChildNodes():
            for i in node.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    t = i.nodeValue.encode(encoding)
                    if not t.strip():#去除空白字符
                        continue
                    
                    if d.has_key('<text>'):
                        d['<text>'] += t
                    else:
                        d['<text>'] = t
                elif i.nodeType == i.ELEMENT_NODE:
                    self.domToDict(i, encoding, d)
        
        if node.hasAttributes():
            d['<attrs>'] = dict([(i[0].encode(encoding), i[1].encode(encoding))
                                    for i in node.attributes.items()])
        
        if not node.hasAttributes() and not node.hasChildNodes():
            d['<text>'] = ''
        
        key = node.nodeName.encode(encoding)
        if data.has_key(key):
            if type(data[key]) != list:
                data[key] = [data[key]]
            data[key].append(d)
        else:
            data[key] = d
    
    def loadData(self, d, p, data=None):
        '''格式化字典中的数据'''
        if data == None:
            data = {}
        
        if type(d) == list:
            for dd in d:
                if type(dd) == dict:
                    self.loadData(dd, p, data)
            return None
        
        cs = []
        if d.has_key('<text>'):
            cs.append(d.pop('<text>').strip())
        
        if d.has_key('<attrs>'):
            cs.append(d.pop('<attrs>'))
        
        for c in cs:
            if data.has_key(p):
                if type(data[p]) != list:
                    data[p] = [data[p]]
                data[p].append(c)
            else:
                data[p] = c
        
        for k, v in d.items():
            self.loadData(v, p + '/' + k, data)
        
        return data
        
    
    def get(self, path, df=None):
        '''根据路径访问dom对象'''
        return self._data_.get(path, df)
    
    def list(self, path):
        '''根据路径列出对象中的元素'''
        pos = len(path)
        return dict([(i[pos:], self._data_[i]) for i in self._data_ if i.find(path) == 0])

    def end(self):
        '''关闭dom对象'''
        self._dom_.unlink()

    
def hashKey(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()
    

def _get(name):
    global _DATA_BASE_
    k = hashKey(name)
    if _DATA_BASE_.has_key(k):
        return _DATA_BASE_[k]
    return None

def _set(name, instance):
    global _DATA_BASE_
    k = hashKey(name)
    _DATA_BASE_[k] = instance
    return instance
    
def parseFile(fname):
    _i = _get(fname)
    if not _i:
        _i = MiniXml()
        _i.loadFile(fname).parseXml()
        _i.end()
        _set(fname, _i)
    return _i

def parseString(string):
    _i = _get(string)
    if not _i:
        _i = MiniXml()
        _i.loadString(string).parseXml()
        _i.end()
        _set(string, _i)
    return _i


    
