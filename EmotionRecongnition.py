# -*- coding: utf-8 -*-


import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from real_time_video_me import Emotion_Rec
from os import getcwd
import numpy as np
import cv2
import time
from base64 import b64decode
from os import remove
from slice_png import img as bgImg

#from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QPushButton
from PyQt5.QtWidgets import *
#import SecondUi
class SecondUi(QWidget):
    def __init__(self, name = 'MainForm'):
        super(SecondUi,self).__init__()
        self.setWindowTitle(name)
        self.count=1
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.resize(300,600)   # 设置窗体大小
        _translate = QtCore.QCoreApplication.translate
        
        self.window_pale=QtGui.QPalette()
        #self.img=
        self.window_pale.setBrush(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("images_test/bg.png")))
        self.setPalette(self.window_pale)
        
        self.files=['angry','disgust','happy','neutral','sad','scared','surprised']
        self.EMOTION=['angry','disgust','happy','neutral','sad','scared','surprised']
        # angry 1
        self.btn_choose_angry = QPushButton(self)  
        self.btn_choose_angry.setGeometry(QtCore.QRect(20,20,50,40))
        self.btn_choose_angry.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_angry.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_angry.setObjectName("btn_choose_angry")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/angry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_angry.setIcon(icon)
        self.btn_choose_angry.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_angry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_angry.setAutoFillBackground(False)
        
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        font.setItalic(True)
       
        self.text_angry = QtWidgets.QLabel(self)
        self.text_angry.setFont(font)
        self.text_angry.setGeometry(QtCore.QRect(80, 20, 200, 40))
        self.text_angry.setText("choose_angry")
    

        self.text_angry.setStyleSheet("font-color:white")
        self.text_angry.setObjectName("angry")
        self.text_angry.setFrameShape(QtWidgets.QFrame.Box)
        self.text_angry.setFrameShadow(QtWidgets.QFrame.Raised)
        
        # disgust 2
        self.btn_choose_disgust = QPushButton(self)  
        self.btn_choose_disgust.setGeometry(QtCore.QRect(20,90,50,40))
        self.btn_choose_disgust.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_disgust.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_disgust.setObjectName("btn_choose_disgust")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/disgust.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_disgust.setIcon(icon)
        self.btn_choose_disgust.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_disgust.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_disgust.setAutoFillBackground(False)
        
        self.text_disgust = QtWidgets.QLabel(self)
        self.text_disgust.setFont(font)
        self.text_disgust.setGeometry(QtCore.QRect(80, 90, 200, 40))
        self.text_disgust.setText("choose_disgust")
    

        self.text_disgust.setStyleSheet("font-color:white")
        self.text_disgust.setObjectName("disgust")
        self.text_disgust.setFrameShape(QtWidgets.QFrame.Box)
        self.text_disgust.setFrameShadow(QtWidgets.QFrame.Raised)
        # happy 3
        self.btn_choose_happy = QPushButton(self)  
        self.btn_choose_happy.setGeometry(QtCore.QRect(20,160,50,40))
        self.btn_choose_happy.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_happy.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_happy.setObjectName("btn_choose_happy")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/happy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_happy.setIcon(icon)
        self.btn_choose_happy.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_happy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_happy.setAutoFillBackground(False)

        self.text_happy = QtWidgets.QLabel(self)
        self.text_happy.setFont(font)
        self.text_happy.setGeometry(QtCore.QRect(80, 160, 200, 40))
        self.text_happy.setText("choose_happy")
    

        self.text_happy.setStyleSheet("font-color:white")
        self.text_happy.setObjectName("angry")
        self.text_happy.setFrameShape(QtWidgets.QFrame.Box)
        self.text_happy.setFrameShadow(QtWidgets.QFrame.Raised)
        # neutral 4
        self.btn_choose_neutral = QPushButton(self)  
        self.btn_choose_neutral.setGeometry(QtCore.QRect(20,230,50,40))
        self.btn_choose_neutral.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_neutral.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_neutral.setObjectName("btn_choose_neural")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/netural.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_neutral.setIcon(icon)
        self.btn_choose_neutral.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_neutral.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_neutral.setAutoFillBackground(False)
        
        self.text_neutral= QtWidgets.QLabel(self)
        self.text_neutral.setFont(font)
        self.text_neutral.setGeometry(QtCore.QRect(80, 230, 200, 40))
        self.text_neutral.setText("choose_neutral")
    

        self.text_neutral.setStyleSheet("font-color:white")
        self.text_neutral.setObjectName("neutral")
        self.text_neutral.setFrameShape(QtWidgets.QFrame.Box)
        self.text_neutral.setFrameShadow(QtWidgets.QFrame.Raised)
        #sad 5
        self.btn_choose_sad = QPushButton(self)  
        self.btn_choose_sad.setGeometry(QtCore.QRect(20,300,50,40))
        self.btn_choose_sad.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_sad.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_sad.setObjectName("btn_choose_sad")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/sad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_sad.setIcon(icon)
        self.btn_choose_sad.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_sad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_sad.setAutoFillBackground(False)
        
        self.text_sad = QtWidgets.QLabel(self)
        self.text_sad.setFont(font)
        self.text_sad.setGeometry(QtCore.QRect(80, 300, 200, 40))
        self.text_sad.setText("choose_sad")
    

        self.text_sad.setStyleSheet("font-color:white")
        self.text_sad.setObjectName("sad")
        self.text_sad.setFrameShape(QtWidgets.QFrame.Box)
        self.text_sad.setFrameShadow(QtWidgets.QFrame.Raised)
        #scared 6
        self.btn_choose_scared = QPushButton(self)  
        self.btn_choose_scared.setGeometry(QtCore.QRect(20,370,50,40))
        self.btn_choose_scared.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_scared.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_scared.setObjectName("btn_choose_scared")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/scared.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_scared.setIcon(icon)
        self.btn_choose_scared.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_scared.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_scared.setAutoFillBackground(False)
        
        self.text_scared = QtWidgets.QLabel(self)
        self.text_scared.setFont(font)
        self.text_scared.setGeometry(QtCore.QRect(80, 370, 200, 40))
        self.text_scared.setText("choose_scared")
    

        self.text_scared.setStyleSheet("font-color:white")
        self.text_scared.setObjectName("scared")
        self.text_scared.setFrameShape(QtWidgets.QFrame.Box)
        self.text_scared.setFrameShadow(QtWidgets.QFrame.Raised)
        #surprised 7        
        self.btn_choose_surprised = QPushButton(self)  
        self.btn_choose_surprised.setGeometry(QtCore.QRect(20,440,50,40))
        self.btn_choose_surprised.setMinimumSize(QtCore.QSize(50,39))
        self.btn_choose_surprised.setMaximumSize(QtCore.QSize(50,40))
        self.btn_choose_surprised.setObjectName("btn_choose_surprised")  
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/surprised.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choose_surprised.setIcon(icon)
        self.btn_choose_surprised.setIconSize(QtCore.QSize(40, 40))
        self.btn_choose_surprised.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_choose_surprised.setAutoFillBackground(False)
        
        self.text_surprised = QtWidgets.QLabel(self)
        self.text_surprised.setFont(font)
        self.text_surprised.setGeometry(QtCore.QRect(80, 440, 200, 40))
        self.text_surprised.setText("choose_surprised")
    

        self.text_surprised.setStyleSheet("font-color:white")
        self.text_surprised.setObjectName("angry")
        self.text_surprised.setFrameShape(QtWidgets.QFrame.Box)
        self.text_surprised.setFrameShadow(QtWidgets.QFrame.Raised)
        #compose
        self.btn_compose = QPushButton('compose', self)#设置按钮和按钮名称
        self.btn_compose.setObjectName("btn_compose")
        self.btn_compose.setText("compose")
        self.btn_compose.setStyleSheet(" QPushButton:hover{background-color:rgb(0, 0, 255)}")
        self.btn_compose.setGeometry(40, 500, 200, 25)#前面是按钮左上角坐标，后面是窗口大小
        #self.btn_compose.clicked.connect(self.slot_btn_compose)#将信号连接到槽
        
        #back
        self.btn_back=QPushButton('back',self)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText('back')
        self.btn_back.setStyleSheet(" QPushButton:hover{background-color:rgb(0, 0, 255)}")
        self.btn_back.setGeometry(40, 550, 200, 25)
        # 设置布局
        layout = QVBoxLayout()
 
        self.setLayout(layout)


        # 设置信号
        self.btn_choose_angry.clicked.connect(self.slot_btn_choose_angry)
        self.btn_choose_disgust.clicked.connect(self.slot_btn_choose_disgust)
        self.btn_choose_happy.clicked.connect(self.slot_btn_choose_happy)
        self.btn_choose_neutral.clicked.connect(self.slot_btn_choose_neutral)
        self.btn_choose_sad.clicked.connect(self.slot_btn_choose_sad)
        self.btn_choose_scared.clicked.connect(self.slot_btn_choose_scared)
        self.btn_choose_surprised.clicked.connect(self.slot_btn_choose_surprised)
        self.btn_compose.clicked.connect(self.slot_btn_compose)#将信号连接到槽
        self.btn_back.clicked.connect(self.slot_btn_back)

    def slot_btn_choose_angry(self):
      
        self.files[0], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/angry", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  

       

    def slot_btn_choose_disgust(self):
        self.files[1], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/disgust", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  

      

    def slot_btn_choose_happy(self):
        self.files[2], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/happy", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  


    def slot_btn_choose_neutral(self):
        self.files[3], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/neutral", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  


    def slot_btn_choose_sad(self):
      
        self.files[4], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/sad", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  


    def slot_btn_choose_scared(self):
        self.files[5], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/scared", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  



    def slot_btn_choose_surprised(self):
        self.files[6], filetype = QFileDialog.getOpenFileNames(self,  
                                    "多文件选择",  
                                    "emotion/surprised", # 起始路径 
                                    "All Files (*);;JPG Files (*.jpg)")  


    def slot_btn_compose(self):
        fps=12
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')#不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
        file_Path=r"emotion/compose"+str(self.count)+".avi"
        self.count=self.count+1
        video = cv2.VideoWriter(file_Path, fourcc, fps, (300,225))
        j=0
        for emotion in self.EMOTION:
            #index=self.EMOTION.index[emotion]
            emoji_path="emotion/emoji/"+emotion+".jpg"
            for i in range(1,6):
                img=cv2.imread(emoji_path)
                video.write(img)                 
            for file in self.files[j]:
                img=cv2.imread(file)
                video.write(img)
            j=j+1             
        video.release()                
         
    def slot_btn_back(self):
        self.hide()#隐藏此窗口
                            
            
