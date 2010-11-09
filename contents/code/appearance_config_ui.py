# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents/ui/appearance_config.ui'
#
# Created: Mon Sep 28 10:08:36 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 268)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 261, 101))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 241, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_button = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.horizontal_layout_button.setObjectName("horizontal_layout_button")
        self.verticalLayout.addWidget(self.horizontal_layout_button)
        self.vertical_layout_button = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.vertical_layout_button.setObjectName("vertical_layout_button")
        self.verticalLayout.addWidget(self.vertical_layout_button)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 411, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 391, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.auto_width_button = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.auto_width_button.setObjectName("auto_width_button")
        self.verticalLayout_2.addWidget(self.auto_width_button)
        self.fixed_width_button = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.fixed_width_button.setObjectName("fixed_width_button")
        self.verticalLayout_2.addWidget(self.fixed_width_button)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.width_slider = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.width_slider.setMinimum(10)
        self.width_slider.setMaximum(200)
        self.width_slider.setOrientation(QtCore.Qt.Horizontal)
        self.width_slider.setObjectName("width_slider")
        self.horizontalLayout.addWidget(self.width_slider)
        self.width_spinbox = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.width_spinbox.setMinimum(10)
        self.width_spinbox.setMaximum(200)
        self.width_spinbox.setObjectName("width_spinbox")
        self.horizontalLayout.addWidget(self.width_spinbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 10, 141, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.default_background_button = QtGui.QRadioButton(self.groupBox_3)
        self.default_background_button.setObjectName("default_background_button")
        self.verticalLayout_3.addWidget(self.default_background_button)
        self.translucent_background_button = QtGui.QRadioButton(self.groupBox_3)
        self.translucent_background_button.setObjectName("translucent_background_button")
        self.verticalLayout_3.addWidget(self.translucent_background_button)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.width_slider, QtCore.SIGNAL("valueChanged(int)"), self.width_spinbox.setValue)
        QtCore.QObject.connect(self.width_spinbox, QtCore.SIGNAL("valueChanged(int)"), self.width_slider.setValue)
        QtCore.QObject.connect(self.fixed_width_button, QtCore.SIGNAL("toggled(bool)"), self.width_slider.setEnabled)
        QtCore.QObject.connect(self.fixed_width_button, QtCore.SIGNAL("toggled(bool)"), self.width_spinbox.setEnabled)
        QtCore.QObject.connect(self.auto_width_button, QtCore.SIGNAL("toggled(bool)"), self.width_slider.setDisabled)
        QtCore.QObject.connect(self.auto_width_button, QtCore.SIGNAL("toggled(bool)"), self.width_spinbox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontal_layout_button.setText(QtGui.QApplication.translate("Form", "Horizontal (side-by-side)", None, QtGui.QApplication.UnicodeUTF8))
        self.vertical_layout_button.setText(QtGui.QApplication.translate("Form", "Vertical (stacked)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Button Width", None, QtGui.QApplication.UnicodeUTF8))
        self.auto_width_button.setText(QtGui.QApplication.translate("Form", "Automatic (based on button text)", None, QtGui.QApplication.UnicodeUTF8))
        self.fixed_width_button.setText(QtGui.QApplication.translate("Form", "Fixed size:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Background", None, QtGui.QApplication.UnicodeUTF8))
        self.default_background_button.setText(QtGui.QApplication.translate("Form", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.translucent_background_button.setText(QtGui.QApplication.translate("Form", "Translucent", None, QtGui.QApplication.UnicodeUTF8))

