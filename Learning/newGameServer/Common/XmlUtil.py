#coding=gbk
import re
from xml.dom import minidom


def parseString(s):
    if s[:5] == '<?xml':
        ss = s.split('?>', 1)
        m = re.search(r'encoding=\W([\w\-]+)\W', ss[0])
        if m:
            s = ss[1].decode(m.group(1)).encode('utf8')
        else:
            s = ss[1]
    return minidom.parseString(s)


def parseFile(fname):
    f = open(fname, 'r')
    s = f.read()
    f.close()
    return parseString(s)


def parseToDict(s, encoding='utf8'):
    dom = parseString(s)
    data = domToDict(dom, encoding)
    dom.unlink()
    return data


def domToDict(node, encoding='utf8', data=None):
    if data == None:
        data = {}
    if node.nodeType == node.DOCUMENT_NODE:
        domToDict(node.firstChild, encoding, data)
        return data
    d = {}
    if node.hasChildNodes():
        for i in node.childNodes:
            if i.nodeType == i.TEXT_NODE:
                if d.has_key('<text>'):
                    d['<text>'] += i.nodeValue.encode(encoding)
                else:
                    d['<text>'] = i.nodeValue.encode(encoding)
            elif i.nodeType == i.ELEMENT_NODE:
                domToDict(i, encoding, d)
    if node.hasAttributes():
        d['<attrs>'] = dict([(i[0].encode(encoding), i[1].encode(encoding))
                                for i in node.attributes.items()])
    data[node.nodeName.encode(encoding)] = d

