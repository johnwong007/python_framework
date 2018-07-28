#coding=gbk
"""ICE(zeroc)С����
"""
import Ice


def initAppData(xcfg=None, props=None):
    """��ʼ��һ��ICE��Ӧ��������
        xcfg    XmlConfig���õ�·������ѡ��
        props   ����ָ�������ԣ���ѡ��
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

