# -*- coding: utf-8 -*-
# Author:Fenn
# blog: fennbk.com
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,Qt
import qtawesome,sys,requests,imghdr,threading,os,requests,random,json
from PyQt5.QtGui import QMovie,QFont
from PyQt5.QtGui import  QPixmap,QIcon,QCursor
class QHead_Button(QPushButton):
    def __init__(self, *args):
        super(QHead_Button, self).__init__(*args)
        self.setFont(QFont("Webdings"))
        self.setFixedWidth(40)
class App_Compression(QtWidgets.QMainWindow):
    def __init__(self):
        super(App_Compression, self).__init__(None,Qt.FramelessWindowHint)
        self.resize(496, 445)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setObjectName('main_widget')
        self._TitleLabel = QLabel(chr(0xf23b) + '  图片压缩 V1.0',self.main_widget)
        self._TitleLabel.setFont(qtawesome.font('fa', 16))
        self._TitleLabel.setGeometry(10, 0, 400, 40)
        self._ClosButton = QHead_Button(b'\xef\x81\xb2'.decode("utf-8"), self.main_widget)
        self._ClosButton.setObjectName("ClosButton")
        self._ClosButton.move(self.width() - self._ClosButton.width() - 1, 0)
        self._MinimumButton = QHead_Button(b'\xef\x80\xb0'.decode("utf-8"), self.main_widget)
        self._MinimumButton.setObjectName("MinMaxButton")
        self._MinimumButton.move(self.width() - self._ClosButton.width() - 31, 0)
        self._MinimumButton.clicked.connect(self.showMinimized)
        self._ClosButton.clicked.connect(self.close)
        self.setAcceptDrops(True)
        self._MoveVarl = False
        # self.main_widget.setAcceptDrops(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 120))
        # self.label_3.setTextFormat(QtCore.Qt.PlainText)
        # self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        # self.label_3.setWordWrap(True)
        # self.label_3.setOpenExternalLinks(True)
        # self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 500))
        # self.label_2.setTextFormat(QtCore.Qt.PlainText)
        # self.label_2.setScaledContents(True)
        # self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        # self.label_2.setWordWrap(True)
        # self.label_2.setOpenExternalLinks(True)
        # self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setSpacing(36)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 5, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.setCentralWidget(self.main_widget)
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", "支持类型:PNG/jpg/文件夹\n拖拽到窗口开始压缩,文件不大于5M\n压缩多次可能会导致图片失帧，自行测试"))
        self.label_2.setStyleSheet('''
        color:#00CC33
        
        ''')
        photo = QPixmap()
        photo.loadFromData(requests.get('https://upload-images.jianshu.io/upload_images/17084873-926c0d1059be7461.png').content)
        self.label_2.setPixmap(photo)

        self.label.setText(_translate("Form", "警告：本工具仅限学习研究，不得用于商业用途。\nAuth：Fenn Blog:fennbk.com"))
        # self.checkBox.setChecked(True)
        self.label_4.setText(_translate("Form", "压缩"))
        self.label_5.setText(_translate("Form", "次"))
        self.setWindowTitle('图片压缩工具 V1.0')
        self.main_widget.setStyleSheet(''' 
            QWidget#main_widget{
            border-top-right-radius:10px;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            border-bottom-right-radius:10px;background-color: qlineargradient(spread:pad, x1:0.524597, y1:1, x2:0.524, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.0384615 rgba(216, 255, 249, 255), stop:0.387987 rgba(157, 248, 255, 255), stop:0.631494 rgba(156, 237, 255, 255), stop:1 rgba(112, 192, 255, 255));
            }
            QPushButton#ClosButton,QPushButton#MinMaxButton{
            color:#FFFFFF;
            border:0px;
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));
            }
            QPushButton#ClosButton:hover{
                color:#FF6347
            }
            QPushButton#MinMaxButton:hover {
                color:#848484
            }
            QLabel{              
                line-height: 1.5;
                color: #606c71;
                font-weight: normal;
                opacity: 0.7;
                font-size: 16px;
            }
                    ''')

    def dragEnterEvent(self, evn):

        self.look_exe=False
        if self.look_exe:return
        evn.accept()
    def dropEvent(self, evn):
        if os.path.isdir(evn.mimeData().text()[8:]):
            dir_list = evn.mimeData().text()[8:].replace('\\', '/').split('/')
            self.Lod_dir = dir_list[-1]
            self.New_dir = dir_list[-1] + '_压缩后'
            if not os.path.isdir('/'.join(dir_list[:-1])+'/'+self.New_dir):
                os.system('mkdir %s\%s'%('\\'.join(dir_list[:-1]),self.New_dir))
        threading.Thread(target=self.Thread_start,args=(evn.mimeData().text()[8:],)).start()
    def Thread_start(self,evn):
        self.label_2.setText('开始压缩.....')
        self.look_exe = True
        if os.path.isfile(evn):
            self.Re_cont(evn,True)
        else:
            self.Re_cont(evn, False)
        self.look_exe = False
    def Re_cont(self,pash,File):
        try:
            cont = int(self.spinBox.text())
        except:
            return
            # self.Request(evn)
        if File:
            Toola_size=os.path.getsize(pash)
            name = pash.replace('\\', '/').split('/')[-1]
            New_file = pash.replace(name, '压缩后_' + name)
            for item in range(0, cont):
                if item !=0:pash = New_file
                data = self.Request(pash)
                print(data)
                response = requests.get(data['output']['url'], headers={
                    "user-agent": data['User_Agent']})
                img = response.content
                with open(New_file, 'wb') as f:
                    f.write(img)

            self.label_2.setText('图片压缩前：%s\n图片压缩后: %s' % (self.set_resiz(Toola_size),self.set_resiz(os.path.getsize(New_file))))

        else:

            Total = self.dir_resiz(pash)
            for fpathe, dirs, fs in os.walk(pash):
                os.system('mkdir %s' % (fpathe.replace('/', '\\').replace(self.Lod_dir, self.New_dir)))
                for file in fs:
                    file = os.path.join(fpathe,file)
                    New_dir = file.replace(self.Lod_dir, self.New_dir)
                    for item in range(0, cont):
                        if item != 0: file = New_dir
                        data = self.Request(file)
                        print(data)
                        response = requests.get(data['output']['url'], headers={
                            "user-agent": data['User_Agent']})
                        print(file,New_dir)
                        with open(New_dir, 'wb') as f:
                            f.write(response.content)
            Total_new = self.dir_resiz(pash.replace(self.Lod_dir, self.New_dir))
            self.label_2.setText('文件夹压缩前：%s\n文件夹压缩后: %s'%(self.set_resiz(Total),self.set_resiz(Total_new)))
    def set_resiz(self,cont):
        if int(cont) > 1024:
            data = int(cont)//1024
            if data > 1024:
                return str(int(cont) // 1024) + ' M'
            else:
                return str(data) + ' KB'
        else:
            return str(cont) + ' 字节'
    def dir_resiz(self,pash):
        dir_Toola_size = 0
        for root, dirs, files in os.walk(pash):
            dir_Toola_size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return dir_Toola_size
    def Request(self,Picture):
        User_Agent = random.choice([
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        ])
        resp = requests.post('https://tinypng.com/web/shrink', data=(open(Picture, 'rb')).read(), headers={
            "user-agent":User_Agent})
        data = json.loads(resp.text)
        try:
            if data['error'] == 'Unsupported media type':
                self.label.setText('%s 文件，类型错误！'%Picture.replace('\\','/').split('/')[-1])
                return
        except:
            pass
        data['User_Agent'] = User_Agent
        return data
        # print(data['input'])
        # print(data['output'])
        # print(data['output']['url'])

    def mousePressEvent(self, event):
        if event.y() < 42:
            self._MoveVarl = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if self._MoveVarl:
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self._MoveVarl = False
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = App_Compression()

    gui.show()
    sys.exit(app.exec_())