from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QCompleter
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox, QScrollArea, QWidget, QApplication 
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import sqlite3
import random
import os

from kalorihesapla import hesapla_kalori
import kullanici_veritabani
from yemeklistesi import kahvalti, aksam, ogle, ara_ogun
import foods

#Ana ekranın sınıfı ve fonksiyonları
class Ui_MainWindow(object):
 

    def setupUi(self, MainWindow):
        
        global veri
        veri = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1255, 740)
        MainWindow.setFixedSize(1255, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kalorigroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.kalorigroupbox.setGeometry(QtCore.QRect(250, 80, 431, 251))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kalorigroupbox.setFont(font)
        self.kalorigroupbox.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"font: 10pt \"Sans Serif Collection\",#191A1F;\n"
"")
        
        self.kalorigroupbox.setObjectName("kalorigroupbox")
        self.besinlineedit = QtWidgets.QLineEdit(self.kalorigroupbox)
        self.besinlineedit.setGeometry(QtCore.QRect(20, 60, 231, 31))
        self.besinlineedit.setObjectName("besinlineedit")

        # QCompleter ile lineeditte verileri göster
        completer = QtWidgets.QCompleter(foods.veriler)      
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)   
        self.besinlineedit.setCompleter(completer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.besinlineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.besinlineedit.setObjectName("besinlineedit")
        self.besingramlineedit = QtWidgets.QLineEdit(self.kalorigroupbox)
        self.besingramlineedit.setGeometry(QtCore.QRect(20, 110, 231, 31))
        self.besingramlineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.besingramlineedit.setObjectName("besingramlineedit")
        self.kaloritakipkaydetbuton = QtWidgets.QPushButton(self.kalorigroupbox)
        self.kaloritakipkaydetbuton.setGeometry(QtCore.QRect(280, 160, 91, 31))
        self.kaloritakipkaydetbuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.kaloritakipkaydetbuton.setObjectName("kaloritakipkaydetbuton")
        self.sumiktarilineedit_4 = QtWidgets.QLineEdit(self.kalorigroupbox)
        self.sumiktarilineedit_4.setGeometry(QtCore.QRect(20, 160, 231, 31))
        self.sumiktarilineedit_4.setMouseTracking(False)
        self.sumiktarilineedit_4.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: #FF6436;\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.sumiktarilineedit_4.setReadOnly(True)
        self.sumiktarilineedit_4.setPlaceholderText("")
        self.sumiktarilineedit_4.setObjectName("sumiktarilineedit_4")
        self.besiyuzdeprogressBar = QtWidgets.QProgressBar(self.kalorigroupbox)
        self.besiyuzdeprogressBar.setGeometry(QtCore.QRect(20, 210, 351, 31))
        self.besiyuzdeprogressBar.setStyleSheet("\n"
"QProgressBar::chunk {\n"
"  background-color: #D5ECFA; /* Progress bar doluluğu için renk */\n"
"\n"
" border-radius: 2px;  /* Dolu kısmın köşelerini yuvarlayalım */\n"
" /*background-color: #4CAF50;   Dolu kısım rengi */\n"
"  \n"
"            }\n"
"            QProgressBar {\n"
"                text-align: center;  /* Metni ortala */\n"
"            }\n"
"")
        self.besiyuzdeprogressBar.setProperty("value", 0)
        self.besiyuzdeprogressBar.setOrientation(QtCore.Qt.Horizontal)
        self.besiyuzdeprogressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.besiyuzdeprogressBar.setObjectName("besiyuzdeprogressBar")
        self.alnankalorilabel = QtWidgets.QLabel(self.kalorigroupbox)
        self.alnankalorilabel.setGeometry(QtCore.QRect(140, 160, 91, 31))
        self.alnankalorilabel.setStyleSheet("background-color: transparent;")
        self.alnankalorilabel.setObjectName("alnankalorilabel")
        self.egzersizgroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.egzersizgroupbox.setGeometry(QtCore.QRect(770, 80, 431, 251))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.egzersizgroupbox.setFont(font)
        self.egzersizgroupbox.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"font: 10pt \"Sans Serif Collection\",#191A1F;")
        self.egzersizgroupbox.setObjectName("egzersizgroupbox")
        self.sporcomboBox = QtWidgets.QComboBox(self.egzersizgroupbox)
        self.sporcomboBox.setGeometry(QtCore.QRect(70, 70, 291, 31))
        self.sporcomboBox.setStyleSheet("QComboBox { \n"
"    border: 1px solid #333333;\n"
"    border-radius: 5px;\n"
"    background-color:#D5ECFA;\n"
"    padding-left:7px;\n"
"    min-width: 6em;\n"
"    color: #191A1F;;\n"
"    }\n"
"QComboBox QAbstractItemView{\n"
"    background-color: #D5ECFA;\n"
"    color: #D5ECFA;\n"
" \n"
"    selection-background-color:  rgb(87, 101, 241);\n"
"    selection-color: #FEFEFE;\n"
"    \n"
"    \n"
"    font-size: 16px;\n"
"\n"
"    color: black;\n"
"}")
        self.sporcomboBox.setPlaceholderText("")
        self.sporcomboBox.setObjectName("sporcomboBox")
        self.sporcomboBox.addItem("")
        self.sporcomboBox.addItem("")
        self.sporcomboBox.addItem("")
        self.sporcomboBox.addItem("")
        self.sporcomboBox.addItem("")
        self.spordklineEdit = QtWidgets.QLineEdit(self.egzersizgroupbox)
        self.spordklineEdit.setGeometry(QtCore.QRect(120, 120, 181, 31))
        self.spordklineEdit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.spordklineEdit.setObjectName("spordklineEdit")
        self.sporkaydetbuton = QtWidgets.QPushButton(self.egzersizgroupbox)
        self.sporkaydetbuton.setGeometry(QtCore.QRect(160, 170, 93, 31))
        self.sporkaydetbuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.sporkaydetbuton.setObjectName("sporkaydetbuton")
        self.sumiktarilineedit_3 = QtWidgets.QLineEdit(self.egzersizgroupbox)
        self.sumiktarilineedit_3.setGeometry(QtCore.QRect(120, 210, 181, 31))
        self.sumiktarilineedit_3.setMouseTracking(False)
        self.sumiktarilineedit_3.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: #FF6436;\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.sumiktarilineedit_3.setReadOnly(True)
        self.sumiktarilineedit_3.setPlaceholderText("")
        self.sumiktarilineedit_3.setObjectName("sumiktarilineedit_3")
        self.sporkalori = QtWidgets.QLabel(self.egzersizgroupbox)
        self.sporkalori.setGeometry(QtCore.QRect(220, 210, 81, 31))
        self.sporkalori.setStyleSheet("background-color: transparent;")
        self.sporkalori.setObjectName("sporkalori")
        self.sutakipgroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.sutakipgroupbox.setGeometry(QtCore.QRect(250, 380, 431, 251))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sutakipgroupbox.setFont(font)
        self.sutakipgroupbox.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"font: 10pt \"Sans Serif Collection\",#191A1F;")
        self.sutakipgroupbox.setObjectName("sutakipgroupbox")
        self.sueklelineedit = QtWidgets.QLineEdit(self.sutakipgroupbox)
        self.sueklelineedit.setGeometry(QtCore.QRect(20, 70, 231, 31))
        self.sueklelineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.sueklelineedit.setObjectName("sueklelineedit")
        self.sueklebuton = QtWidgets.QPushButton(self.sutakipgroupbox)
        self.sueklebuton.setGeometry(QtCore.QRect(280, 70, 93, 31))
        self.sueklebuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.sueklebuton.setObjectName("sueklebuton")
        self.sumiktarilineedit_2 = QtWidgets.QLineEdit(self.sutakipgroupbox)
        self.sumiktarilineedit_2.setGeometry(QtCore.QRect(20, 130, 231, 31))
        self.sumiktarilineedit_2.setMouseTracking(False)
        self.sumiktarilineedit_2.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: #FF6436;\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.sumiktarilineedit_2.setReadOnly(True)
        self.sumiktarilineedit_2.setPlaceholderText("")
        self.sumiktarilineedit_2.setObjectName("sumiktarilineedit_2")
        self.sporkalori_2 = QtWidgets.QLabel(self.sutakipgroupbox)
        self.sporkalori_2.setGeometry(QtCore.QRect(170, 130, 81, 31))
        self.sporkalori_2.setStyleSheet("background-color: transparent;")
        self.sporkalori_2.setObjectName("sporkalori_2")
        self.suyuzdebar = QtWidgets.QProgressBar(self.sutakipgroupbox)
        self.suyuzdebar.setGeometry(QtCore.QRect(20, 190, 351, 31))
        self.suyuzdebar.setStyleSheet("\n"
"QProgressBar::chunk {\n"
"  background-color: #D5ECFA; /* Progress bar doluluğu için renk */\n"
"\n"
" border-radius: 2px;  /* Dolu kısmın köşelerini yuvarlayalım */\n"
" /*background-color: #4CAF50;   Dolu kısım rengi */\n"
"  \n"
"            }\n"
"            QProgressBar {\n"
"                text-align: center;  /* Metni ortala */\n"
"            }\n"
"")
        self.suyuzdebar.setProperty("value", 0)
        self.suyuzdebar.setOrientation(QtCore.Qt.Horizontal)
        self.suyuzdebar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.suyuzdebar.setObjectName("suyuzdebar")
        self.diyetlistesigroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.diyetlistesigroupbox.setGeometry(QtCore.QRect(770, 380, 421, 251))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.diyetlistesigroupbox.setFont(font)
        self.diyetlistesigroupbox.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"font: 10pt \"Sans Serif Collection\",#191A1F;")
        self.diyetlistesigroupbox.setObjectName("diyetlistesigroupbox")
        self.diyetlistesioluturebuton = QtWidgets.QPushButton(self.diyetlistesigroupbox)
        self.diyetlistesioluturebuton.setGeometry(QtCore.QRect(110, 100, 171, 51))
        self.diyetlistesioluturebuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.diyetlistesioluturebuton.setObjectName("diyetlistesioluturebuton")
        self.kullanicibilgilerigrup = QtWidgets.QGroupBox(self.centralwidget)
        self.kullanicibilgilerigrup.setGeometry(QtCore.QRect(20, 80, 201, 551))
        self.kullanicibilgilerigrup.setStyleSheet("background-color :rgb(254, 254, 254);\n"
"font: 10pt \"Sans Serif Collection\",#191A1F;\n"
"")
        self.kullanicibilgilerigrup.setObjectName("kullanicibilgilerigrup")
        self.kullaniciismilineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
      
        self.kullaniciismilineedit.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.kullaniciismilineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullaniciismilineedit.setPlaceholderText("")
        self.kullaniciismilineedit.setObjectName("kullaniciismilineedit")
        self.kullaniciyaslineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullaniciyaslineedit.setGeometry(QtCore.QRect(10, 110, 171, 31))
        self.kullaniciyaslineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullaniciyaslineedit.setPlaceholderText("")
        self.kullaniciyaslineedit.setObjectName("kullaniciyaslineedit")
        self.kullaniciboylineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullaniciboylineedit.setGeometry(QtCore.QRect(10, 160, 171, 31))
        self.kullaniciboylineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullaniciboylineedit.setPlaceholderText("")
        self.kullaniciboylineedit.setObjectName("kullaniciboylineedit")
        self.kullanicicinsiyetlineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullanicicinsiyetlineedit.setGeometry(QtCore.QRect(10, 260, 171, 31))
        self.kullanicicinsiyetlineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullanicicinsiyetlineedit.setPlaceholderText("")
        self.kullanicicinsiyetlineedit.setObjectName("kullanicicinsiyetlineedit")
        self.kullanicikilolineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullanicikilolineedit.setGeometry(QtCore.QRect(10, 210, 171, 31))
        self.kullanicikilolineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullanicikilolineedit.setPlaceholderText("")
        self.kullanicikilolineedit.setObjectName("kullanicikilolineedit")
        self.kullaniciaktivitelineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullaniciaktivitelineedit.setGeometry(QtCore.QRect(10, 310, 171, 31))
        self.kullaniciaktivitelineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullaniciaktivitelineedit.setPlaceholderText("")
        self.kullaniciaktivitelineedit.setObjectName("kullaniciaktivitelineedit")
        self.kullanicihedeflineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullanicihedeflineedit.setGeometry(QtCore.QRect(10, 360, 171, 31))
        self.kullanicihedeflineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullanicihedeflineedit.setPlaceholderText("")
        self.kullanicihedeflineedit.setObjectName("kullanicihedeflineedit")
        self.kullanicikalorilineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullanicikalorilineedit.setGeometry(QtCore.QRect(10, 410, 171, 31))
        self.kullanicikalorilineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullanicikalorilineedit.setPlaceholderText("")
        self.kullanicikalorilineedit.setObjectName("kullanicikalorilineedit")
        self.kullanicisumiktarilineedit = QtWidgets.QLineEdit(self.kullanicibilgilerigrup)
        self.kullanicisumiktarilineedit.setGeometry(QtCore.QRect(10, 460, 171, 31))
        self.kullanicisumiktarilineedit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.kullanicisumiktarilineedit.setPlaceholderText("")
        self.kullanicisumiktarilineedit.setObjectName("kullanicisumiktarilineedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        #Kullanıcı bilgilerini göstermek

        connection = sqlite3.connect("kullanici_veritabani.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=?", (isim,))
        veri = cursor.fetchone()  
        
        self.kullaniciismilineedit.setText("Kullanıcı Adı: "+isim)
        self.kullaniciyaslineedit.setText("Yaşınız: "+str(veri[3]))
        self.kullaniciboylineedit.setText("Boyunuz: "+str(veri[4])+" cm")
        self.kullanicikilolineedit.setText("Kilonuz: "+str(veri[5])+" kg")
        self.kullanicicinsiyetlineedit.setText("Cinsiyetiniz: "+str(veri[6]))
        self.kullaniciaktivitelineedit.setText("Aktivite Düzeyiniz: "+str(veri[7]))
        self.kullanicihedeflineedit.setText("Hedefiniz: "+str(veri[8]))
        self.kullanicikalorilineedit.setText("Günlük Kalori: "+str(veri[9])+" kcal")
        self.kullanicisumiktarilineedit.setText("Günlük Su: "+str(veri[10])+" ml")
        
        self.kullaniciismilineedit.setReadOnly(True)
        self.kullaniciyaslineedit.setReadOnly(True)
        self.kullaniciboylineedit.setReadOnly(True)
        self.kullanicikilolineedit.setReadOnly(True)
        self.kullanicicinsiyetlineedit.setReadOnly(True)
        self.kullaniciaktivitelineedit.setReadOnly(True)
        self.kullanicihedeflineedit.setReadOnly(True)
        self.kullanicikalorilineedit.setReadOnly(True)
        self.kullanicisumiktarilineedit.setReadOnly(True)
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
       
        
        self.kaloritakipkaydetbuton.clicked.connect(self.kalori_takip_kaydet)
        self.sporkaydetbuton.clicked.connect(self.egzersiz_kaydet)
        self.sueklebuton.clicked.connect(self.su_takip_ekle)
        self.diyetlistesioluturebuton.clicked.connect(self.diyet_listesi_olustur)
   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diyet"))
        self.kalorigroupbox.setTitle(_translate("MainWindow", "Kalori takip"))
        self.besinlineedit.setPlaceholderText(_translate("MainWindow", "Besin"))
        self.besingramlineedit.setPlaceholderText(_translate("MainWindow", "00 gram"))
        self.kaloritakipkaydetbuton.setText(_translate("MainWindow", "Ekle"))
        self.sumiktarilineedit_4.setText(_translate("MainWindow", "Alınan Kalori:"))
        self.alnankalorilabel.setText(_translate("MainWindow", "00"))
        self.egzersizgroupbox.setTitle(_translate("MainWindow", "Egzersiz"))
        self.sporcomboBox.setCurrentText(_translate("MainWindow", "Egzersiz"))
        self.sporcomboBox.setItemText(0, _translate("MainWindow", "Egzersiz"))
        self.sporcomboBox.setItemText(1, _translate("MainWindow", "Yürüyüş"))
        self.sporcomboBox.setItemText(2, _translate("MainWindow", "Koşu"))
        self.sporcomboBox.setItemText(3, _translate("MainWindow", "Bisiklet sürme"))
        self.sporcomboBox.setItemText(4, _translate("MainWindow", "Yüzme"))
        self.spordklineEdit.setPlaceholderText(_translate("MainWindow", "00 dk"))
        self.sporkaydetbuton.setText(_translate("MainWindow", "Kaydet"))
        self.sumiktarilineedit_3.setText(_translate("MainWindow", "Yakılan Kalori:"))
        self.sporkalori.setText(_translate("MainWindow", "00"))
        self.sutakipgroupbox.setTitle(_translate("MainWindow", "Su takip"))
        self.sueklelineedit.setPlaceholderText(_translate("MainWindow", "00 ml"))
        self.sueklebuton.setText(_translate("MainWindow", "Ekle"))
        self.sumiktarilineedit_2.setText(_translate("MainWindow", "İçilen Su Miktarı:"))
        self.sporkalori_2.setText(_translate("MainWindow", "00"))
        self.diyetlistesigroupbox.setTitle(_translate("MainWindow", "Diyet listesi"))
        self.diyetlistesioluturebuton.setText(_translate("MainWindow", "Diyet Listesi Oluştur"))
        self.kullanicibilgilerigrup.setTitle(_translate("MainWindow", "Kullanıcı Bilgileri"))
   

    def kalori_takip_kaydet(self):
       #kaloriyi alıp toplar her besinin kalorisini toplam kaloriye ekler
      toplam_kalori = float(self.alnankalorilabel.text()) if self.alnankalorilabel.text() else 0 
      besinadi = self.besinlineedit.text()
      for besin in foods.veriler:
          if besinadi == besin:
              kalori = foods.veriler[besinadi]
              gramkalori = kalori / 100
              alinangram = int(self.besingramlineedit.text())
              sonkalori = gramkalori * alinangram
              toplam_kalori += sonkalori  
      self.alnankalorilabel.setText("{:.2f}".format(toplam_kalori))
      self.besin_progress_bar()
      QMessageBox.information(None, "Bilgi", f"Alınan kalori: {sonkalori:.2f}")
      pass
    def besin_progress_bar(self):
        # besin progress barın ilerlemesini sağlayan fonksiyon
        try:
            
            connection = sqlite3.connect("kullanici_veritabani.db")
            cursor = connection.cursor()
            cursor.execute("SELECT günlükkalori FROM kullanicilar WHERE kullaniciadi=?", (isim,))
            print(isim)
          
            maksimum_kalori1 =cursor.fetchone()
            print(maksimum_kalori1)

            maksimum_kalori=maksimum_kalori1[0]
            toplam_kalori=float(self.alnankalorilabel.text())

            yuzde = (toplam_kalori * 100) / maksimum_kalori

            if yuzde >=100:
                self.besiyuzdeprogressBar.setValue(int(100))
            else :
                self.besiyuzdeprogressBar.setValue(int(yuzde))
        except Exception as e:
            QMessageBox.warning(None, "Uyarı", f"Bir hata oluştu: {str(e)}")

    def egzersiz_kaydet(self):
    # Kullanıcının seçtiği spor türüne ve süreye göre kalori hesaplayan fonk.
      spor = self.sporcomboBox.currentText()
      sure = float(self.spordklineEdit.text()) if self.spordklineEdit.text() else 0
      
      # Spor türleri ve kalori değerlerini içeren bir sözlük
      sporlar_kalori = {
          "Yürüyüş": 4,
          "Koşu": 10,
          "Bisiklet sürme": 8,
          "Yüzme": 11
         
      }
  
      toplam_kalori = float(self.sporkalori.text()) if self.sporkalori.text() else 0
  
      if spor in sporlar_kalori:
          kalori = sporlar_kalori[spor]
          toplam_kalori += sure * kalori
    

      print("Toplam Kalori:", toplam_kalori)
 
      QMessageBox.information(None, "Bilgi", f"Yakılan kalori: {sure*kalori:.2f}")
      self.sporkalori.setText(str(toplam_kalori))

    def su_takip_ekle(self):
        # su miktarını takip eden fonk.
        try:
         
            suMl = float(self.sueklelineedit.text())  
            suMl += float(self.sporkalori_2.text())
            self.sporkalori_2.setText(str(suMl))
            self.update_progress_bar()
        except ValueError:
            # Geçersiz sayı girildiğinde uyarı
            QMessageBox.warning(None, "Uyarı", "Lütfen geçerli bir sayı girin.")
        pass
     
    def update_progress_bar(self):
        #su progress barın ilerlemesini sağlayan fonk.
        try:
            connection = sqlite3.connect("kullanici_veritabani.db")
            cursor = connection.cursor()
            cursor.execute("SELECT sumiktarı FROM kullanicilar WHERE kullaniciadi=?", (isim,))
            sumiktarı_tuple = cursor.fetchone() 
            connection.close()
           
            if sumiktarı_tuple is not None:
                # Kullanıcının girdiği su miktarını al
                sumiktarı = sumiktarı_tuple[0]  # Tuple'ın  elemanını al
                print(sumiktarı)
                su = float(self.sporkalori_2.text())
                yuzde = (su * 100) / sumiktarı   
                # İlerleme çubuğunu güncelle
                if yuzde >=100 :
                    
                    self.suyuzdebar.setValue(int(100))
                else :
                    self.suyuzdebar.setValue(int(yuzde))


            else:
                # Veritabanında kayıt bulunamazsa uyarı göster
                QMessageBox.warning(None, "Uyarı", "Kullanıcı veritabanında kayıt bulunamadı.")
        except sqlite3.Error as e:
            # Veritabanı hatasını konsola yazdır
            print("SQLite hatası:", e)
   
    def listeyiolustur(self,kalori_ihtiyaci_range, yiyecek_listesi):
        #diyet listesini hazırlayan fonk.
        self.diyetlistesioluturebuton.hide()
        min_kalori, max_kalori = kalori_ihtiyaci_range
       
        kalori_ihtiyaci = random.randrange(int(min_kalori), int(max_kalori))

        kalan_kalori = kalori_ihtiyaci
        diyet_planı = []
        kullanilan_yiyecekler = set()
    
        while kalan_kalori > 0 and yiyecek_listesi:
            yiyecek = random.choice(yiyecek_listesi)
            if yiyecek["isim"] in kullanilan_yiyecekler:
                continue  
            miktar = random.randint(50, 100) 
            yiyecek_kalori = miktar * yiyecek["kalori"]
    
            if yiyecek_kalori <= kalan_kalori:
                diyet_planı.append({"isim": yiyecek["isim"], "miktar": miktar})
                kalan_kalori -= yiyecek_kalori
                kullanilan_yiyecekler.add(yiyecek["isim"])
            else:
                break  
            yiyecek_listesi = [item for item in yiyecek_listesi if item["isim"] not in kullanilan_yiyecekler]
    
        return diyet_planı


    
    def diyet_listesi_olustur(self):
      
    
        kahvaltı_listesi = [{"isim": isim, "kalori": kalori / 100.0} for isim, kalori in kahvalti.items()]
        ogle_listesi = [{"isim": isim, "kalori": kalori / 100.0} for isim, kalori in ogle.items()]
        aksam_listesi = [{"isim": isim, "kalori": kalori / 100.0} for isim, kalori in aksam.items()]
        aragun_listesi = [{"isim": isim, "kalori": kalori / 100.0} for isim, kalori in ara_ogun.items()]
        günlük_kalori= int(veri[9])
        kahvaltı_gerekli_kalori=int(günlük_kalori*0.25)
        ogle_gerekli_kalori=int(günlük_kalori*0.30)
        aksam_gerekli_kalori=int(günlük_kalori*0.30)
        ara_ogun_gerekli_kalori=int(günlük_kalori*0.15)
        print(günlük_kalori)
        kahvaltı_kalori_ihtiyaci =((kahvaltı_gerekli_kalori)-100,(kahvaltı_gerekli_kalori)+100)
        ogle_kalori_ihtiyaci =((ogle_gerekli_kalori)-100,(ogle_gerekli_kalori)+100) 
        aksam_kalori_ihtiyaci = ((aksam_gerekli_kalori)-100,(aksam_gerekli_kalori)+100)
        ara_kalori_ihtiyaci = ((ara_ogun_gerekli_kalori)-100,(ara_ogun_gerekli_kalori)+100)
    
        kahvaltı_planı = self.listeyiolustur(kahvaltı_kalori_ihtiyaci, kahvaltı_listesi)
        ogle_planı = self.listeyiolustur(ogle_kalori_ihtiyaci, ogle_listesi)
        aksam_planı = self.listeyiolustur(aksam_kalori_ihtiyaci, aksam_listesi)
        ara_planı = self.listeyiolustur(ara_kalori_ihtiyaci, aragun_listesi)
    
       
        diyet_layout = QVBoxLayout()
    
        # Kahvaltı planı
        diyet_layout.addWidget(QLabel("Kahvaltı Planı:"))
        kahvalti_listview = QListWidget()
        for yiyecek in kahvaltı_planı:
            kahvalti_listview.addItem(QListWidgetItem(f"{yiyecek['isim']}: {yiyecek['miktar']} gram"))
        diyet_layout.addWidget(kahvalti_listview)
    
        # Öğle planı
        diyet_layout.addWidget(QLabel("Öğle Planı:"))
        ogle_listview = QListWidget()
        for yiyecek in ogle_planı:
            ogle_listview.addItem(QListWidgetItem(f"{yiyecek['isim']}: {yiyecek['miktar']} gram"))
        diyet_layout.addWidget(ogle_listview)
    
        # Akşam planı
        diyet_layout.addWidget(QLabel("Akşam Planı:"))
        aksam_listview = QListWidget()
        for yiyecek in aksam_planı:
            aksam_listview.addItem(QListWidgetItem(f"{yiyecek['isim']}: {yiyecek['miktar']} gram"))
        diyet_layout.addWidget(aksam_listview)
    
        # Ara öğün planı
        diyet_layout.addWidget(QLabel("Ara Öğün Planı:"))
        ara_listview = QListWidget()
        for yiyecek in ara_planı:
            ara_listview.addItem(QListWidgetItem(f"{yiyecek['isim']}: {yiyecek['miktar']} gram"))
        diyet_layout.addWidget(ara_listview)
       
        #diyet listesinin içinde göster     
               
        scrollContentWidget = QtWidgets.QWidget()
        scrollContentWidget.setLayout(diyet_layout)
        
      
        scrollArea = QtWidgets.QScrollArea(self.diyetlistesigroupbox)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scrollArea.setWidget(scrollContentWidget)
        
      
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(scrollArea)
        self.diyetlistesigroupbox.setLayout(layout)


# Giriş ekranının sınıfı ve fonksiyonları

class Ui_anagirisekrani(object):

    global isim 
    isim = None
    def setupUi(self, anagirisekrani):
       
        
        anagirisekrani.setObjectName("anagirisekrani")
        anagirisekrani.setEnabled(True)
        anagirisekrani.resize(733, 632)
        anagirisekrani.setFixedSize(733, 632) 
        anagirisekrani.setStyleSheet("background-color: #f4f4f4;")
        anagirisekrani.setWindowTitle("Giriş")
        self.kullaniciadi = QtWidgets.QLineEdit(anagirisekrani)
        self.kullaniciadi.setGeometry(QtCore.QRect(239, 230, 271, 40))
        self.kullaniciadi.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")

        self.kullaniciadi.setText("")
        self.kullaniciadi.setObjectName("kullaniciadi")
        self.lineEdit = QtWidgets.QLineEdit(anagirisekrani)
        self.lineEdit.setGeometry(QtCore.QRect(239, 300, 271, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"color:#191A1F;\n"
"font: 9pt \"Sans Serif Collection\";\n"
"background-color: rgb(213, 236, 250);\n"
"border:rgb(48,50,62);\n"
"padding-left:5px;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit:Hover{\n"
"border:rgb(48,50,62);}\n"
"QLineEdit:Focus{\n"
"border:rgb(85,170,255);}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.girisekranilabel = QtWidgets.QLabel(anagirisekrani)
        self.girisekranilabel.setGeometry(QtCore.QRect(250, 120, 250, 70))
        self.girisekranilabel.setStyleSheet("font: 20pt \"Sans Serif Collection\",#191A1F;\n"
"background-color:#f4f4f4;")

        self.girisekranilabel.setObjectName("girisekranilabel")
        self.kayitolbuton = QtWidgets.QPushButton(anagirisekrani)
        self.kayitolbuton.setGeometry(QtCore.QRect(240, 370, 121, 41))
        self.kayitolbuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.kayitolbuton.setObjectName("kayitolbuton")
        self.girisyapbuton = QtWidgets.QPushButton(anagirisekrani)
        self.girisyapbuton.setGeometry(QtCore.QRect(390, 370, 121, 41))
        self.girisyapbuton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.girisyapbuton.setObjectName("girisyapbuton")
        self.kayitolbuton.clicked.connect(self.kayit_ol)
        self.girisyapbuton.clicked.connect(self.giris_yap)
        self.retranslateUi(anagirisekrani)
        QtCore.QMetaObject.connectSlotsByName(anagirisekrani)
    

    def retranslateUi(self, anagirisekrani):
        _translate = QtCore.QCoreApplication.translate
        self.kullaniciadi.setPlaceholderText(_translate("anagirisekrani", "Kullanıcı Adı"))
        self.lineEdit.setPlaceholderText(_translate("anagirisekrani", "Şifre"))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.girisekranilabel.setText(_translate("anagirisekrani", "<html><head/><body><p align=\"center\">  Hoş geldiniz!</p></body></html>"))

        self.kayitolbuton.setText(_translate("anagirisekrani", "Kayıt Ol"))
        self.girisyapbuton.setText(_translate("anagirisekrani", "Giriş Yap"))
    
    
    def kayit_ol(self):
        global isim
        isim = self.kullaniciadi.text()
        sifre = self.lineEdit.text()
        conn = sqlite3.connect('kullanici_veritabani.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi = ?", (isim,))
        kullaniciadi_check = cursor.fetchone()
        if kullaniciadi_check:
           QMessageBox.warning(None, "Uyarı", "Bu kullanıcı adı zaten kayıtlı.")
            
        else:
            cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre) VALUES (?, ?)", (isim, sifre))
            conn.commit()
            print("Kayıt başarıyla tamamlandı.")
            
            self.open_dialog()
            anagirisekrani.hide()
        
        conn.close()

    def giris_yap(self):
        global isim
           

        isim = self.kullaniciadi.text()
        sifre = self.lineEdit.text()

        conn = sqlite3.connect("kullanici_veritabani.db")
        cursor = conn.cursor()
        
        # Kullanıcı adı ve şifre doğruluğunu kontrol
        cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciadi=? AND sifre=?", (isim, sifre))
        kullanici = cursor.fetchone()
        conn.close()
        
        if kullanici:
            
            QMessageBox.information(None, "Başarılı", "Giriş başarılı, hoş geldiniz {}!".format(isim))
            self.open_main_window()
            anagirisekrani.hide()

        else:
            QMessageBox.warning(None, "Uyarı", "Kullanıcı adı veya şifre hatalı.")
        return isim
    
     #Ana sayfayı açan fonk.
    def open_main_window(self):
     
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.main_window)
        self.main_window.show()
        
     
   #kayıt ekranını açan fonk.
    def open_dialog(self):
        self.dialog = QtWidgets.QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)
        self.dialog.show() 
        global kayıtekran
        kayıtekran = self.dialog


# Kayıt ekranının sınıfı ve fonksiyonları 

class Ui_Dialog(object):
    global son_kullanici
    son_kullanici = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 632)
        Dialog.setFixedSize(733, 632) 
        Dialog.setStyleSheet("background-color: #f4f4f4;")
        self.kilolinedit = QtWidgets.QLineEdit(Dialog)
        self.kilolinedit.setGeometry(QtCore.QRect(60, 350, 251, 51))
        self.kilolinedit.setStyleSheet("background-color:#d5ecfa;\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"font: 10pt \"Sans Serif Collection\";\n"
"padding-left:5px;\n"
"color: #191a1f;")
        self.kilolinedit.setText("")
        self.kilolinedit.setObjectName("kilolinedit")
        self.boylineedit = QtWidgets.QLineEdit(Dialog)
        self.boylineedit.setGeometry(QtCore.QRect(60, 230, 251, 51))
        self.boylineedit.setStyleSheet("background-color: #d5ecfa;\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"font: 10pt \"Sans Serif Collection\";\n"
"padding-left:5px;\n"
"color:  #191a1f;")
        self.boylineedit.setText("")
        self.boylineedit.setObjectName("boylineedit")
        self.yaslinedit = QtWidgets.QLineEdit(Dialog)
        self.yaslinedit.setGeometry(QtCore.QRect(60, 110, 251, 51))
        self.yaslinedit.setStyleSheet("background-color:#d5ecfa;\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"font: 10pt \"Sans Serif Collection\";\n"
"padding-left:5px;\n"
"color:  #191a1f;")
        self.yaslinedit.setText("")
        self.yaslinedit.setObjectName("yaslinedit")
        self.cinsiyetcombobox = QtWidgets.QComboBox(Dialog)
        self.cinsiyetcombobox.setGeometry(QtCore.QRect(430, 110, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.cinsiyetcombobox.setFont(font)
        self.cinsiyetcombobox.setMouseTracking(False)
        self.cinsiyetcombobox.setStyleSheet("QComboBox { \n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background-color:#d5ecfa;\n"
"    padding-left:5px;\n"
"    min-width: 6em;\n"
"    color: #191a1f;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color: #016837;\n"
"    color: #4f4f4f;\n"
"    selection-background-color: #f5efe6;\n"
"    selection-color: #666699;\n"
"    font-family: \"Consolas\";\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.cinsiyetcombobox.setPlaceholderText("")
        self.cinsiyetcombobox.setObjectName("cinsiyetcombobox")
        self.cinsiyetcombobox.addItem("")
        self.cinsiyetcombobox.addItem("")
        self.cinsiyetcombobox.addItem("")
        self.hareketcombobox = QtWidgets.QComboBox(Dialog)
        self.hareketcombobox.setGeometry(QtCore.QRect(430, 230, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.hareketcombobox.setFont(font)
        self.hareketcombobox.setMouseTracking(False)
        self.hareketcombobox.setStyleSheet("QComboBox { \n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background-color:#d5ecfa;\n"
"    padding-left:5px;\n"
"    min-width: 6em;\n"
"    color: #191a1f;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color: #016837;\n"
"    color: #4f4f4f;\n"
"    selection-background-color: #f5efe6;\n"
"    selection-color: #666699;\n"
"    font-family: \"Consolas\";\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.hareketcombobox.setPlaceholderText("")
        self.hareketcombobox.setObjectName("hareketcombobox")
        self.hareketcombobox.addItem("")
        self.hareketcombobox.addItem("")
        self.hareketcombobox.addItem("")
        self.hareketcombobox.addItem("")
        self.hareketcombobox.addItem("")
        self.hareketcombobox.addItem("")
        self.hedefcombobox = QtWidgets.QComboBox(Dialog)
        self.hedefcombobox.setGeometry(QtCore.QRect(430, 350, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.hedefcombobox.setFont(font)
        self.hedefcombobox.setMouseTracking(False)
        self.hedefcombobox.setStyleSheet("QComboBox { \n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    background-color:#d5ecfa;\n"
"    padding-left:5px;\n"
"    min-width: 6em;\n"
"    color: #191a1f;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color: #016837;\n"
"    color: #4f4f4f;\n"
"    selection-background-color: #f5efe6;\n"
"    selection-color: #666699;\n"
"    font-family: \"Consolas\";\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.hedefcombobox.setPlaceholderText("")
        self.hedefcombobox.setObjectName("hedefcombobox")
        self.hedefcombobox.addItem("")
        self.hedefcombobox.addItem("")
        self.hedefcombobox.addItem("")
        self.hedefcombobox.addItem("")
        self.kaydetButton = QtWidgets.QPushButton(Dialog)
        self.kaydetButton.setGeometry(QtCore.QRect(290, 470, 161, 51))
        self.kaydetButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(87, 101, 241);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Sans Serif Collection\";\n"
"border-radius:5px;}\n"
"QPushButton:Hover{\n"
"background-color:rgb(71,82,196);}")
        self.kaydetButton.setObjectName("kaydetButton")
        self.kaydetButton.clicked.connect(self.kaydet_buton)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

       
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kayıt"))
        self.kilolinedit.setPlaceholderText(_translate("Dialog", "Kilonuz"))
        self.boylineedit.setPlaceholderText(_translate("Dialog", "Boyunuz"))
        self.yaslinedit.setPlaceholderText(_translate("Dialog", "Yaşınız"))
        self.cinsiyetcombobox.setCurrentText(_translate("Dialog", "Cinsiyetiniz"))
        self.cinsiyetcombobox.setItemText(0, _translate("Dialog", "Cinsiyetiniz"))
        self.cinsiyetcombobox.setItemText(1, _translate("Dialog", "Erkek"))
        self.cinsiyetcombobox.setItemText(2, _translate("Dialog", "Kadın"))
        self.hareketcombobox.setCurrentText(_translate("Dialog", "Hareket düzeyi"))
        self.hareketcombobox.setItemText(0, _translate("Dialog", "Hareket düzeyi"))
        self.hareketcombobox.setItemText(1, _translate("Dialog", "Hiç yok"))
        self.hareketcombobox.setItemText(2, _translate("Dialog", "Az"))
        self.hareketcombobox.setItemText(3, _translate("Dialog", "Orta seviye"))
        self.hareketcombobox.setItemText(4, _translate("Dialog", "Fazla"))
        self.hareketcombobox.setItemText(5, _translate("Dialog", "Çok fazla"))
        self.hedefcombobox.setCurrentText(_translate("Dialog", "Hedefiniz"))
        self.hedefcombobox.setItemText(0, _translate("Dialog", "Hedefiniz"))
        self.hedefcombobox.setItemText(1, _translate("Dialog", "Kilo vermek"))
        self.hedefcombobox.setItemText(2, _translate("Dialog", "Kilo koruma"))
        self.hedefcombobox.setItemText(3, _translate("Dialog", "Kilo almak"))
        self.kaydetButton.setText(_translate("Dialog", "Kaydet"))
       
        
    def kaydet_buton(self):
        global son_kullanici
        # Kullanıcı verilerini al
        yas = self.yaslinedit.text()
        boy = self.boylineedit.text()
        kilo = self.kilolinedit.text()
        cinsiyet = self.cinsiyetcombobox.currentText()
        aktivite = self.hareketcombobox.currentText()
        hedef = self.hedefcombobox.currentText()

        # Boş alan kontrolü
        if not yas or not boy or not kilo or not cinsiyet or not aktivite or not hedef:
            QtWidgets.QMessageBox.warning(None, "Hata", "Lütfen tüm alanları doldurun.")
            return

        # Günlük kalori ihtiyacı ve su miktarını hesapla
        try:
            günlükkalori = hesapla_kalori(yas, boy, kilo, cinsiyet, aktivite)
            sumiktarı = float(kilo) * 33
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Hata", f"Hesaplama hatası: {e}")
            print(f"Hesaplama hatası: {e}")
            return

        # Kullanıcının verilerini güncelle veya ekle
        try:
            conn = sqlite3.connect("kullanici_veritabani.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM kullanicilar ORDER BY id DESC LIMIT 1")
            son_kullanici = cursor.fetchone()
            print(son_kullanici)
            if son_kullanici:
                son_kullanici_id = son_kullanici[0]
                cursor.execute(
                    "UPDATE kullanicilar SET yas=?, boy=?, kilo=?, cinsiyet=?, aktivite=?, hedef=?, günlükkalori=?, sumiktarı=? WHERE id=?",
                    (yas, boy, kilo, cinsiyet, aktivite, hedef, günlükkalori, sumiktarı, son_kullanici_id)
                )
                conn.commit()
                QtWidgets.QMessageBox.information(None, "Başarılı", "Veriler başarıyla güncellendi.") 
                self.open_main_window()
                kayıtekran.hide()

            else:
                cursor.execute(
                    "INSERT INTO kullanicilar (yas, boy, kilo, cinsiyet, aktivite, hedef) VALUES (?, ?, ?, ?, ?, ?)",
                    (yas, boy, kilo, cinsiyet, aktivite, hedef)
                )
                conn.commit()
                QtWidgets.QMessageBox.information(None, "Başarılı", "Yeni kullanıcı başarıyla eklendi.")
             
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Hata", f"Veritabanı hatası: {e}")
            print(f"Veritabanı hatası: {e}")
        
     #Ana sayfayı açan fonk.
    def open_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.main_window)
        self.main_window.show()

       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    anagirisekrani = QtWidgets.QDialog()
    ui = Ui_anagirisekrani()
    ui.setupUi(anagirisekrani)
    anagirisekrani.show()
    sys.exit(app.exec_())
