#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QLineEdit, QLabel, QWidget, QPlainTextEdit, QPushButton, QVBoxLayout,QGridLayout, QSpinBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from lwidget import LWidget

class LParseQT(QMainWindow):
	def __init__(self):
		super().__init__()
		self.windowsetup()

	bsubmit = None
	aedit = None
	vedit = None
	dspin = None
	lrender = None
	mainwidget = None

	def toolbarsetup(self):
		renderAction = QAction(QIcon.fromTheme("applications-science"), 'Render', self)
		renderAction.setShortcut('Ctrl+R')
		renderAction.triggered.connect(self.signalRender)

		settingsAction = QAction(QIcon.fromTheme("document-properties"), 'Settings', self)
		settingsAction.setShortcut('Ctrl+P')
		settingsAction.triggered.connect(self.signalRender)

		self.toolbar = self.addToolBar('Tools')
		self.toolbar.addAction(renderAction)
		self.toolbar.addAction(settingsAction)

	def layoutsetup(self):
		self.mainwidget = QWidget(self)
		self.setCentralWidget(self.mainwidget)

		vbox = QVBoxLayout()
		self.lrender = LWidget()

		vargrid = QGridLayout()
		alabel = QLabel("Axiom")
		vargrid.addWidget(alabel,0,0)
		self.aedit = QLineEdit()
		vargrid.addWidget(self.aedit,0,1)

		vlabel = QLabel("Variables")
		vargrid.addWidget(vlabel,1,0)
		self.vedit = QPlainTextEdit()
		vargrid.addWidget(self.vedit,1,1)

		self.dspin = QSpinBox()
		self.dspin.setMinimum(0)
		self.dspin.setMaximum(99)
		self.dspin.setValue(1)
		vargrid.addWidget(self.dspin,0,2)

		self.sspin = QSpinBox()
		self.sspin.setMinimum(1)
		self.sspin.setMaximum(99)
		self.sspin.setValue(5)
		vargrid.addWidget(self.sspin,1,2)

		# Actual layout
		vbox.addWidget(self.lrender,1)
		vbox.addLayout(vargrid)
		self.mainwidget.setLayout(vbox)

	def windowsetup(self):
		self.toolbarsetup()
		self.layoutsetup()

		self.setWindowTitle("L-Parser")
		self.show()

	def signalRender(self):
		self.lrender.valueSetEvent({"axiom":self.aedit.text(), "depth":self.dspin.value(), "env":self.vedit.toPlainText(), "scale":self.sspin.value()})
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	render = LParseQT()
	sys.exit(app.exec_())

