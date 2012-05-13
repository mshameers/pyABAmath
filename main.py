#!/usr/bin/env python

import sys,os															#import system libraries
from random import randint
from PyQt4.QtCore import *												#pyQt imports
from PyQt4.QtGui import *
from mathUi import Ui_Form												#gui 
from time import sleep 

class Main(QWidget):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
#initialize variables
		self.valueOne = '0'												
		self.valueTwo = '0'
		self.operaspeak = '+'
		self.opera = '+'
		self.level = 1
#gui setup		
		self.mathUi = Ui_Form()
		self.mathUi.setupUi(self)
#connect widgets with functions
		self.mathUi.operatorCombo.currentIndexChanged.connect(self.operatorSelect)
		self.mathUi.vspinBox1.valueChanged.connect(self.value1Select)
		self.mathUi.vspinBox2.valueChanged.connect(self.value2Select)
		self.mathUi.showButton.clicked.connect(self.showButtonClick)
		self.mathUi.nextlButton.clicked.connect(self.nextButtonClick)
		self.mathUi.previouslButton.clicked.connect(self.previousButtonClick)
#timer to check response time
		self.ctimer = QTimer()
		QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timeUp)
#groupboxes for levels in a list		
		self.gBtop = [self.mathUi.gBtop1,self.mathUi.gBtop2,self.mathUi.gBtop3,self.mathUi.gBbot,self.mathUi.toolsgB]
#labels for levels
		self.tLabel1 = [self.mathUi.label11,self.mathUi.label12,self.mathUi.labela1]
		self.tLabel2 = [self.mathUi.label21,self.mathUi.label22,self.mathUi.labela2]
		self.tLabel3 = [self.mathUi.label31,self.mathUi.label32,self.mathUi.labela3]
#operator for levels
		self.operator = [self.mathUi.operator1,self.mathUi.operator2,self.mathUi.operator3]
#toplabel & bottomlabel
		self.tLabel = [self.tLabel1,self.tLabel2,self.tLabel3]
		self.bLabel = [self.mathUi.blabel0,self.mathUi.blabel1,self.mathUi.blabel2,self.mathUi.blabel3,self.mathUi.blabel4,self.mathUi.blabel5,self.mathUi.blabel6,self.mathUi.blabel7,self.mathUi.blabel8,self.mathUi.blabel9]
#set hide top groupbox initially
		for i in self.gBtop[:4]:
			i.setHidden(True)
#get a random number
		self.rand3num = randint(1,9)
		self.rand = randint(0,2)
#some final beautificaion...;-D		
		palette = self.palette()
		pixmap = QPixmap("images/back.jpg")
		brush = QBrush()
		brush.setTexture(pixmap)
		palette.setBrush(QPalette.Background, brush)
		self.setPalette(palette)
		self.setWindowTitle('pyABAmath')
		self.setGeometry(width/2-self.width()/2,height/2-self.height()/2,780,600)		
		self.setFixedSize(780,600)
		#self.resize(780, 600)

#function level 1
	def level1(self,num,valueOne,valueTwo,operator):
		self.tLabel[num][0].setText(valueOne)
		self.tLabel[num][1].setText(valueTwo)
		self.operator[num].setText(operator)
		if str(self.opera) == '+':
			self.ans = str(int(valueOne)+int(valueTwo))
		else:
			self.ans = str(int(valueOne)-int(valueTwo))
		self.tLabel[num][2].setText(self.ans)
		self.gBtop[num].setHidden(False)
		self.children()[num].setStyleSheet("QGroupBox { border:2px solid rgb(255, 255, 255); }")
		app.processEvents()
		self.gBtop[num].mousePressEvent = self.gBtopMousefun#[num]
		self.speakFun(self.valueOne,self.operaspeak,self.valueTwo,self.ans)
#function level 2
	def level2(self,num,valueOne,valueTwo,operator):
		if valueOne == 0 or valueTwo == 0:
			initvalue = 0
			num1,num2 = 0
		else:
			initvalue = -9
			num1 = randint(initvalue,int(valueOne))	
			num2 = randint(initvalue,int(valueTwo))
		self.tLabel[num][0].setText(str(num1))
		self.tLabel[num][1].setText(str(num2))
		self.operator[num].setText(operator)
		if str(self.opera) == '+':
			self.ans = str(num1+num2)
		else:
			self.ans = str(num1-num2)
		self.tLabel[num][2].setText(self.ans)
		self.gBtop[num].setHidden(False)
		self.gBtop[num].mousePressEvent = self.gBtopMousefun2#[num]		
		self.children()[num].setStyleSheet("QGroupBox { border:2px solid rgb(255, 255, 255); }")

