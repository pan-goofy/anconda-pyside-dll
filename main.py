import sys
from pyqt6_ui import Ui_Form
import ctypes
from threading import Thread
import requests
import time
import socket
from PyQt6.QtCore import QThread, pyqtSignal,pyqtSlot,Qt,QCoreApplication,QPoint,QMimeData,QSharedMemory
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox,QMainWindow,QSystemTrayIcon,QMenu
import json
import configparser
from PyQt6.QtGui import QDrag,QCursor,QAction,QIcon
import asyncio
from socketServerMain import SocketThread,OutputPower
from errorMsg import getMsg
from httpclient import Worker
import image_rc
# 日志模块
import logging
import traceback
import datetime

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
    icNumber = ""
    sectors = ""
    isConnect  = True
    def __init__(self):
        super().__init__()
              # 检查是否已经有一个实例运行
        app_id = "my_app_identifier"
        self.shared_memory = QSharedMemory(app_id)
        if not self.shared_memory.create(1):
            QMessageBox.critical(None, "Error", "发卡器已经运行.")
            sys.exit()

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        #窗口置顶
        #Sself.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
    
     # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('Icon.ico'))
        

        # 创建托盘菜单
        self.tray_menu = QMenu(self)
        self.show_action = QAction("显示窗口", self)
        self.quit_action = QAction("退出", self)
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.quit_action)
       

        # 将托盘菜单设置为系统托盘图标的菜单
        self.tray_icon.setContextMenu(self.tray_menu)

        # 将系统托盘图标显示出来
        self.tray_icon.show()

        # 将“显示窗口”菜单项连接到槽函数
        self.show_action.triggered.connect(self.showNormal)
        self.quit_action.triggered.connect(app.quit)

        # 将窗口最小化时隐藏窗口并显示系统托盘图标
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.Tool)
        self.tray_icon.activated.connect(self.trayClick)
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
        #最小化
        self.minimizeCard.clicked.connect(self.showMinimized)
        #self.minimizeCard.clicked.connect(self.trayClick)
        self.connect.clicked.connect(self.connectComm)
        self.onconnect.clicked.connect(self.unConnectComm)
        
        self.getHotelInfo.clicked.connect(self.getHotel)
        self.addCard.clicked.connect(self.addIcCard)
        self.readCard.clicked.connect(self.readIcCard)
        self.clearCard.clicked.connect(self.clearIcCard)
        #配置发卡器
        self.setCard.clicked.connect(self.setCardHotel)
        
        self.getCardNumber.clicked.connect(self.getIcCardNumber)
        #写入酒店专用卡
        self.writeHotelCard.clicked.connect(self.writeHotelIcCard)
        #写入酒店总卡
        self.writeAllCard.clicked.connect(self.writeAllIcCard)
        #制作空白卡
        self.emptyCard.clicked.connect(self.emptyIcCard)
        #self.startSocket.clicked.connect(self.startSockets)
        #启动socket
        self.startSockets()
    def saveSetting(self):
        self.cf.set("Sections","cardPort", self.cardPort.text())  
        self.cf.set("Sections","appid", self.appid.text())  
        self.cf.set("Sections","secrets", self.secrets.text())  
        self.cf.set("Sections","socketPort", self.socketPort.text())  
        self.cf.set("Sections","socketIp", self.socketIp.text())  


        with open('config.ini', 'w') as f:
            self.cf.write(f)
        self.textLog.append(f"保存配置成功")
    def writeAllIcCard(self):
        buildNumber =  0
        floor = 0
        mac  = "000000000000".encode()
        times  = int(time.time()) + (86400*30)
        hotelInfo = self.hotelInfo.encode()
        allowLockOut = False
        res = self.clib.CE_WriteCard(hotelInfo,buildNumber,floor,mac,int(times),allowLockOut)  
        if res==0:
            self.textLog.append(f"写入总卡成功{res}")
        elif res==16:
            self.textLog.append("发卡器未连接")
        elif res==106:
            self.textLog.append("数据写入失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
        else :
            self.textLog.append(f"写入数据失败,错误码:{res}")         
        return res    
            
 
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
        #self.startSocket.setText(text)
        self.startSocket.setEnabled(False)
        # self.isConnect  = not self.isConnect
        # #如果已经连接断开socket
        # if self.isConnect:
        #     asyncio.run(self.socket_thread.stopThread())
        #     self.socket_thread.quit()
        #     #self.socket_thread.wait()
        #     print("线程关闭")
        #     self.textLog.append(f"断开socket连接")
        #     return
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
            allowLockOut = bool(jsonMsg.get("allowLockOut"))
            res = self.clib.CE_WriteCard(self.hotelInfo.encode(),buildNumber,floor,mac,endtime,allowLockOut)  
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
        elif jsonMsg.get("action") == "getIcCardNumber":    
            res =self.getIcCardNumber()                     
        print(res,"res")    
        if res !="":    
            data ={
                "status":res,
                "msg":getMsg().get(res),
                "list" :icCards,
                "cardNo" : self.icNumber,
                "type" : jsonMsg.get("action")
            } 
            asyncio.run(self.socket_thread.sendMsg(json.dumps(data),websocket))
            
    def startSound(self,length=1000,interval=100,number=2):
        length = 100 if length ==False else length
        re = self.clib.CE_Beep(length, interval, number)
        if re==0:
            self.textLog.append(f"发声成功{re},音长{length},间隔{interval},次数{number}")    
            self.writeLog(f"发声成功{re},音长{length},间隔{interval},次数{number}")
        elif re==16:      
            self.textLog.append(f"发卡器未连接{re}")  
            self.writeLog(f"发卡器未连接{re}")
        else:
            self.textLog.append(f"发声失败{re}") 
            self.writeLog(f"发声失败{re}")
        return re     
    
    def getIcCardNumber(self):  
        
        no = ctypes.c_char_p()
        re = self.clib.CE_GetCardNo(ctypes.byref(no))
        if re==0:
            self.icNumber = str(no.value,"UTF-8")
            self.textLog.append(f"获取成功{re}卡号:{self.icNumber}")   
        elif re==2:      
            self.textLog.append(f"参数错误{re}")    
        elif re==21:
            self.textLog.append(f"非Ic卡{re}") 
        else:
            self.textLog.append(f"其他错误{re}")  
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
        self.textLog.append("获取hotelInfo中...")
        self.writeLog("获取hotelInfo中...")
        self.getHotelInfo.setDisabled(True)
        self.worker_thread = QThread()
        self.worker = Worker(self.appid.text(),self.secrets.text())
        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.result.connect(self.show_result)
        self.worker_thread.started.connect(self.worker.do_work)
        self.worker_thread.start()  
        return 0
    @pyqtSlot(str)
    def show_result(self, result):
        print("返回结果",result)
        self.writeLog(f"返回结果{result}")
        self.hotelInfo =result
        self.textLog.append(result)   
        self.getHotelInfo.setDisabled(False) 
  
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
            self.writeLog(f"写入数据成功{res}")
        elif res==16:
            self.textLog.append("发卡器未连接")
            self.writeLog("发卡器未连接")
        elif res==106:
            self.textLog.append("数据写入失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
            self.writeLog("数据写入失败，IC卡非酒店卡或已被初始化为其它酒店的卡")
        else :
            self.textLog.append(f"写入数据失败,错误码:{res}")     
            self.writeLog(f"写入数据失败,错误码:{res}")    
        return res    
    def readIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        
        hotel_array_ptr = ctypes.c_char_p()
        
        res = self.clib.CE_ReadCard(hotelInfo,ctypes.byref(hotel_array_ptr))
        if res==0:
            #获取字符串数组
            try:
                self.textLog.append(f"读取数据成功{hotel_array_ptr.value.decode()}")
                self.writeLog(f"读取数据成功{hotel_array_ptr.value.decode()}")    
                self.icCards = hotel_array_ptr.value
            except:
                print("读取数据错误")  
           
        elif res==16:
            self.textLog.append("发卡器未连接")
            self.writeLog("发卡器未连接")    
        elif res==106:
            self.textLog.append("读取失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
            self.writeLog("读取失败，IC卡非酒店卡或已被初始化为其它酒店的卡")   
        else :
            self.textLog.append(f"读取数据失败,错误码:{res}")  
            self.writeLog(f"读取数据失败,错误码:{res}")   
 
        return res     
    def clearIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_ClearCard(hotelInfo)
        if res==0:
            self.textLog.append("ic卡清空成功")
            self.writeLog("ic卡清空成功") 
        elif res==16:
            self.textLog.append("发卡器未连接")
            self.writeLog("发卡器未连接") 
        elif res==106:
            self.textLog.append("操作失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
            self.writeLog("操作失败，IC卡非酒店卡或已被初始化为其它酒店的卡") 
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}") 
            self.writeLog(f"操作数据失败,错误码:{res}") 
        return res    
    def writeHotelIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_InitCard(hotelInfo) 
        if res==0:
            self.textLog.append("ic卡酒店专用卡成功")
            self.writeLog("ic卡酒店专用卡成功") 
        elif res==16:
            self.textLog.append("发卡器未连接")
            self.writeLog("发卡器未连接")
        elif res==106:
            self.textLog.append("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
            self.writeLog("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}") 
            self.writeLog(f"操作数据失败,错误码:{res}")
        return res    
    def emptyIcCard(self):
        hotelInfo = self.hotelInfo.encode()
        res = self.clib.CE_DeInitCard(hotelInfo) 
        if res==0:
            self.textLog.append("恢复空白Ic卡成功")
            self.writeLog("恢复空白Ic卡成功")
        elif res==16:
            self.textLog.append("发卡器未连接")
            self.writeLog("发卡器未连接")
        elif res==106:
            self.textLog.append("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")  
            self.writeLog("恢复空白卡失败，IC卡非酒店卡或已被初始化为其它酒店的卡")
        else :
            self.textLog.append(f"操作数据失败,错误码:{res}") 
            self.writeLog(f"操作数据失败,错误码:{res}")
        return res                
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    def mousePressEvent(self, event):
        # 鼠标按下时记录坐标
        self.mouse_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        # 鼠标移动时计算移动距离
        if self.mouse_pos:
            diff = event.globalPosition() - self.mouse_pos
            self.move(self.pos() + diff.toPoint())
            self.mouse_pos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        # 鼠标释放时清空坐标
        self.mouse_pos = None
    def trayClick(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.showNormal()    
    def closeEvent(self, event):
        # 点击关闭按钮时隐藏窗口并显示系统托盘图标
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("应用程序最小化到托盘", "单击托盘图标以恢复应用程序。")    
    def writeLog(self,msg):
        filelog = datetime.date.today()
        logging.basicConfig(filename=f'{filelog}.txt', level=logging.INFO, filemode='a', format='【%(asctime)s】 【%(levelname)s】 >>>  %(message)s', datefmt = '%Y-%m-%d %H:%M')
        logging.info(f'{msg}')
    
if __name__ == "__main__":
    filelog = datetime.date.today()
    logging.basicConfig(filename=f'{filelog}.txt', level=logging.DEBUG, filemode='a', format='【%(asctime)s】 【%(levelname)s】 >>>  %(message)s', datefmt = '%Y-%m-%d %H:%M')
    try:
        app = QApplication(sys.argv)
        password = Password()
        app.exit(app.exec())
    except Exception as e:
         logging.error("主程序抛错：")
         logging.error(e)
         logging.error("\n" + traceback.format_exc())
    

