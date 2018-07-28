#coding=gbk
''' XML配置管理工具
*）使用示例：
    假设有个asdf.xml文件，内容
    <a>
        <b>bb</b>
        <c c1="cc" c2="ccc"/>
    </a>
    测试代码：
    XmlConfig.loadFile('asdf.xml')
    print XmlConfig.get('/a/b')
    print XmlConfig.get('/a/c')
    print XmlConfig.list('/a/') # 注意"a"后面的"/"
'''


import XmlUtil


_DATAS_ = {}
_ENCODING_ = 'utf8'


def setEncoding(enc):
    global _ENCODING_
    _ENCODING_ = enc


def get(path, df=None):
    return _DATAS_.get(path, df)


def list(path):
    pos = len(path)
    return dict([(i[pos:], _DATAS_[i]) for i in _DATAS_ if i.find(path) == 0])


def loadData_(d, p):
    if d.has_key('<text>'):
        _DATAS_[p] = d.pop('<text>').strip()
    if d.has_key('<attrs>'):
        _DATAS_[p] = d.pop('<attrs>')
    for k, v in d.items():
        loadData_(v, p + '/' + k)


def loadFile(fname):
    global _ENCODING_
    dom = XmlUtil.parseFile(fname)
    data = XmlUtil.domToDict(dom, _ENCODING_)
    dom.unlink()
    loadData_(data, '')