#function level 3
	def level3(self,num,valueOne,valueTwo,operator):
		self.tLabel[num][2].setText("")
		self.tLabel[num][0].setText(valueOne)
		self.tLabel[num][1].setText(valueTwo)
		self.operator[num].setText(operator)
		if str(self.opera) == '+':
			self.ans = str(int(valueOne)+int(valueTwo))
		else:
			self.ans = str(int(valueOne)-int(valueTwo))
		self.bLabel[self.rand3num].setText(self.ans)
		self.bLabel[self.rand3num].setStyleSheet("QLabel { border:2px solid rgb(255, 255, 255); }")
		self.mathUi.gBbot.setHidden(False)
		self.gBtop[num].setHidden(False)
		app.processEvents()
		self.bLabel[self.rand3num].mousePressEvent = self.gBtopMousefun3#[num]
		self.speakFun(self.valueOne,self.operaspeak,self.valueTwo,self.ans)

#function level 4		
	def level4(self,valueOne,valueTwo):
		
		self.bLabel[self.rand3num].setStyleSheet("QLabel {border:0px solid rgb(255, 255,0);")
		app.processEvents()
		
		if valueOne == '0':
			startnum = -9
			stopnum = -1
		for i in self.bLabel:
			i.setText(str(randint(startnum,stopnum)))
			i.setStyleSheet("QLabel { border:2px solid rgb(255, 255, 255); }")
			i.mousePressEvent = self.gBtopMousefun4 
		self.rand3num = randint(1,9)

#this function makes the app talking..	
	def speakFun(self,valueOne,operaspeak,valueTwo,ans):
		self.setCursor(QCursor(Qt.BlankCursor))
		#os.system("espeak 'say'")
		os.system("espeak 'say with me' -s 130 -p 100 -a 20")
		os.system("espeak"+' '+ str(self.valueOne)+' -s 150 -p 100 -a 30')
		os.system("espeak"+' '+ str(self.operaspeak)+' -s 120 -p 90 -a 30')
		os.system("espeak"+' '+ str(self.valueTwo)+' -s 150 -p 90 -a 30')
		os.system("espeak 'equals' -s 150 -p 90 -a 30")
		if self.level =='3' or self.level == '4':
				pass
		else:
			if self.ans[0] != '-':
				os.system("espeak"+' '+ str(self.ans)+' -s 150 -p 100 -a 30')
			else:
				os.system("espeak"+' '+ 'minus'+str(self.ans[1])+' -s 150 -p 100 -a 30')
		self.ctimer.start(9000)	
		self.unsetCursor()
		app.processEvents()

#check mouse clicked answer in level 1		
	def gBtopMousefun(self,event):
		self.splash()
		app.processEvents()

		self.children()[self.rand].setStyleSheet("QGroupBox { border:0px solid rgb(255, 255,0); }")	
		if event.button() != Qt.LeftButton:
			event.ignore()
			return
		self.children()[self.rand].setHidden(True)
		self.rand = randint(0,2)
		if self.level == '1':
			self.level1(self.rand,self.valueOne,self.valueTwo,self.opera)
		elif self.level == '2':
			for i in range(0,3):
				if i == self.rand:
					pass
				else:
					self.level2(i,self.valueOne,self.valueTwo,self.opera)
			self.level1(self.rand,self.valueOne,self.valueTwo,self.opera)

#check mouse clicked wrong answer in level 2
	def gBtopMousefun2(self,event):	
		self.ctimer.stop()	
		os.system("espeak 'wrong answer please try again!' -s 150 -p 90 -a 20")
		self.ctimer.start(9000)	

#check mouse clicked answer in level 3	
	def gBtopMousefun3(self,event):
		self.bLabel[self.rand3num].setText("")
		self.bLabel[self.rand3num].setStyleSheet("QLabel {border:0px solid rgb(255, 255,0);")
		
		self.ctimer.stop()	
		if self.ans[0] != '-':
			os.system("espeak"+' '+ str(self.ans)+' -s 150 -p 100 -a 20')
		else:
			os.system("espeak"+' '+ 'minus'+str(self.ans[1])+' -s 150 -p 100 -a 20')
		self.tLabel[self.rand][2].setText(self.ans)
		app.processEvents()
		self.splash()
		app.processEvents()
		#sleep(2)
		if self.level == '4':
			self.level4(self.valueOne,self.valueTwo)
		self.children()[self.rand].setHidden(True)	
		self.rand = randint(0,2)
		self.rand3num = randint(1,9)
		
		self.level3(self.rand,self.valueOne,self.valueTwo,self.opera)
		self.ctimer.start(9000)	

