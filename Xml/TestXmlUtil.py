import XmlConfig
XmlConfig.loadFile("./poker_game.xml" )
watcher_group_name  = XmlConfig.get("/xml/Watcher_name/group_name")["value"]
watcher_server_name = XmlConfig.get("/xml/Watcher_name/server_name")["value"]
print(watcher_group_name)
print(watcher_server_name)