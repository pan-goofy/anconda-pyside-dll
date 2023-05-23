# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1116, 976)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.cardFrame = QtWidgets.QFrame(parent=Form)
        self.cardFrame.setStyleSheet("cardFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.cardFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.cardFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.cardFrame.setObjectName("cardFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cardFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.exitCard = QtWidgets.QPushButton(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitCard.sizePolicy().hasHeightForWidth())
        self.exitCard.setSizePolicy(sizePolicy)
        self.exitCard.setMinimumSize(QtCore.QSize(30, 30))
        self.exitCard.setMaximumSize(QtCore.QSize(30, 30))
        self.exitCard.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.exitCard.setAutoFillBackground(False)
        self.exitCard.setStyleSheet("#exitCard{\n"
"    background-color: rgb(255, 255, 255); \n"
"    border-radius:15px;    \n"
"}")
        self.exitCard.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/myIcon/qidong-copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exitCard.setIcon(icon1)
        self.exitCard.setIconSize(QtCore.QSize(30, 30))
        self.exitCard.setAutoDefault(False)
        self.exitCard.setObjectName("exitCard")
        self.horizontalLayout_15.addWidget(self.exitCard)
        self.minimizeCard = QtWidgets.QPushButton(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeCard.sizePolicy().hasHeightForWidth())
        self.minimizeCard.setSizePolicy(sizePolicy)
        self.minimizeCard.setMinimumSize(QtCore.QSize(30, 30))
        self.minimizeCard.setMaximumSize(QtCore.QSize(30, 30))
        self.minimizeCard.setStyleSheet("#minimizeCard{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;    \n"
"}")
        self.minimizeCard.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/myIcon/zuixiaohua.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeCard.setIcon(icon2)
        self.minimizeCard.setIconSize(QtCore.QSize(30, 30))
        self.minimizeCard.setObjectName("minimizeCard")
        self.horizontalLayout_15.addWidget(self.minimizeCard)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.horizontalLayout_15.addItem(spacerItem)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.saveConfig = QtWidgets.QPushButton(parent=self.cardFrame)
        self.saveConfig.setMinimumSize(QtCore.QSize(200, 50))
        self.saveConfig.setMaximumSize(QtCore.QSize(200, 50))
        self.saveConfig.setStyleSheet("#saveConfig{\n"
"border-radius:20px;    \n"
"background-color: rgb(206, 228, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/myIcon/menjindukaqi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.saveConfig.setIcon(icon3)
        self.saveConfig.setObjectName("saveConfig")
        self.horizontalLayout_17.addWidget(self.saveConfig)
        self.getHotelInfo = QtWidgets.QPushButton(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getHotelInfo.sizePolicy().hasHeightForWidth())
        self.getHotelInfo.setSizePolicy(sizePolicy)
        self.getHotelInfo.setMinimumSize(QtCore.QSize(200, 50))
        self.getHotelInfo.setMaximumSize(QtCore.QSize(200, 50))
        self.getHotelInfo.setStyleSheet("#getHotelInfo{\n"
"border-radius:20px;    \n"
"background-color: rgb(206, 228, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/myIcon/xiangsu-fangwuloudong.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.getHotelInfo.setIcon(icon4)
        self.getHotelInfo.setObjectName("getHotelInfo")
        self.horizontalLayout_17.addWidget(self.getHotelInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.appid = QtWidgets.QLineEdit(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appid.sizePolicy().hasHeightForWidth())
        self.appid.setSizePolicy(sizePolicy)
        self.appid.setMinimumSize(QtCore.QSize(300, 40))
        self.appid.setMaximumSize(QtCore.QSize(300, 40))
        self.appid.setObjectName("appid")
        self.horizontalLayout_6.addWidget(self.appid)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.secrets = QtWidgets.QLineEdit(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secrets.sizePolicy().hasHeightForWidth())
        self.secrets.setSizePolicy(sizePolicy)
        self.secrets.setMinimumSize(QtCore.QSize(300, 40))
        self.secrets.setMaximumSize(QtCore.QSize(300, 40))
        self.secrets.setObjectName("secrets")
        self.horizontalLayout_7.addWidget(self.secrets)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.cardPort = QtWidgets.QLineEdit(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardPort.sizePolicy().hasHeightForWidth())
        self.cardPort.setSizePolicy(sizePolicy)
        self.cardPort.setMinimumSize(QtCore.QSize(300, 40))
        self.cardPort.setMaximumSize(QtCore.QSize(300, 40))
        self.cardPort.setObjectName("cardPort")
        self.horizontalLayout_10.addWidget(self.cardPort)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect = QtWidgets.QPushButton(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect.sizePolicy().hasHeightForWidth())
        self.connect.setSizePolicy(sizePolicy)
        self.connect.setMinimumSize(QtCore.QSize(200, 40))
        self.connect.setMaximumSize(QtCore.QSize(200, 40))
        self.connect.setStyleSheet("#connect{\n"
"border-radius:20px;    \n"
"background-color: rgb(206, 228, 255);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/myIcon/shishidukaqi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.connect.setIcon(icon5)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.onconnect = QtWidgets.QPushButton(parent=self.cardFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onconnect.sizePolicy().hasHeightForWidth())
        self.onconnect.setSizePolicy(sizePolicy)
        self.onconnect.setMinimumSize(QtCore.QSize(200, 40))
        self.onconnect.setMaximumSize(QtCore.QSize(200, 40))
        self.onconnect.setStyleSheet("#onconnect{\n"
"background-color: rgb(255, 213, 253);\n"
"border-radius:20px;    \n"
"\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/myIcon/shuma-duqiaqi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.onconnect.setIcon(icon6)
        self.onconnect.setObjectName("onconnect")
        self.horizontalLayout.addWidget(self.onconnect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.addCard = QtWidgets.QPushButton(parent=self.cardFrame)
        self.addCard.setMinimumSize(QtCore.QSize(0, 40))
        self.addCard.setStyleSheet("#addCard{\n"
"background-color:  rgb(206, 228, 255);\n"
"border-radius:15px;    \n"
"\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/myIcon/card1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addCard.setIcon(icon7)
        self.addCard.setObjectName("addCard")
        self.horizontalLayout_13.addWidget(self.addCard)
        self.readCard = QtWidgets.QPushButton(parent=self.cardFrame)
        self.readCard.setMinimumSize(QtCore.QSize(0, 40))
        self.readCard.setStyleSheet("#readCard{\n"
"background-color:  rgb(135, 255, 159);\n"
"border-radius:15px;    \n"
"\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/myIcon/name-card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.readCard.setIcon(icon8)
        self.readCard.setObjectName("readCard")
        self.horizontalLayout_13.addWidget(self.readCard)
        self.clearCard = QtWidgets.QPushButton(parent=self.cardFrame)
        self.clearCard.setMinimumSize(QtCore.QSize(0, 40))
        self.clearCard.setStyleSheet("#clearCard{\n"
"background-color: rgb(255, 213, 253);\n"
"border-radius:15px;    \n"
"\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/myIcon/louceng1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clearCard.setIcon(icon9)
        self.clearCard.setObjectName("clearCard")
        self.horizontalLayout_13.addWidget(self.clearCard)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.floor = QtWidgets.QLineEdit(parent=self.cardFrame)
        self.floor.setMinimumSize(QtCore.QSize(0, 30))
        self.floor.setObjectName("floor")
        self.horizontalLayout_2.addWidget(self.floor)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.cardFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.building = QtWidgets.QLineEdit(parent=self.cardFrame)
        self.building.setMinimumSize(QtCore.QSize(0, 30))
        self.building.setObjectName("building")
        self.horizontalLayout_3.addWidget(self.building)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.doorMac = QtWidgets.QLineEdit(parent=self.cardFrame)
        self.doorMac.setMinimumSize(QtCore.QSize(0, 30))
        self.doorMac.setObjectName("doorMac")
        self.horizontalLayout_5.addWidget(self.doorMac)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.time = QtWidgets.QLineEdit(parent=self.cardFrame)
        self.time.setMinimumSize(QtCore.QSize(0, 30))
        self.time.setObjectName("time")
        self.horizontalLayout_4.addWidget(self.time)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.writeHotelCard = QtWidgets.QPushButton(parent=self.cardFrame)
        self.writeHotelCard.setMinimumSize(QtCore.QSize(0, 40))
        self.writeHotelCard.setStyleSheet("#writeHotelCard{\n"
"border-radius:20px;    \n"
"background-color: rgb(206, 228, 255);\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/myIcon/zu49.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.writeHotelCard.setIcon(icon10)
        self.writeHotelCard.setObjectName("writeHotelCard")
        self.horizontalLayout_8.addWidget(self.writeHotelCard)
        self.emptyCard = QtWidgets.QPushButton(parent=self.cardFrame)
        self.emptyCard.setMinimumSize(QtCore.QSize(0, 40))
        self.emptyCard.setStyleSheet("#emptyCard{\n"
"border-radius:20px;    \n"
"background-color:  rgb(255, 213, 253);\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/myIcon/louceng.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.emptyCard.setIcon(icon11)
        self.emptyCard.setObjectName("emptyCard")
        self.horizontalLayout_8.addWidget(self.emptyCard)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.cardFrame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.socketPort = QtWidgets.QLineEdit(parent=self.cardFrame)
        self.socketPort.setMinimumSize(QtCore.QSize(0, 40))
        self.socketPort.setObjectName("socketPort")
        self.horizontalLayout_9.addWidget(self.socketPort)
        self.startSocket = QtWidgets.QPushButton(parent=self.cardFrame)
        self.startSocket.setMinimumSize(QtCore.QSize(0, 40))
        self.startSocket.setObjectName("startSocket")
        self.horizontalLayout_9.addWidget(self.startSocket)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_14.addWidget(self.cardFrame)
        self.textLog = QtWidgets.QTextBrowser(parent=Form)
        self.textLog.setObjectName("textLog")
        self.horizontalLayout_14.addWidget(self.textLog)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_14)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveConfig.setText(_translate("Form", "保存配置"))
        self.getHotelInfo.setText(_translate("Form", "获取hotelInfo"))
        self.label_5.setText(_translate("Form", "appid"))
        self.appid.setText(_translate("Form", "f37d200d9d5b4250924ce43280ed806e"))
        self.label_6.setText(_translate("Form", "secrets"))
        self.secrets.setText(_translate("Form", "4b88327993e0695ea16d54be377a639b"))
        self.label_8.setText(_translate("Form", "发卡器串口"))
        self.cardPort.setText(_translate("Form", "COM3"))
        self.connect.setText(_translate("Form", "连接发卡器"))
        self.onconnect.setText(_translate("Form", "断开连接"))
        self.addCard.setText(_translate("Form", "添加ic卡"))
        self.readCard.setText(_translate("Form", "读取ic卡"))
        self.clearCard.setText(_translate("Form", "清空ic卡"))
        self.label_2.setText(_translate("Form", "楼层号"))
        self.floor.setText(_translate("Form", "1"))
        self.label.setText(_translate("Form", "楼栋号"))
        self.building.setText(_translate("Form", "1"))
        self.label_3.setText(_translate("Form", "设备MAC"))
        self.doorMac.setText(_translate("Form", "D059F21EE252"))
        self.label_4.setText(_translate("Form", "有效时间"))
        self.time.setText(_translate("Form", "1684344289"))
        self.writeHotelCard.setText(_translate("Form", "写酒店专用卡"))
        self.emptyCard.setText(_translate("Form", "恢复空白卡"))
        self.label_7.setText(_translate("Form", "socket端口号"))
        self.socketPort.setText(_translate("Form", "8989"))
        self.startSocket.setText(_translate("Form", "启动"))
        self.textLog.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