#check mouse clicked wrong answer in level 4
	def gBtopMousefun4(self,event):	
		os.system("espeak 'wrong answer please try again' -s 150 -p 90 -a 20")
		
#blink after some time to point the answer	
	def timeUp(self):
		if self.level == "3" or self.level == "4":
			box = "QLabel"
			nu = self.rand3num
			child = self.bLabel
		else:
			nu = self.rand
			box = "QGroupBox"
			child = self.children()
		child[nu].setStyleSheet(box+" { border:3px solid rgb(255, 255, 255); }")
		app.processEvents()
		sleep(0.5)
		child[nu].setStyleSheet(box+" { border:3px solid rgb(255, 0, 255); }")
		app.processEvents()
		sleep(0.75)
		child[nu].setStyleSheet(box+"{ border:3px solid rgb(0, 255, 255); }")
		app.processEvents()
		sleep(1)
		child[nu].setStyleSheet(box+" { border:3px solid rgb(255, 255,0); }")				
		app.processEvents()
		self.speakFun(self.valueOne,self.operaspeak,self.valueTwo,self.ans)

#fill operator combobox	
	def operatorSelect(self,i):
		operators = ['plus','minus']
		self.operaspeak = operators[i]
		self.opera = str(self.mathUi.operatorCombo.currentText())

#value1 value 
	def value1Select(self,i):
		self.valueOne = str(i)

#value2 value
	def value2Select(self,i):
		self.valueTwo = str(i)

#showButton clicked
	def showButtonClick(self,checked):		
		if checked == False:
			self.mathUi.toolsgB.setHidden(True)
			self.level = self.mathUi.levelLabel.text()[-1]
			if self.level == '1':
				self.level1(self.rand,self.valueOne,self.valueTwo,self.opera)
			elif self.level == '2':
				for i in range(0,3):
					if i == self.rand:
						pass
					else:
						self.level2(i,self.valueOne,self.valueTwo,self.opera)
				self.level1(self.rand,self.valueOne,self.valueTwo,self.opera)
			elif self.level == '3':
				
				self.level3(self.rand,self.valueOne,self.valueTwo,self.opera)
			elif self.level == '4':
				
				self.level4(self.valueOne,self.valueTwo)
				self.level3(self.rand,self.valueOne,self.valueTwo,self.opera)
			self.ctimer.start()
		else:		
			self.mathUi.toolsgB.setHidden(False)
			self.ctimer.stop()
			self.children()[self.rand].setStyleSheet("QGroupBox { border:0px solid rgb(255, 255,0); }")	

#click to go to previous level			
	def previousButtonClick(self):
		self.level = int(self.level)
		if self.level == 4  :
			for i in self.bLabel:
				i.setText(" ")
				i.setStyleSheet("QLabel {border:0px solid rgb(255, 255,0);")

		if self.level != 0:
			self.level -=1
		else: 
			self.level = 0
		for i in self.gBtop[:4]:
			i.setHidden(True)
		self.mathUi.levelLabel.setText('Level'+' '+str(self.level))		
		self.update()

#click to go to next level
	def nextButtonClick(self):
		self.level = int(self.level)
		if self.level != 4:
			self.level +=1
		else: 
			self.level = 4
			
		for i in self.gBtop[:4]:
			i.setHidden(True)
		self.mathUi.levelLabel.setText('Level'+" "+str(self.level))		
		self.update()

#if correct answer show a shining/smiling star... :-P
	def splash(self):
		splashPix = QPixmap("images/splash.png")
		splash = QSplashScreen(splashPix,Qt.WindowStaysOnTopHint)
		splash.show()
		app.processEvents()
		os.system("espeak 'good job' -s 150 -p 90 -a 20")
		sleep(1)
		splash.close()

	
if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	width = QApplication.desktop().width()
	height = QApplication.desktop().height()
	window = Main()
	window.show()
	sys.exit(app.exec_())
		
