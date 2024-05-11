# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EdgdeDetection\Qt_EdgeDetection.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EdgeDetection_Gui(object):
    def setupUi(self, EdgeDetection_Gui):
        EdgeDetection_Gui.setObjectName("EdgeDetection_Gui")
        EdgeDetection_Gui.resize(992, 571)
        self.groupBox = QtWidgets.QGroupBox(EdgeDetection_Gui)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 611, 201))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(True)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 181, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 50, 91, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lowthreshold_textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.lowthreshold_textEdit.setReadOnly(True)
        self.lowthreshold_textEdit.setObjectName("lowthreshold_textEdit")
        self.verticalLayout_3.addWidget(self.lowthreshold_textEdit)
        self.highthreshold_textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.highthreshold_textEdit.setReadOnly(True)
        self.highthreshold_textEdit.setObjectName("highthreshold_textEdit")
        self.verticalLayout_3.addWidget(self.highthreshold_textEdit)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 50, 241, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hysteresislowth_horizontalSlider = QtWidgets.QSlider(self.layoutWidget2)
        self.hysteresislowth_horizontalSlider.setMinimum(1)
        self.hysteresislowth_horizontalSlider.setMaximum(1000)
        self.hysteresislowth_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hysteresislowth_horizontalSlider.setObjectName("hysteresislowth_horizontalSlider")
        self.verticalLayout.addWidget(self.hysteresislowth_horizontalSlider)
        self.hysteresishighth_horizontalSlider = QtWidgets.QSlider(self.layoutWidget2)
        self.hysteresishighth_horizontalSlider.setMinimum(1)
        self.hysteresishighth_horizontalSlider.setMaximum(1000)
        self.hysteresishighth_horizontalSlider.setProperty("value", 100)
        self.hysteresishighth_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hysteresishighth_horizontalSlider.setObjectName("hysteresishighth_horizontalSlider")
        self.verticalLayout.addWidget(self.hysteresishighth_horizontalSlider)
        self.Kernelsize_label = QtWidgets.QLabel(self.groupBox)
        self.Kernelsize_label.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.Kernelsize_label.setObjectName("Kernelsize_label")
        self.Kernelsize_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.Kernelsize_comboBox.setGeometry(QtCore.QRect(110, 130, 73, 22))
        self.Kernelsize_comboBox.setObjectName("Kernelsize_comboBox")
        self.Kernelsize_comboBox.addItem("")
        self.Kernelsize_comboBox.addItem("")
        self.Kernelsize_comboBox.addItem("")
        self.L2norm_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.L2norm_checkBox.setGeometry(QtCore.QRect(230, 130, 131, 31))
        self.L2norm_checkBox.setObjectName("L2norm_checkBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 381, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(EdgeDetection_Gui)
        QtCore.QMetaObject.connectSlotsByName(EdgeDetection_Gui)

    def retranslateUi(self, EdgeDetection_Gui):
        _translate = QtCore.QCoreApplication.translate
        EdgeDetection_Gui.setWindowTitle(_translate("EdgeDetection_Gui", "Form"))
        self.groupBox.setTitle(_translate("EdgeDetection_Gui", "CANNY EDGE DETECION"))
        self.label.setText(_translate("EdgeDetection_Gui", "Hysteresis Low threshold"))
        self.label_2.setText(_translate("EdgeDetection_Gui", "Hysteresis High threshold"))
        self.Kernelsize_label.setText(_translate("EdgeDetection_Gui", "Kernel size"))
        self.Kernelsize_comboBox.setItemText(0, _translate("EdgeDetection_Gui", "3"))
        self.Kernelsize_comboBox.setItemText(1, _translate("EdgeDetection_Gui", "4"))
        self.Kernelsize_comboBox.setItemText(2, _translate("EdgeDetection_Gui", "5"))
        self.L2norm_checkBox.setText(_translate("EdgeDetection_Gui", "L2 norm accurate"))
        self.label_3.setText(_translate("EdgeDetection_Gui", "<html><head/><body><p><a href=\"https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de\"><span style=\" text-decoration: underline; color:#0000ff;\">Reference link to Opencv Canny()</span></a></p></body></html>"))
