#coding=gbk
"""ICE(zeroc)小工具
"""
import Ice


def initAppData(xcfg=None, props=None):
    """初始化一个ICE的应用数据类
        xcfg    XmlConfig配置的路径（可选）
        props   额外指定的属性（可选）
    """
    data = Ice.InitializationData()
    data.properties = Ice.createProperties()
    if xcfg:
        import XmlConfig
        if xcfg[-1:] != '/':
            xcfg += '/'
        for k, v in XmlConfig.list(xcfg).items():
            data.properties.setProperty(k, v)
    if props:
        for k, v in props.items():
            data.properties.setProperty(k, v)
    return data