class  FirstUi(QWidget):#第一个窗口
    def __init__(self,MainWindow):
        super(FirstUi, self).__init__()
        self.time_video=QtCore.QTimer()
        self.init_ui(MainWindow)
        self.cap=cv2.VideoCapture('emotion/compose1.avi')
        
    def init_ui(self,MainWindow):
        
        self.time_video.timeout.connect(self.show_video)
        self.video_width=300
        self.video_height=225
        self.resize(600, 400)#设置窗口大小
        self.setWindowTitle('First Ui')#设置窗口标题
        self.btn = QPushButton('back', self)#设置按钮和按钮名称
        self.btn.setGeometry(200, 350, 50, 25)#前面是按钮左上角坐标，后面是窗口大小
        self.btn.setStyleSheet(" QPushButton:hover{background-color:rgb(0, 0, 255)}")

        self.btn.clicked.connect(self.slot_btn_function)#将信号连接到槽
        self.btn2=QPushButton('Play',self)
        self.btn2.setGeometry(350,350,50,25)
        self.btn2.setStyleSheet(" QPushButton:hover{background-color:rgb(0, 0, 255)}")

        self.btn2.clicked.connect(self.play)
        
        self.window_pale=QtGui.QPalette()
        #self.img=
        self.window_pale.setBrush(self.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("images_test/bg2.png")))
        self.setPalette(self.window_pale)
        
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        self.label_video = QtWidgets.QLabel(self)
        self.label_video.setGeometry(QtCore.QRect(150, 80,self.video_width, self.video_height))
        self.label_video.setMinimumSize(QtCore.QSize(self.video_width,self.video_height))
        self.label_video.setMaximumSize(QtCore.QSize(self.video_width, self.video_height))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_video.setFont(font)
        self.label_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_video.setPixmap(QtGui.QPixmap("images_test/scan2.gif"))
        self.label_video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video.setObjectName("label_video")
        
        gif = QMovie('images_test/scan2.gif')
        self.label_video.setMovie(gif)
        gif.start()
        
       
    
        
    def slot_btn_function(self):
        self.hide()#隐藏此窗口
        self.cap.release()
        self.label_video.clear()
        gif = QMovie('images_test/scan2.gif')
        self.label_video.setMovie(gif)
        gif.start()    
        self.hide()#隐藏此窗口
 
    def play(self):
        #self.label_video.setPixmap("Users\\shuifan\\Desktop\\database\\emotion\\angry\\1.jpg")
        self.label_video.clear()
        #a=1
        print('begin')
        if self.time_video.isActive() == False:  # 检查定时状态
    
            QtWidgets.QApplication.processEvents()
                #self.textEdit_camera.setText('实时摄像已开启')      
            QtWidgets.QApplication.processEvents()
            # 打开定时器
            self.time_video.start(30)
        else:
                # 选择取消，恢复界面状态
                # self.textEdit_pic1.setText('文件未选中')
            #gif = QMovie(':/newPrefix/images_test/scan.gif')
            self.cap=cv2.VideoCapture('emotion/compose1.avi')
            gif=QMovie('images_test/scan2.gif')
            self.label_video.setMovie(gif)
            gif.start()
    def show_video(self):
        
        flag1, self.image = self.cap.read() # 获取画面
        self.image=cv2.flip(self.image, 1) # 左右翻转
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_video.setPixmap(QtGui.QPixmap.fromImage(showImage))
        QtWidgets.QApplication.processEvents()
       
        time_start = time.time() # 计时
        # 使用模型预测
        
        time_end = time.time()
            
