from PyQt6.QtWidgets import (
    QApplication, QDialog, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import QUrl
from PyQt6.QtWebSockets import QWebSocket
import sys
from pyqt6_ui import Ui_Form
import ctypes
import tornado.web
from threading import Thread
import socket
import requests
import time
import json
from websocket import SocketThread,OutputPower

class Password(Ui_Form,QDialog):
    clib = ctypes.CDLL("64/CardEncoder.dll")
    hotelInfo = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #uic.loadUi('./index.ui',self)
        self.show()
           
        self.connect.clicked.connect(self.connectComm)
        self.onconnect.clicked.connect(self.unConnectComm)
        
        self.getHotelInfo.clicked.connect(self.getHotel)
        self.addCard.clicked.connect(self.addIcCard)
        self.readCard.clicked.connect(self.readIcCard)
        self.clearCard.clicked.connect(self.clearIcCard)

        #写入酒店专用卡
        self.writeHotelCard.clicked.connect(self.writeHotelIcCard)
        #制作空白卡
        self.emptyCard.clicked.connect(self.emptyIcCard)
        self.startSocket.clicked.connect(self.startSockets)
    def startSockets(self):
        #启动socket  获取酒店hotel 连接发卡器
        self.getHotel()
        self.connectComm()
        port =  self.socketPort.text()
        self.textLog.append(f"启动socket:{port}")
        # 创建socket应用服务
        self.socket_thread = SocketThread("127.0.0.1", 10000)
        self.socket_thread.data_received.connect(self.handle_data_received)
        self.socket_thread.start()
    def handle_data_received(self,msg):
        jsonMsg = {}
        res  = ""
        try:
            jsonMsg = json.loads(msg)
        except ValueError:
            self.textLog.append(f"{msg}") 
        
        if jsonMsg.get("action") == "writeCard":
            buildNumber = int(jsonMsg.get("buildNumber"))
            floor = int(jsonMsg.get("floor"))
            mac = jsonMsg.get("mac").encode()
            endtime = int(jsonMsg.get("endtime"))
            res = self.clib.CE_WriteCard(self.hotelInfo.encode(),buildNumber,floor,mac,endtime,True)  
            self.textLog.append(f"{res}") 
        elif  jsonMsg.get("action") == "emptyCard":
            self.clearIcCard()
        elif jsonMsg.get("action") == "readCard":    
            self.readIcCard()    
        elif jsonMsg.get("action") == "readCard":    
            self.writeHotelIcCard()
        self.socket_sethread = OutputPower()    
        self.socket_sethread.finished.connect(lambda:print("调用子进程 发送消息"))
        self.socket_sethread.start()
    def connectComm(self):
        port_name = self.cardPort.text()  # 串口名称
        re =self.clib.CE_ConnectComm(port_name.encode())
        if re==0:
            print(f"发卡器已经连接{re}")
            self.textLog.append(f"连接成功{re}")
            #配置发卡器
            #config = self.clib.CE_InitCardEncoder(self.hotelInfo)
            source  = "11111111111000000".encode()
            san=self.clib.CE_SetSectors(source)
            print("san",san)
        if re ==1:
            print(f"连接失败{re}")  
            self.textLog.append(f"连接失败{re}")   
    def unConnectComm(self):
        re = self.clib.CE_DisconnectComm()
        if re==0:
            print(f"断开成功{re}")
            self.textLog.append(f"发卡器断开成功{re}")
        else:
            print(f"断开失败{re}")    
            self.textLog.append(f"发卡器断开失败{re}")        
    def getHotel(self):
        url = "https://cnapi.ttlock.com/v3/hotel/getInfo"
        data = {
            "clientId": self.appid.text(),
            "clientSecret": self.secrets.text(),
            "date": int(time.time()) * 1000,
        }
        response = requests.post(url, params=data).text
        try:
            data = json.loads(response)
            self.hotelInfo = data['hotelInfo']
        except Exception as e :    
            self.textLog.append(f"json解析失败")
        self.textLog.append(f"获取hotelInfo: {data['hotelInfo']}")
    def addIcCard(self):
        buildNumber =  int(self.building.text())
        floor = int(self.floor.text())
        mac  = self.doorMac.text().encode()
        time  = self.time.text()
        hotelInfo = self.hotelInfo.encode()
        allowLockOut = True
        res = self.clib.CE_WriteCard(hotelInfo,buildNumber,floor,mac,time,allowLockOut)  
        if res==0:
            self.textLog.append(f"写入数据成功{res}")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("数据写入失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"写入数据失败,错误码:{res}")         
    def readIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        hotel_array_ptr = ctypes.c_char_p()
        
        res = self.clib.CE_ReadCard(hotelInfo,ctypes.byref(hotel_array_ptr))
        if res==0:
            #获取字符串数组
            try:
                self.textLog.append(f"读取数据成功{hotel_array_ptr.value.decode()}")
            except:
                print("读取数据错误")  
           
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("读取失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"读取数据失败,错误码:{res}")    
    def clearIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_ClearCard(hotelInfo)
        if res==0:
            self.textLog.append("ic卡清空成功")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("操作失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}") 
    def writeHotelIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_InitCard(hotelInfo) 
        if res==0:
            self.textLog.append("ic卡酒店专用卡成功")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}") 
    def emptyIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_DeInitCard(hotelInfo) 
        if res==0:
            self.textLog.append("恢复空白Ic卡成功")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}")         
        
                       
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    password = Password()
    app.exit(app.exec())
