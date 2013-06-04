#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QMainWindow, QPushButton, QApplication
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,  QMessageBox, QFileDialog

from PySide import QtCore, QtGui
 
from form1 import Ui_MainWindow

from imageresize import *
from cdnsend import *
import os, filecmp
import Image
import sys
from adtsend import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        

        self.pushButton_2.clicked.connect(self.filedialog)
        #self.refreshButton.clicked.connect(self.listfield)
        self.buttonBox.accepted.connect(self.listfield)
		#self.buttonBox.rejected.connect(self.reject)
        


        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,QtGui.QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

    def filedialog(self):
    	fileName = QFileDialog.getOpenFileName(self,"Open Image", "/home/pavel", "Image Files (*.png *.jpg *.bmp)")
    	if fileName:
    		image = QtGui.QImage(fileName[0])
    		#self.lineEdit.insert(fileName[0])
    		self.imagefilename=fileName[0].encode("UTF-8")
    		self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
    		self.scaleFactor = 1.0

    def listfield(self):
    	#print "sdfsdf"
    	#self.label_3.setText="dsfsdf"
    	#msgBox = QMessageBox()
    	#msgBox.setText("The document ыфвфывhas been modifiasdased.")
        #msgBox.exec_()
        #self.label_3.setText("text")
        #self.title.setText("dfdsfds")
        #self.altname.setText(self.title.text())
        post={
        		"region_id":"1",
        		"category_id":"1",
			"altname":self.altname.text(),
			"title":self.title.text(),
			"text":self.text_desc.toPlainText(),
			"price":self.price.text(),
			#"isactive"=>self.isactive.text(),
			#"ontop"=>"",
			"imageurl":self.imageurl.text(),
			#"partner_id":self.partner_id.text(),
			"partner_id":"1",
			"district":self.district.text(),
			"space":self.space.text(),
			"floor":self.floor.text(),
			"material":self.material.text(),
			"plan":self.plan.text(),
			"year":self.year.text(),
			"conditionbuilding":self.conditionbuilding.text(),
			"apartmentstate":self.apartmentstate.text(),
			"balcony":"1",
			"phone":"1",
		
			#"contact"=>"",
			#"tags"=>"",
			#"user_id"=>"",
			#"updated_at"=>"2013-05-30T04:04:33Z",
			#"created_at"=>"2013-05-30T04:04:33Z",
			#"isdelete"=>"",
			#"id"=>40,
		}
	#print post
	adtsnd= Adtsend()
	print adtsnd.send_post(post)







if __name__ == "__main__":
    # QTextCodec::setCodecForTr(QTextCodec::codecForName("UTF-8"));
     #QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
     app = QApplication(sys.argv)
     frame = MainWindow()
     frame.show()
     app.exec_()