class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.path = getcwd()
        self.timer_camera = QtCore.QTimer() # 定时器
       
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.slot_init(MainWindow) # 槽函数设置

        # 设置界面动画
        gif = QMovie('images_test/scan1.gif')
        self.label_face.setMovie(gif)
        gif.start()
        
        self.count=1#记录生成视频的数量
        self.EMOTION=["angry","disgust","happy","neutral","sad","scared","surprised"]   
        self.image_Path="emotion/"
        
        self.cap = cv2.VideoCapture() # 屏幕画面对象
        self.capture=cv2.VideoCapture("1.avi")
        self.CAM_NUM = 0 # 摄像头标号
        self.model_path = None # 模型路径
        # self.__flag_work = 0
        self.flag=0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(765, 645)
        MainWindow.setMinimumSize(QtCore.QSize(765, 645))
        MainWindow.setMaximumSize(QtCore.QSize(765, 645))
        MainWindow.setToolTip("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False )
        MainWindow.setStyleSheet("#MainWindow{border-image: url(images_test/background.PNG);}\n"
                                 "\n"
                                 "#QInputDialog{border-image: url(images_test/light.png);}\n"
                                 "\n"
                                 "QMenuBar{border-color:transparent;}\n"
                                 "QToolButton[objectName=pushButton_doIt]{\n"
                                 "border:5px;}\n"
                                 "\n"
                                 "QToolButton[objectName=pushButton_doIt]:hover {\n"
                                 "image:url(images_test/run_hover.png);}\n"
                                 "\n"
                                 "QToolButton[objectName=pushButton_doIt]:pressed {\n"
                                 "image:url(images_test/run_pressed.png);}\n"
                                 "\n"
                                 "QScrollBar:vertical{\n"
                                 "background:transparent;\n"
                                 "padding:2px;\n"
                                 "border-radius:8px;\n"
                                 "max-width:14px;}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical{\n"
                                 "background:#9acd32;\n"
                                 "min-height:50px;\n"
                                 "border-radius:8px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical:hover{\n"
                                 "background:#9eb764;}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical:pressed{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "                               \n"
                                 "QScrollBar::sub-page:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical{\n"
                                 "background:none;}\n"
                                 "                                 \n"
                                 "QScrollBar::sub-line:vertical{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QScrollArea{\n"
                                 "border:0px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal{\n"
                                 "background:transparent;\n"
                                 "padding:0px;\n"
                                 "border-radius:6px;\n"
                                 "max-height:4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal{\n"
                                 "background:#9acd32;\n"
                                 "min-width:50px;\n"
                                 "border-radius:6px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal:hover{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal:pressed{\n"
                                 "background:#9eb764;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-page:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QScrollBar::add-line:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal{\n"
                                 "background:none;\n"
                                 "}\n"
                                 "QToolButton::hover{\n"
                                 "border:0px;\n"
                                 "} ")
      
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 765, 645))
        self.label_bg.setPixmap(QtGui.QPixmap("images_test/bkg.png"))
        
        self.label_bg.setText("")
        self.label_bg.setObjectName("background")
        
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(80, 40, 271, 30))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(250, 110, 132, 30))
        self.label_author.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_author.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_author.setObjectName("label_author")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(530, 200, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(530, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(480, 200, 38, 38))
        self.label_picTime.setPixmap(QtGui.QPixmap("images_test/clock.png"))
        
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(480, 270, 41, 41))
        self.label_picResult.setPixmap(QtGui.QPixmap("images_test/result.png"))
        #self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/images_test/result.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(440, 160, 321, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(10, 360, 420, 280))
        self.label_face.setMinimumSize(QtCore.QSize(420, 280))
        self.label_face.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:images_test/scan1.gif);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.textEdit_model = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_model.setGeometry(QtCore.QRect(60, 180, 360, 30))
        self.textEdit_model.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_model.setMaximumSize(QtCore.QSize(360, 30))
        self.textEdit_model.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_model.setFont(font)
        self.textEdit_model.setStyleSheet("background-color: transparent;\n"
                                          "border-color: rgb(255, 255, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.textEdit_model.setReadOnly(True)
        self.textEdit_model.setObjectName("textEdit_model")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(10, 300, 50, 40))
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        self.toolButton_file.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon)
        self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_camera_2")
        
        self.toolButton_file1 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file1.setGeometry(QtCore.QRect(10, 130, 50, 40))
        self.toolButton_file1.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file1.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file1.setAutoFillBackground(False)
        self.toolButton_file1.setStyleSheet("background-color: transparent;")
        self.toolButton_file1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file1.setIcon(icon)
        self.toolButton_file1.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file1.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file1.setAutoRaise(False)
        self.toolButton_file1.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file1.setObjectName("toolButton_camera_3")
        #合成按钮
        self.toolButton_file2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file2.setGeometry(QtCore.QRect(450,40 ,50 ,40))
        self.toolButton_file2.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file2.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file2.setAutoFillBackground(False)
        self.toolButton_file2.setStyleSheet("background-color: transparent;")
        self.toolButton_file2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/join.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file2.setIcon(icon)
        self.toolButton_file2.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file2.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file2.setAutoRaise(False)
        self.toolButton_file2.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file2.setObjectName("compose")        
          #clear按钮
        self.toolButton_file3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file3.setGeometry(QtCore.QRect(450, 80, 50, 40))
        self.toolButton_file3.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file3.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file3.setAutoFillBackground(False)
        self.toolButton_file3.setStyleSheet("background-color: transparent;")
        self.toolButton_file3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file3.setIcon(icon)
        self.toolButton_file3.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file3.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file3.setAutoRaise(False)
        self.toolButton_file3.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file3.setObjectName("clear")                
        #播放按钮
        self.toolButton_file4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file4.setGeometry(QtCore.QRect(450, 120, 50, 40))
        self.toolButton_file4.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file4.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file4.setAutoFillBackground(False)
        self.toolButton_file4.setStyleSheet("background-color: transparent;")
        self.toolButton_file4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images_test/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file4.setIcon(icon)
        self.toolButton_file4.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file4.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file4.setAutoRaise(False)
        self.toolButton_file4.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file4.setObjectName("clear")                
        
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(60, 250, 360, 30))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_camera.setMaximumSize(QtCore.QSize(360, 30))
        self.textEdit_camera.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
                                           "border-color: rgb(255, 255, 255);\n"
                                           "color: rgb(255, 255, 255);")
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(60, 310, 360, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(360, 30))
        self.textEdit_pic.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        
        self.textEdit_pic1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic1.setGeometry(QtCore.QRect(60,130 , 360, 30))
        self.textEdit_pic1.setMinimumSize(QtCore.QSize(360, 30))
        self.textEdit_pic1.setMaximumSize(QtCore.QSize(360, 30))
        self.textEdit_pic1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_pic1.setFont(font)
        self.textEdit_pic1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic1.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        #合成 text
        self.textEdit_pic2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic2.setGeometry(QtCore.QRect(510,40 , 360, 30))
        self.textEdit_pic2.setMinimumSize(QtCore.QSize(80, 30))
        self.textEdit_pic2.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_pic2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_pic2.setFont(font)
        self.textEdit_pic2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic2.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        
        self.textEdit_pic2.setReadOnly(True)
        self.textEdit_pic2.setObjectName("textEdit_pic1")
        #清空text
        self.textEdit_pic3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic3.setGeometry(QtCore.QRect(510,80 , 360, 30))
        self.textEdit_pic3.setMinimumSize(QtCore.QSize(80, 30))
        self.textEdit_pic3.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_pic3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_pic3.setFont(font)
        self.textEdit_pic3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic3.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        
        self.textEdit_pic3.setReadOnly(True)
        self.textEdit_pic3.setObjectName("textEdit_pic3")    
       #播放text
        self.textEdit_pic4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic4.setGeometry(QtCore.QRect(510,120 , 360, 30))
        self.textEdit_pic4.setMinimumSize(QtCore.QSize(80, 30))
        self.textEdit_pic4.setMaximumSize(QtCore.QSize(80, 30))
        self.textEdit_pic4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_pic4.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.textEdit_pic4.setFont(font)
        self.textEdit_pic4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic4.setStyleSheet("background-color: transparent;\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "color: rgb(255, 255, 255);")
        
        self.textEdit_pic4.setReadOnly(True)
        self.textEdit_pic4.setObjectName("textEdit_pic4")    
    
    
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(10, 240, 50, 45))
        self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;")
        self.toolButton_camera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images_test/cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon1)
        self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_model.setGeometry(QtCore.QRect(10, 170, 50, 40))
        self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        self.toolButton_model.setStyleSheet("background-color: transparent;")
        self.toolButton_model.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images_test/module.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_model.setIcon(icon2)
        self.toolButton_model.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_model.setObjectName("toolButton_model")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(610, 206, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(440, 340, 321, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(640, 278, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setObjectName("label_result")
        self.label_outputResult = QtWidgets.QLabel(self.centralwidget)
        self.label_outputResult.setGeometry(QtCore.QRect(450, 380, 300, 250))
        self.label_outputResult.setText("")
        self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
        #self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test/ini.png);")
        self.label_outputResult.setObjectName("label_outputResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion recongnition "))
        self.label_title.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
        self.label_title.setText(_translate("MainWindow", "表情识别系统"))
        self.label_author.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
  
        self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>用时：</p></body></html>"))
        self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>识别结果：<br/></p></body></html>"))
        self.label_face.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        
        self.textEdit_pic4.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">播放</span></p></body></html>"))
        
        self.textEdit_pic3.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">清空</span></p></body></html>"))
        
        self.textEdit_pic2.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">合成影集</span></p></body></html>"))
        
        self.textEdit_pic1.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">选择视频</span></p></body></html>"))
        
        self.textEdit_model.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">选择模型</span></p></body></html>"))
        self.textEdit_camera.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">实时摄像未开启</span></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';color:black\">选择图片</span></p></body></html>"))
        self.label_time.setText(_translate("MainWindow", "0 s"))
        self.label_result.setText(_translate("MainWindow", "None"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))


    def slot_init(self,MainWindow): # 定义槽函数
       
        self.toolButton_camera.clicked.connect(self.button_open_camera_click)
        self.toolButton_model.clicked.connect(self.choose_model)
        self.timer_camera.timeout.connect(self.show_camera)
        self.toolButton_file.clicked.connect(self.choose_pic)
        self.toolButton_file1.clicked.connect(self.choose_video)
        self.toolButton_file2.clicked.connect(self.compose)
        self.toolButton_file3.clicked.connect(self.clear)
        self.toolButton_file4.clicked.connect(self.slot_btn_function)

    def button_open_camera_click(self):
        self.flag=1
        self.capture.release()
        if self.timer_camera.isActive() == False: # 检查定时状态
            flag = self.cap.open(self.CAM_NUM) # 检查相机状态
            if flag == False: # 相机打开失败提示
                msg = QtWidgets.QMessageBox.warning(self.centralwidget, u"Warning",
                                                    u"请检测相机与电脑是否连接正确！ ",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)

            else:
                # 准备运行识别程序
                self.textEdit_pic.setText('文件未选中')
                self.textEdit_pic1.setText('文件未选中')
                QtWidgets.QApplication.processEvents()
                self.textEdit_camera.setText('实时摄像已开启')
                self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                self.emotion_model = Emotion_Rec(self.model_path)
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            self.label_face.clear()
            self.textEdit_camera.setText('实时摄像已关闭')
            self.textEdit_pic.setText('选择图片')
            self.textEdit_pic1.setText('选择视频')
            gif = QMovie('C:\\Users\\shuifan\\Desktop\\database\\images_test\\scan1.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear()
       
            self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
            self.label_result.setText('None')
            self.label_time.setText('0 s')


    def show_camera(self):
        
        if self.flag==1:
            flag1, self.image = self.cap.read() # 获取画面
            self.image=cv2.flip(self.image, 1) # 左右翻转
            #tmp = open('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png', 'wb')
            #tmp.write(b64decode(bgImg))
            #tmp.close()
            canvas = cv2.imread('images_test/slice.png') # 用于数据显示的背景图片
           # remove('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png')

            time_start = time.time() # 计时
        # 使用模型预测
            result = self.emotion_model.run(self.image, canvas, self.label_face, self.label_outputResult)
            time_end = time.time()
        else:
            flag1, self.image1 = self.capture.read() # 获取画面
            self.image1=cv2.flip(self.image1, 1) # 左右翻转
           
            #tmp = open('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png', 'wb')
            #tmp.write(b64decode(bgImg))
            #tmp.close()
            canvas = cv2.imread('images_test/slice.png') # 用于数据显示的背景图片
            #remove('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png')

            time_start = time.time() # 计时
        # 使用模型预测
            result = self.emotion_model.run(self.image1, canvas, self.label_face, self.label_outputResult)
            time_end = time.time()
        # 在界面显示结果
        self.label_result.setText(result)
        self.label_time.setText(str(round((time_end-time_start),3))+' s')

        
    def choose_pic(self):
        # 界面处理
        self.capture.release()
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()
        self.label_result.setText('None')
        self.label_time.setText('0 s')
        self.textEdit_camera.setText('实时摄像已关闭')
        self.label_outputResult.clear()
        #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
        self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
        # 使用文件选择对话框选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(
                                self.centralwidget, "选取图片文件",
                                self.path,  # 起始路径
                                "图片(*.jpg;*.jpeg;*.png)") # 文件类型
        self.path = fileName_choose # 保存路径
        if fileName_choose != '':
            self.textEdit_pic.setText(fileName_choose+'文件已选中')
            self.label_face.setText('正在启动识别系统...\n\nleading')
            QtWidgets.QApplication.processEvents()
            # 生成模型对象
            self.emotion_model = Emotion_Rec(self.model_path)
            # 读取背景图
           # tmp = open('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png', 'wb')
            #tmp.write(b64decode(bgImg))
            #tmp.close()
            canvas = cv2.imread('images_test/slice.png')
            #remove('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png')

            image = self.cv_imread(fileName_choose) # 读取选择的图片
            # 计时并开始模型预测
            QtWidgets.QApplication.processEvents()
            time_start = time.time()
            result = self.emotion_model.run(image, canvas, self.label_face, self.label_outputResult)
            time_end = time.time()
            # 显示结果
            self.label_result.setText(result)
            self.label_time.setText(str(round((time_end - time_start), 3)) + ' s')

        else:
            # 选择取消，恢复界面状态
            self.textEdit_pic.setText('选择图片')
            gif = QMovie('images_test/scan1.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear() # 清除画面
            #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
            self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
            self.label_result.setText('None')
            self.label_time.setText('0 s')
  
    def choose_video(self):
        #self.cap.release()
        self.flag=0
        self.timer_camera.stop()
        self.cap.release()
        self.label_face.clear()
        self.label_result.setText('  None')
        self.label_time.setText('0 s')
        #self.textEdit_camera.setText('实时摄像已关闭')
        self.label_outputResult.clear()
        #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
        self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
        # 使用文件选择对话框选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(
                                self.centralwidget, "选取视频文件",
                                self.path,  # 起始路径
                                "视频(*.avi;*.mov;*.mp4)") # 文件类型
        self.path = fileName_choose # 保存路径
        if fileName_choose != '':
            # 读取背景图
            #tmp = open('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png', 'wb')
            #tmp.write(b64decode(bgImg))
            #tmp.close()
            canvas = cv2.imread('images_test/slice.png')
            #remove('C:\\Users\\shuifan\\Desktop\\database\\images_test\\slice.png')

            self.capture=cv2.VideoCapture(fileName_choose)
            if self.timer_camera.isActive() == False:  # 检查定时状态
                QtWidgets.QApplication.processEvents()
                #self.textEdit_camera.setText('实时摄像已开启')
                self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                self.emotion_model = Emotion_Rec(self.model_path)
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
            else:
                # 选择取消，恢复界面状态
                # self.textEdit_pic1.setText('文件未选中')
                gif = QMovie('images_test/scan1.gif')
                self.label_face.setMovie(gif)
                gif.start()
                self.label_outputResult.clear()  # 清除画面
                #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
                self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
                self.label_result.setText('  None')
                self.label_time.setText('0 s')  # 界面处理
        else:
            # 选择取消，恢复界面状态
            #self.textEdit_pic1.setText('文件未选中')
            gif = QMovie('images_test/scan1.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear() # 清除画面
            #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
            self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
            self.label_result.setText('  None')
            self.label_time.setText('0 s')        # 界面处理        
        
    def cv_imread(self,filePath):
        # 读取图片
        cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
        ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
        ## cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
        return cv_img



    def choose_model(self):
        # 选择训练好的模型文件
        self.timer_camera.stop()
        self.cap.release()
        self.capture.release()
        self.label_face.clear()
        self.label_result.setText('None')
        self.label_time.setText('0 s')
        self.textEdit_camera.setText('实时摄像已关闭')
        self.label_outputResult.clear()
        #self.label_outputResult.setStyleSheet("border-image: url(:C:\\Users\\shuifan\\Desktop\\database\\images_test\\ini.png);")
        self.label_outputResult.setPixmap(QtGui.QPixmap("images_test/ini.png"))
        # 调用文件选择对话框
        fileName_choose, filetype = QFileDialog.getOpenFileName(self.centralwidget,
                                                                "选取图片文件", getcwd(), # 起始路径
                                                                "Model File (*.hdf5)")  # 文件类型
        # 显示提示信息
        if fileName_choose != '':
            self.model_path = fileName_choose
            self.textEdit_model.setText(fileName_choose+' 已选中')
        else:
            self.textEdit_model.setText('使用默认模型')

        # 恢复界面
        gif = QMovie('images_test/scan1.gif')
        self.label_face.setMovie(gif)
        gif.start()
        
    def compose(self):
        self.cp = SecondUi('chose_emotion')#将第一个窗口换个名字
        self.cp.show()#将第一个窗口显示出来        

         
    def  clear(self):
        for emotion in self.EMOTION:
            path=self.image_Path+"\\"+emotion
            for i in os.listdir(path):
                path_file=os.path.join(path,i)
                if os.path.isfile(path_file):
                    os.remove(path_file)
                else:
                    for f in os.listdir(path_file):
                        path_file2=os.join(path_file,f)
                        if os.path.isfile(path_file2):
                            os.remove(path_file2)
    def slot_btn_function(self,MainWindow):
        #self.hide()#隐藏此窗口
        self.f = FirstUi(MainWindow)#将第一个窗口换个名字
        self.f.show()#将第一个窗口显示出来