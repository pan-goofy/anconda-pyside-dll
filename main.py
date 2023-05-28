import sys
from pyqt6_ui import Ui_Form
import ctypes
from threading import Thread
import requests
import time
import socket
from PyQt6.QtCore import QThread, pyqtSignal,pyqtSlot,Qt,QCoreApplication
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox
import json
import configparser
import asyncio
from socketServerMain import SocketThread,OutputPower
from errorMsg import getMsg
from httpclient import Worker
import image_rc

class Password(Ui_Form,QDialog):
    clib = ctypes.CDLL("./64/CardEncoder.dll")
    #读取配置
    cf = configparser.ConfigParser()
    cf.read('./config.ini', encoding='utf-8')
    cf_cardPort = cf.get("Sections","cardPort")
    cf_appid = cf.get("Sections","appid")
    cf_secrets = cf.get("Sections","secrets")
    cf_socketPort = cf.get("Sections",'socketPort')
    cf_socketIp = cf.get("Sections",'socketIp')
    hotelInfo = ""
    icCards = ""
    sectors = ""
    isConnect  = True
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        #uic.loadUi('./index.ui',self)
        self.show()
        #加载配置文件
        _translate = QCoreApplication.translate
        print(self.cf_cardPort)
        self.cardPort.setText(_translate("Form", self.cf_cardPort))
        self.appid.setText(_translate("Form", self.cf_appid))
        self.secrets.setText(_translate("Form", self.cf_secrets))
        self.socketPort.setText(_translate("Form", self.cf_socketPort))
        self.socketIp.setText(_translate("Form", self.cf_socketIp))
        self.time.setText(_translate("Form", str(int(time.time())+86400)))

        #保存配置
        self.saveConfig.clicked.connect(self.saveSetting)
        #发卡器发声
        self.openSound.clicked.connect(self.startSound)
        #退出
        self.exitCard.clicked.connect(self.showDialog)
        self.minimizeCard.clicked.connect(self.showMinimized)
        self.connect.clicked.connect(self.connectComm)
        self.onconnect.clicked.connect(self.unConnectComm)
        
        self.getHotelInfo.clicked.connect(self.getHotel)
        self.addCard.clicked.connect(self.addIcCard)
        self.readCard.clicked.connect(self.readIcCard)
        self.clearCard.clicked.connect(self.clearIcCard)
        #配置发卡器
        self.setCard.clicked.connect(self.setCardHotel)

        #写入酒店专用卡
        self.writeHotelCard.clicked.connect(self.writeHotelIcCard)
        #制作空白卡
        self.emptyCard.clicked.connect(self.emptyIcCard)
        self.startSocket.clicked.connect(self.startSockets)

    def saveSetting(self):
        self.cf.set("Sections","cardPort", self.cardPort.text())  
        self.cf.set("Sections","appid", self.appid.text())  
        self.cf.set("Sections","secrets", self.secrets.text())  
        self.cf.set("Sections","socketPort", self.socketPort.text())  
        self.cf.set("Sections","socketIp", self.socketIp.text())  


        with open('config.ini', 'w') as f:
            self.cf.write(f)
        self.textLog.append(f"保存配置成功")
 
    def showDialog(self):
        try:
            reply = QMessageBox.question(self, '退出', '确定退出程序')
            reply = str(reply)
            if reply == 'StandardButton.Yes':
                 sys.exit()    
            else:
                return
        except Exception as e:
            print(e)
        print(reply)    
    def getSectors(self):
        sectors = ctypes.c_char_p()
        res = self.clib.CE_GetSectors(ctypes.byref(sectors))    
        if res ==0:
            self.sectors  = sectors.value
            self.textLog.append(f"获取扇区成功{sectors.value}")
        elif res ==16:
            self.textLog.append(f"发卡器未连接")   
        else:
            self.textLog.append(f"获取扇区失败")    
    def startSockets(self):
        #按钮禁止重复点击
        text = "启动"  if self.isConnect==False  else "断开"
        self.startSocket.setText(text)
        self.isConnect  = not self.isConnect
        #如果已经连接断开socket
        if self.isConnect:
            self.socket_thread.quit()
            #self.socket_thread.wait()
            asyncio.run(self.socket_thread.stopThread())
            print("线程关闭")
            self.textLog.append(f"断开socket连接")
            return
        #启动socket  获取酒店hotel 连接发卡器
        self.getHotel()
        self.connectComm()
        port =  self.socketPort.text()
        #ip = self.get_local_ip()
        ip = self.socketIp.text()
        self.textLog.append(f"启动socket:{ip}:{port}")
        # 创建socket应用服务
        self.socket_thread = SocketThread(ip, port)
        self.socket_thread.data_received.connect(self.handle_data_received)
        self.socket_thread.start()
    def handle_data_received(self,msg,websocket):
        jsonMsg = {}
        self.websocket = websocket
        print("websocket",websocket)
        res  = ""
        icCards = ""
        try:
            jsonMsg = json.loads(msg)
        except ValueError:
            self.textLog.append(f"{msg}") 
        
        if jsonMsg.get("action") == "writeCard":
            buildNumber = int(jsonMsg.get("buildNumber"))
            floor = int(jsonMsg.get("floor"))
            mac = jsonMsg.get("mac").encode()
            endtime = int(jsonMsg.get("endtime"))
            res = self.clib.CE_WriteCard(self.hotelInfo.encode(),buildNumber,floor,mac,endtime,False)  
            self.textLog.append(f"{res}") 
        elif  jsonMsg.get("action") == "clearCard":
            res =self.clearIcCard()
        elif jsonMsg.get("action") == "readCard":    
            res =self.readIcCard()    
            icCards  = json.loads(self.icCards)
        elif jsonMsg.get("action") == "initCard":    
            res =self.writeHotelIcCard()
        elif jsonMsg.get("action") == "emptyCard":    
            res =self.emptyIcCard()    
        elif jsonMsg.get("action") == "startSound":    
            length = int(jsonMsg.get("length"))
            interval = int(jsonMsg.get("interval"))
            number = int(jsonMsg.get("number"))
            res =self.startSound(length,interval,number)       
        elif jsonMsg.get("action") == "connectComm":    
            res =self.connectComm()        
        elif jsonMsg.get("action") == "unConnectComm":    
            res =self.unConnectComm()   
        elif jsonMsg.get("action") == "setCardHotel":    
            res =self.setCardHotel()     
        elif jsonMsg.get("action") == "getHotel":    
            res =self.getHotel()             
        print(res,"res")    
        if res !="":    
            data ={
                "status":res,
                "msg":getMsg().get(res),
                "list" :icCards,
                "type" : jsonMsg.get("action")
            } 
            asyncio.run(self.socket_thread.sendMsg(json.dumps(data),websocket))
            
    def startSound(self,length=1000,interval=100,number=2):
        length = 100 if length ==False else length
        re = self.clib.CE_Beep(length, interval, number)
        if re==0:
            self.textLog.append(f"发声成功{re},音长{length},间隔{interval},次数{number}")    
        elif re==16:      
            self.textLog.append(f"发卡器未连接{re}")    
        else:
            self.textLog.append(f"发声失败{re}") 
        return re     

        
          
    def connectComm(self):
        port_name = self.cardPort.text()  # 串口名称
        re =self.clib.CE_ConnectComm(port_name.encode())
        if re==0:
            print(f"发卡器已经连接{re}")
            self.textLog.append(f"连接成功{re}")
            self.getSectors()
            #source  = "11111111111000000".encode()
            san=self.clib.CE_SetSectors(self.sectors)
            print("san",san)
        if re ==1:
            print(f"连接失败{re}")  
            self.textLog.append(f"连接失败{re}")   
        return re    
    def setCardHotel(self):
        #配置发卡器
        print(self.hotelInfo)
        re = self.clib.CE_InitCardEncoder(self.hotelInfo.encode())  
        if re==0:
            self.textLog.append(f"配置发卡器成功{re}")    
        elif re==2:      
            self.textLog.append(f"配置发卡器失败{re}")    
        else:
            self.textLog.append(f"配置发卡器失败{re}")    
        return re    
            

    def unConnectComm(self):
        re = self.clib.CE_DisconnectComm()
        if re==0:
            print(f"断开成功{re}")
            self.textLog.append(f"发卡器断开成功{re}")
        else:
            print(f"断开失败{re}")    
            self.textLog.append(f"发卡器断开失败{re}") 
        return re          
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
        return 0
    def getHotel(self):
        self.textLog.append("获取hotelInfo中...")
        self.worker_thread = QThread()
        self.worker = Worker(self.appid.text(),self.secrets.text())
        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.result.connect(self.show_result)
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker_thread.start()  
    @pyqtSlot(str)
    def show_result(self, result):
        print("返回结果",result)
        self.hotelInfo =result
        self.textLog.append(result)      
    def addIcCard(self):
        buildNumber =  int(self.building.text())
        floor = int(self.floor.text())
        mac  = self.doorMac.text().encode()
        time  = self.time.text()
        hotelInfo = self.hotelInfo.encode()
        allowLockOut = False
        res = self.clib.CE_WriteCard(hotelInfo,buildNumber,floor,mac,int(time),allowLockOut)  
        if res==0:
            self.textLog.append(f"写入数据成功{res}")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("数据写入失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"写入数据失败,错误码:{res}")         
        return res    
    def readIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        
        hotel_array_ptr = ctypes.c_char_p()
        
        res = self.clib.CE_ReadCard(hotelInfo,ctypes.byref(hotel_array_ptr))
        if res==0:
            #获取字符串数组
            try:
                self.textLog.append(f"读取数据成功{hotel_array_ptr.value.decode()}")
                self.icCards = hotel_array_ptr.value
            except:
                print("读取数据错误")  
           
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("读取失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"读取数据失败,错误码:{res}")   
        return res     
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
        return res    
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
        return res    
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
        return res                
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    # def mousePressEvent(self, event):
    #     if event.button()==Qt.LeftButton:
    #     self.m_flag=True
    #     self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
    #     event.accept()
    #     self.setCursor(QCursor(Qt.OpenHandCursor)) #更改鼠标图标
    
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #     self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
    #     QMouseEvent.accept()
    
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag=False
    #     self.setCursor(QCursor(Qt.ArrowCursor))

                       
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    password = Password()
    app.exit(app.exec())
