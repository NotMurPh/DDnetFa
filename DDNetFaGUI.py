from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import QPoint
import DDNetFa
import random


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName('MainWindow')
        self.setFixedSize(800, 220)

        self.setStyleSheet('''
        *:focus{
            outline: none;
        }

        QMainWindow{
            background-color: #222831;
            border:none;
        }

        #title_text{
            color: #eeeeee;
        }

        #exit_btn, #min_btn{
            color: white;
            border: none;
        }

        #min_btn:hover{
            background-color: #34343E;
        }

        #exit_btn:hover{
            background-color:#F20530;
        }

        #input_text{
            background-color: transparent;
            border: none;
            border-bottom: 2px solid #393e46;
            color: #eeeeee;
            padding-bottom: 5px;
        }
        
        #copy_btn{
            border: 2px solid #393e46;
            border-radius: 15px;
            background-color: transparent;
            color: #eeeeee;
        }

        #contact_text{
            color: #eeeeee;
        }''')

        font = QtGui.QFont()
        font.setFamily('IRANSansWeb')
        self.setFont(font)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate('MainWindow', 'DDNetFa'))
        self.setWindowIcon(QtGui.QIcon(r'Icons\DDNetFaIcon.svg'))
        self.setFocus()
        self.show()
        
        self.exit_btn = QtWidgets.QPushButton(self)
        self.exit_btn.setGeometry(QtCore.QRect(770,0,30,30))
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_btn.setObjectName('exit_btn')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r'Icons\close.svg'))
        self.exit_btn.setIcon(icon)
        self.exit_btn.clicked.connect(self.close)
        self.exit_btn.show()

        self.min_btn = QtWidgets.QPushButton(self)
        self.min_btn.setGeometry(QtCore.QRect(740,0,30,30))
        self.min_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_btn.setObjectName('min_btn')
        icon.addPixmap(QtGui.QPixmap(r'Icons\min.svg'))
        self.min_btn.setIcon(icon)
        self.min_btn.clicked.connect(self.showMinimized)
        self.min_btn.show()
        
        self.title_text = QtWidgets.QLabel(self)
        self.title_text.setGeometry(QtCore.QRect(12,12,393,20))
        self.title_text.setObjectName('title_text')
        font.setPointSize(8)
        self.title_text.setFont(font)
        self.title_text.setText(_translate('MainWindow', 'DDNetFa ~ Made by OmeGa'))
        self.title_text.show()

        self.input_text = QtWidgets.QLineEdit(self)
        self.input_text.setGeometry(QtCore.QRect(50, 95, 700, 30))
        font.setPointSize(10)
        self.input_text.setFont(font)
        self.input_text.setObjectName('input_text')
        self.input_text.setPlaceholderText(_translate('MainWindow', 'متن مورد نظر...'))
        self.input_text.textChanged.connect(self.ChangeBtnColor)
        self.input_text.show()

        self.copy_btn = QtWidgets.QPushButton(self)
        self.copy_btn.setGeometry(QtCore.QRect(315, 147, 170, 30))
        font.setPointSize(12)
        self.copy_btn.setFont(font)
        self.copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_btn.setObjectName('copy_btn')
        self.copy_btn.setText(_translate('MainWindow', 'کپی کن'))
        self.copy_btn.clicked.connect(self.CopyBtn)
        self.copy_btn.show()

        self.output_text = QtWidgets.QLabel(self)
        self.output_text.setGeometry(QtCore.QRect(630, 130, 120, 20))
        self.output_text.setObjectName('output_text')
        self.output_text.setText(_translate('MainWindow', 'متن شما با موفقت کپی شد'))
        
        down=-4
        right=15
        self.contact_text = QtWidgets.QLabel(self)
        self.contact_text.setGeometry(QtCore.QRect(264+right,196+down,272,20))
        self.contact_text.setObjectName('contact_text')
        font.setPointSize(8)
        self.contact_text.setFont(font)
        self.contact_text.setText(_translate('MainWindow', 'Z3Neuga        Omegatee.ir:8302        @PouyaCr72'))
        self.contact_text.show()

        self.discord_icon = QtWidgets.QLabel(self)
        self.discord_icon.setGeometry(QtCore.QRect(242+right,195+down,21,21))
        self.discord_icon.setObjectName('discord_icon')
        self.discord_icon.setPixmap(QtGui.QPixmap(r'Icons\Discord-Logo-White.svg'))
        self.discord_icon.setScaledContents(True)
        self.discord_icon.show()

        self.telegram_icon = QtWidgets.QLabel(self)
        self.telegram_icon.setGeometry(QtCore.QRect(435+right,197+down,15,15))
        self.telegram_icon.setObjectName('telegram_icon')
        self.telegram_icon.setPixmap(QtGui.QPixmap(r'Icons\telegram.svg'))
        self.telegram_icon.setScaledContents(True)
        self.telegram_icon.show()

        self.teeworlds_icon = QtWidgets.QLabel(self)
        self.teeworlds_icon.setGeometry(QtCore.QRect(316+right,196+down,17,17))
        self.teeworlds_icon.setObjectName('teeworlds_icon')
        self.teeworlds_icon.setPixmap(QtGui.QPixmap(r'Icons\teeworlds.svg'))
        self.teeworlds_icon.setScaledContents(True)
        self.teeworlds_icon.show()

        self.oldPos = self.pos()

    def ChangeBtnColor(self):
        if self.input_text.text() !='':
            self.copy_btn.setStyleSheet('border: 2px solid #d65a31;')
        else:
            self.copy_btn.setStyleSheet('border: 2px solid #393e46;')
            
    def CopyBtn(self):
        if self.input_text.text()!='':
            DDNetFa.Manager(self.input_text.text())
            self.input_text.setText('')
            self.output_text.show()
            self.output_text.setStyleSheet(f'color:rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)});font-family:IRANSansWeb;')

    def keyPressEvent(self,event):
        if event.key() == 16777220 or event.key() == 16777221:
            self.CopyBtn()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())