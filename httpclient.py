import sys
import typing
import requests
from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import time
import json
class Worker(QObject):
    def __init__(self, appid,secrets):
        super().__init__()
        self.appid = appid
        self.secrets = secrets
    finished = pyqtSignal()
    result = pyqtSignal(str)

    @pyqtSlot()
    def do_work(self):
        url = "https://cnapi.ttlock.com/v3/hotel/getInfo"
        data = {
            "clientId": self.appid,
            "clientSecret": self.secrets,
            "date": int(time.time()) * 1000,
        }
        try:
            response = requests.post(url, params=data).text
            data = json.loads(response)
            self.hotelInfo = data['hotelInfo']
        except requests.exceptions.RequestException as e :    
            print("请求hotelInfo失败",e)
        #self.textLog.append(f"获取hotelInfo: {data['hotelInfo']}")  
        self.result.emit(self.hotelInfo)
        self.finished.emit()