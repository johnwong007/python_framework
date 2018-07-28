#coding=gbk
"""�����ݷ�Ƭ������·�ɵ�С����

ʹ��ʾ��1��
    from DataRoute import DataRing
    dr = DataRing({
        'node01': res01, # res01���������ⶫ��
        'node02': res02, # res02���������ⶫ��
    })
    res = dr.get_node('mykey') # ���ظ���һ���Թ�ϣ����һ��res

ʹ��ʾ��2��
    import DataRoute
    nodes = {
        'node01': res01, # res01���������ⶫ��
        'node02': res02, # res02���������ⶫ��
    }
    DataRoute.set_resource('res_name', DataRing(nodes))
    DataRoute.get_node('res_name', 'mykey') # ���ظ���һ���Թ�ϣ����һ��res

ʹ��ʾ��3��
    �������ļ�project.xml
        <?xml version="1.0" encoding="utf-8"?>
        <project_show>
            <data_route>
                <userinfo>
                    <node01 dbtype="mysql" dbid="projshow" table="t_userinfo_01" />
                </userinfo>
                <showinfo>
                    <node01 dbtype="mysql" dbid="projshow" table="t_showinfo_01" />
                    <node02 dbtype="mysql" dbid="projshow" table="t_showinfo_02" />
                </showinfo>
            </data_route>
        </project_show>
    ���룺
        XmlConfig.loadFile('project.xml')
        DataRoute.load_from_xmlconfig('/project_show/data_route/showinfo/')
        DataRoute.load_from_xmlconfig('/project_show/data_route/userinfo/')
        print DataRoute.get_node('showinfo', 'mykey')
        print DataRoute.get_node('userinfo', 'mykey')

ʹ��ʾ��4��
    import DataRoute
    ap = DataRoute.AliquotPart('asdf_', 10, 2, 3)
    print ap.get_node(1)
    print ap.get_node(11)
    print ap.get_node(22)

ʹ��ʾ��5��
    import DataRoute
    md = DataRoute.Modulo('asdf_', 3)
    print md.get_node(1)
    print md.get_node(2)
    print md.get_node('3')
    print md.get_node('4')
"""

from hash_ring import HashRing

# ȫ������·��
DATA_ROUTES = {
}


############################################################


class DataRing:
    """��һ���Թ�ϣʵ�ֵ�·��"""

    def __init__(self, nodes):
        """���캯��
            nodes    �ڵ����ݣ���ʽ��{'node01': resource01, 'node02': resource02}
        """
        self._nodes = nodes
        ids = nodes.keys()
        ids.sort()
        self._ring = HashRing(ids)

    def get_node(self, key):
        """ȡ�ýڵ��Ӧ��Դ����
        """
        return self._nodes[self._ring.get_node(str(key))]

    def get_nodes_list(self):
        """�������нڵ��Ӧ��Դ����
        """
        return self._nodes.values()


class AliquotPart:
    """������ʵ�ֵ�·��"""

    def __init__(self, prefix, divisor, subfix_len=1, start_with=0):
        """���캯��
           prefix   ǰ׺
           divisor  ����
           subfix_len   ��׺����
           start_with   ��ʲô���ֿ�ʼ
        """
        self._prefix = prefix
        self._divisor = abs(int(divisor))
        self._start_with = abs(int(start_with))
        self._node_format = self._prefix + '%0' + \
                            str(abs(int(subfix_len))) + 'd'

    def get_node(self, key):
        """ȡ�ýڵ��Ӧ��Դ����
        """
        id = abs(int(key)) / self._divisor + self._start_with
        return self._node_format % int(id)


class Modulo:
    """��������ȡģ��ʵ�ֵ�·��"""

    def __init__(self, prefix, mod, subfix_len=1):
        """���캯��
            prefix   ǰ׺
            mod      ģ��ֵ
            subfix_len   ��׺����
        """
        self._prefix = prefix
        self._mod = abs(int(mod))
        self._node_format = self._prefix + '%0' + \
                            str(abs(int(subfix_len))) + 'd'

    def get_node(self, key):
        """ȡ�ýڵ��Ӧ��Դ����
        """
        id = abs(int(key)) % self._mod
        return self._node_format % id


class Division:
    """�ó���ʵ�ֵ�·��"""

    def __init__(self, nodes, key_field, divisor, start_with=0):
        """���캯��
            nodes    �ڵ����ݣ���ʽ��{'node01': {}, 'node02': {}}����[{},{}]
            key_filed    ��Ҫ��ʽ���Ľڵ�
            divisor  ����
            start_with   ��ʲô���ֿ�ʼ
        """
        if type(nodes) is list:
            self._nodes = nodes
        else:
            self._nodes = [nodes[i] for i in sorted(nodes.keys())]
        self._key_field = key_field
        self._divisor = abs(int(divisor))
        self._start_with = abs(int(start_with))

    def get_node(self, key):
        """ȡ�ýڵ��Ӧ��Դ����
        """
        id = abs(int(key)) // self._divisor + self._start_with
        data = self._nodes[id % len(self._nodes)].copy()
        data[self._key_field] = data[self._key_field] % id
        return data

        
############################################################


def set_resource(res_name, route_obj):
    """������Դ�ڵ�
    """
    DATA_ROUTES[res_name] = route_obj


def load_from_xmlconfig(xpath, route_class=DataRing, *args, **kwargs):
    """��XmlConfig������Դ
    """
    import XmlConfig
    if xpath[-1:] != '/':
        xpath += '/'
    res_name = xpath.split('/')[-2]
    if DATA_ROUTES.has_key(res_name):
        return 0
    nodes = XmlConfig.list(xpath)
    if not nodes:
        return -1
    set_resource(res_name, route_class(nodes, *args, **kwargs))
    return 1


def get_node(res_name, key):
    """������Դ�ؼ�ֵ��ȡ���ڽڵ���Դ
    """
    return DATA_ROUTES[res_name].get_node(key)

