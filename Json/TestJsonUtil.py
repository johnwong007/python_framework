#coding:utf8

import JsonUtil as Json

if __name__=='__main__':
	msg = "{'code':'1'}"
	pack = Json.read(msg)
	print(type(pack))
	print(type(Json.write(pack)))

