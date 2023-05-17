import sys
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import socket
import asyncio
import websockets
import json
import threading

Clients = []
class OutputPower():
    finished = pyqtSignal()
    async def run(self,arg,s,websocket):
        # 发送消息方法，单独和请求的客户端发消息
        await s('接收socket', websocket)
        # 群发消息
        await s('----------')
class SocketThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
    	# 发消息给客户端的回调函数
    async def s(self,msg,websocket=None):
        await self.sendMsg(msg,websocket)
    # 针对不同的信息进行请求，可以考虑json文本
    async def runCase(self,jsonMsg,websocket):  
        # await OutputPower(jsonMsg,self.s,websocket)
        op = OutputPower()
        await op.run(jsonMsg,self.s,websocket)

    # 每一个客户端链接上来就会进一个循环
    async def echo(self,websocket, path):
        Clients.append(websocket)
        await websocket.send(json.dumps({"type": "handshake"}))

        while True:
            try:
                recv_text = await websocket.recv()
                message = "收到消息: {}".format(recv_text)
                # 直接返回客户端收到的信息
                await websocket.send(message)
                
                #返回主线程
                self.data_received.emit(recv_text)   
                # 分析当前的消息 json格式，跳进功能模块分析
                await self.runCase(jsonMsg='',websocket=websocket)

            except websockets.ConnectionClosed:
                print("ConnectionClosed...", path)  # 链接断开
                Clients.remove(websocket)
                break
            except websockets.InvalidState:
                print("InvalidState...")  # 无效状态
                Clients.remove(websocket)
                break
            except Exception as e:
                print(e)
                Clients.remove(websocket)
                break

    # 发送消息
    async def sendMsg(self,msg,websocket):
        print('sendMsg:',msg)
        if websocket != None:
            await websocket.send(msg)
        else:
            await self.broadcastMsg(msg)
        # 避免被卡线程
        await asyncio.sleep(0.2)

	# 群发消息
    async def broadcastMsg(self,msg):
        for user in Clients:
            await user.send(msg)

    # 启动服务器
    async def runServer(self):
        async with websockets.serve(self.echo, self.host, self.port):
            await asyncio.Future()  # run forever    
	# 多线程模式，防止阻塞主线程无法做其他事情
    def WebSocketServer(self):
        asyncio.run(self.runServer())

    def run(self):
        # 多线程启动，否则会堵塞
        thread = threading.Thread(target=self.WebSocketServer)
        thread.start()
        thread.join()
        print("go!!!")
