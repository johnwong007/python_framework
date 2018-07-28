#coding=gbk
"""给数据分片做数据路由的小工具

使用示例1：
    from DataRoute import DataRing
    dr = DataRing({
        'node01': res01, # res01可以是任意东西
        'node02': res02, # res02可以是任意东西
    })
    res = dr.get_node('mykey') # 返回根据一致性哈希其中一个res

使用示例2：
    import DataRoute
    nodes = {
        'node01': res01, # res01可以是任意东西
        'node02': res02, # res02可以是任意东西
    }
    DataRoute.set_resource('res_name', DataRing(nodes))
    DataRoute.get_node('res_name', 'mykey') # 返回根据一致性哈希其中一个res

使用示例3：
    假设有文件project.xml
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
    代码：
        XmlConfig.loadFile('project.xml')
        DataRoute.load_from_xmlconfig('/project_show/data_route/showinfo/')
        DataRoute.load_from_xmlconfig('/project_show/data_route/userinfo/')
        print DataRoute.get_node('showinfo', 'mykey')
        print DataRoute.get_node('userinfo', 'mykey')

使用示例4：
    import DataRoute
    ap = DataRoute.AliquotPart('asdf_', 10, 2, 3)
    print ap.get_node(1)
    print ap.get_node(11)
    print ap.get_node(22)

使用示例5：
    import DataRoute
    md = DataRoute.Modulo('asdf_', 3)
    print md.get_node(1)
    print md.get_node(2)
    print md.get_node('3')
    print md.get_node('4')
"""

from hash_ring import HashRing

# 全局数据路由
DATA_ROUTES = {
}


############################################################


class DataRing:
    """用一致性哈希实现的路由"""

    def __init__(self, nodes):
        """构造函数
            nodes    节点数据，格式：{'node01': resource01, 'node02': resource02}
        """
        self._nodes = nodes
        ids = nodes.keys()
        ids.sort()
        self._ring = HashRing(ids)

    def get_node(self, key):
        """取得节点对应资源数据
        """
        return self._nodes[self._ring.get_node(str(key))]

    def get_nodes_list(self):
        """返回所有节点对应资源数据
        """
        return self._nodes.values()


class AliquotPart:
    """用整除实现的路由"""

    def __init__(self, prefix, divisor, subfix_len=1, start_with=0):
        """构造函数
           prefix   前缀
           divisor  除数
           subfix_len   后缀长度
           start_with   从什么数字开始
        """
        self._prefix = prefix
        self._divisor = abs(int(divisor))
        self._start_with = abs(int(start_with))
        self._node_format = self._prefix + '%0' + \
                            str(abs(int(subfix_len))) + 'd'

    def get_node(self, key):
        """取得节点对应资源数据
        """
        id = abs(int(key)) / self._divisor + self._start_with
        return self._node_format % int(id)


class Modulo:
    """用余数（取模）实现的路由"""

    def __init__(self, prefix, mod, subfix_len=1):
        """构造函数
            prefix   前缀
            mod      模的值
            subfix_len   后缀长度
        """
        self._prefix = prefix
        self._mod = abs(int(mod))
        self._node_format = self._prefix + '%0' + \
                            str(abs(int(subfix_len))) + 'd'

    def get_node(self, key):
        """取得节点对应资源数据
        """
        id = abs(int(key)) % self._mod
        return self._node_format % id


class Division:
    """用除法实现的路由"""

    def __init__(self, nodes, key_field, divisor, start_with=0):
        """构造函数
            nodes    节点数据，格式：{'node01': {}, 'node02': {}}或者[{},{}]
            key_filed    需要格式化的节点
            divisor  除数
            start_with   从什么数字开始
        """
        if type(nodes) is list:
            self._nodes = nodes
        else:
            self._nodes = [nodes[i] for i in sorted(nodes.keys())]
        self._key_field = key_field
        self._divisor = abs(int(divisor))
        self._start_with = abs(int(start_with))

    def get_node(self, key):
        """取得节点对应资源数据
        """
        id = abs(int(key)) // self._divisor + self._start_with
        data = self._nodes[id % len(self._nodes)].copy()
        data[self._key_field] = data[self._key_field] % id
        return data

        
############################################################


def set_resource(res_name, route_obj):
    """设置资源节点
    """
    DATA_ROUTES[res_name] = route_obj


def load_from_xmlconfig(xpath, route_class=DataRing, *args, **kwargs):
    """从XmlConfig加载资源
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
    """根据资源关键值获取所在节点资源
    """
    return DATA_ROUTES[res_name].get_node(key)

