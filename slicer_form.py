# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slicer_form.ui'
#
# Created: Fri Mar 06 09:01:16 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dlgSlicer(object):
    def setupUi(self, dlgSlicer):
        dlgSlicer.setObjectName(_fromUtf8("dlgSlicer"))
        dlgSlicer.resize(462, 521)
        font = QtGui.QFont()
        font.setPointSize(11)
        dlgSlicer.setFont(font)
        dlgSlicer.setLocale(QtCore.QLocale(QtCore.QLocale.system().language(),
                                    QtCore.QLocale.system().country()))
        self.gbFiles = QtGui.QGroupBox(dlgSlicer)
        self.gbFiles.setGeometry(QtCore.QRect(10, 10, 441, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gbFiles.setFont(font)
        self.gbFiles.setObjectName(_fromUtf8("gbFiles"))
        self.gridLayoutWidget = QtGui.QWidget(self.gbFiles)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 25, 421, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gdFiles = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gdFiles.setMargin(0)
        self.gdFiles.setObjectName(_fromUtf8("gdFiles"))
        self.btSelect = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btSelect.setFont(font)
        self.btSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSelect.setAutoDefault(False)
        self.btSelect.setObjectName(_fromUtf8("btSelect"))
        self.gdFiles.addWidget(self.btSelect, 1, 1, 1, 1)
        self.edInput = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edInput.setFont(font)
        self.edInput.setObjectName(_fromUtf8("edInput"))
        self.gdFiles.addWidget(self.edInput, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gdFiles.addWidget(self.label_3, 0, 0, 1, 1)
        self.edOutput = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edOutput.setFont(font)
        self.edOutput.setObjectName(_fromUtf8("edOutput"))
        self.gdFiles.addWidget(self.edOutput, 3, 0, 1, 1)
        self.btSave = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btSave.setFont(font)
        self.btSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSave.setAutoDefault(False)
        self.btSave.setObjectName(_fromUtf8("btSave"))
        self.gdFiles.addWidget(self.btSave, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gdFiles.addWidget(self.label_2, 2, 0, 1, 1)
        self.cbAddLayer = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cbAddLayer.setChecked(True)
        self.cbAddLayer.setObjectName(_fromUtf8("cbAddLayer"))
        self.gdFiles.addWidget(self.cbAddLayer, 4, 0, 1, 2)
        self.cbCompress = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cbCompress.setChecked(True)
        self.cbCompress.setObjectName(_fromUtf8("cbCompress"))
        self.gdFiles.addWidget(self.cbCompress, 5, 0, 1, 2)
        self.frButtons = QtGui.QFrame(dlgSlicer)
        self.frButtons.setGeometry(QtCore.QRect(10, 460, 441, 51))
        self.frButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frButtons.setFrameShadow(QtGui.QFrame.Sunken)
        self.frButtons.setObjectName(_fromUtf8("frButtons"))
        self.btSlice = QtGui.QPushButton(self.frButtons)
        self.btSlice.setGeometry(QtCore.QRect(10, 10, 101, 33))
        self.btSlice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btSlice.setIconSize(QtCore.QSize(25, 25))
        self.btSlice.setAutoDefault(False)
        self.btSlice.setObjectName(_fromUtf8("btSlice"))
        self.btClose = QtGui.QPushButton(self.frButtons)
        self.btClose.setGeometry(QtCore.QRect(370, 10, 60, 33))
        self.btClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btClose.setIconSize(QtCore.QSize(25, 25))
        self.btClose.setAutoDefault(False)
        self.btClose.setObjectName(_fromUtf8("btClose"))
        self.progressBar = QtGui.QProgressBar(self.frButtons)
        self.progressBar.setGeometry(QtCore.QRect(120, 15, 181, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btHelp = QtGui.QPushButton(self.frButtons)
        self.btHelp.setGeometry(QtCore.QRect(300, 10, 60, 33))
        self.btHelp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btHelp.setIconSize(QtCore.QSize(29, 25))
        self.btHelp.setAutoDefault(False)
        self.btHelp.setObjectName(_fromUtf8("btHelp"))
        self.gbDefinition = QtGui.QGroupBox(dlgSlicer)
        self.gbDefinition.setGeometry(QtCore.QRect(10, 230, 441, 221))
        self.gbDefinition.setObjectName(_fromUtf8("gbDefinition"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.gbDefinition)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 24, 421, 21))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lbMin = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbMin.setFont(font)
        self.lbMin.setText(_fromUtf8(""))
        self.lbMin.setObjectName(_fromUtf8("lbMin"))
        self.horizontalLayout.addWidget(self.lbMin)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lbMax = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbMax.setFont(font)
        self.lbMax.setText(_fromUtf8(""))
        self.lbMax.setObjectName(_fromUtf8("lbMax"))
        self.horizontalLayout.addWidget(self.lbMax)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.gbDefinition)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 201, 24))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.rbFixed = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbFixed.setChecked(True)
        self.rbFixed.setObjectName(_fromUtf8("rbFixed"))
        self.horizontalLayout_2.addWidget(self.rbFixed)
        self.rbVariable = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.rbVariable.setObjectName(_fromUtf8("rbVariable"))
        self.horizontalLayout_2.addWidget(self.rbVariable)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayoutWidget = QtGui.QWidget(self.gbDefinition)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 90, 201, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.sbInitial = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.sbInitial.setDecimals(2)
        self.sbInitial.setMinimum(-99999999.0)
        self.sbInitial.setMaximum(100000000.0)
        self.sbInitial.setObjectName(_fromUtf8("sbInitial"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sbInitial)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.sbEnd = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.sbEnd.setDecimals(2)
        self.sbEnd.setMaximum(100000000.0)
        self.sbEnd.setObjectName(_fromUtf8("sbEnd"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sbEnd)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.sbStep = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.sbStep.setDecimals(2)
        self.sbStep.setMaximum(100000000.0)
        self.sbStep.setObjectName(_fromUtf8("sbStep"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.sbStep)
        self.label = QtGui.QLabel(self.gbDefinition)
        self.label.setGeometry(QtCore.QRect(220, 65, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btAdd = QtGui.QPushButton(self.gbDefinition)
        self.btAdd.setGeometry(QtCore.QRect(220, 180, 87, 26))
        self.btAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btAdd.setAutoDefault(False)
        self.btAdd.setObjectName(_fromUtf8("btAdd"))
        self.btRemove = QtGui.QPushButton(self.gbDefinition)
        self.btRemove.setGeometry(QtCore.QRect(344, 180, 87, 26))
        self.btRemove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btRemove.setAutoDefault(False)
        self.btRemove.setObjectName(_fromUtf8("btRemove"))
        self.listSlices = QtGui.QListWidget(self.gbDefinition)
        self.listSlices.setGeometry(QtCore.QRect(220, 90, 211, 84))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(11)
        self.listSlices.setFont(font)
        self.listSlices.setObjectName(_fromUtf8("listSlices"))

        self.retranslateUi(dlgSlicer)
        QtCore.QObject.connect(self.btClose, QtCore.SIGNAL(_fromUtf8("clicked()")), dlgSlicer.close)
        QtCore.QMetaObject.connectSlotsByName(dlgSlicer)
        dlgSlicer.setTabOrder(self.edInput, self.btSelect)
        dlgSlicer.setTabOrder(self.btSelect, self.edOutput)
        dlgSlicer.setTabOrder(self.edOutput, self.btSave)
        dlgSlicer.setTabOrder(self.btSave, self.cbAddLayer)
        dlgSlicer.setTabOrder(self.cbAddLayer, self.cbCompress)
        dlgSlicer.setTabOrder(self.cbCompress, self.rbFixed)
        dlgSlicer.setTabOrder(self.rbFixed, self.rbVariable)
        dlgSlicer.setTabOrder(self.rbVariable, self.sbInitial)
        dlgSlicer.setTabOrder(self.sbInitial, self.sbEnd)
        dlgSlicer.setTabOrder(self.sbEnd, self.sbStep)
        dlgSlicer.setTabOrder(self.sbStep, self.listSlices)
        dlgSlicer.setTabOrder(self.listSlices, self.btAdd)
        dlgSlicer.setTabOrder(self.btAdd, self.btRemove)
        dlgSlicer.setTabOrder(self.btRemove, self.btSlice)
        dlgSlicer.setTabOrder(self.btSlice, self.btHelp)
        dlgSlicer.setTabOrder(self.btHelp, self.btClose)

    def retranslateUi(self, dlgSlicer):
        dlgSlicer.setWindowTitle(QtGui.QApplication.translate("dlgSlicer", "Slicer", None, QtGui.QApplication.UnicodeUTF8))
        self.gbFiles.setTitle(QtGui.QApplication.translate("dlgSlicer", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.btSelect.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Select the input file (Alt + I)", None, QtGui.QApplication.UnicodeUTF8))
        self.btSelect.setText(QtGui.QApplication.translate("dlgSlicer", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btSelect.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+I", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlgSlicer", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.btSave.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Enter the output file (Alt + O)", None, QtGui.QApplication.UnicodeUTF8))
        self.btSave.setText(QtGui.QApplication.translate("dlgSlicer", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btSave.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+O", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgSlicer", "Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAddLayer.setText(QtGui.QApplication.translate("dlgSlicer", "Add to Raster Layers Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCompress.setText(QtGui.QApplication.translate("dlgSlicer", "Compress Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.btSlice.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Slice (Alt+S)", None, QtGui.QApplication.UnicodeUTF8))
        self.btSlice.setText(QtGui.QApplication.translate("dlgSlicer", "Slice", None, QtGui.QApplication.UnicodeUTF8))
        self.btSlice.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.btClose.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Close (Alt+C)", None, QtGui.QApplication.UnicodeUTF8))
        self.btClose.setText(QtGui.QApplication.translate("dlgSlicer", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.btClose.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+C", None, QtGui.QApplication.UnicodeUTF8))
        self.btHelp.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Help (Alt+H)", None, QtGui.QApplication.UnicodeUTF8))
        self.btHelp.setText(QtGui.QApplication.translate("dlgSlicer", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.btHelp.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+H", None, QtGui.QApplication.UnicodeUTF8))
        self.gbDefinition.setTitle(QtGui.QApplication.translate("dlgSlicer", "Definition of slices", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dlgSlicer", "Minimum Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlgSlicer", "Maximum Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlgSlicer", "Step:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbFixed.setText(QtGui.QApplication.translate("dlgSlicer", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.rbVariable.setText(QtGui.QApplication.translate("dlgSlicer", "Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlgSlicer", "Initial", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dlgSlicer", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("dlgSlicer", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgSlicer", "Slices", None, QtGui.QApplication.UnicodeUTF8))
        self.btAdd.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Add the slice (Alt + A)", None, QtGui.QApplication.UnicodeUTF8))
        self.btAdd.setText(QtGui.QApplication.translate("dlgSlicer", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btAdd.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.btRemove.setToolTip(QtGui.QApplication.translate("dlgSlicer", "Remove the slice (Alt + R)", None, QtGui.QApplication.UnicodeUTF8))
        self.btRemove.setText(QtGui.QApplication.translate("dlgSlicer", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btRemove.setShortcut(QtGui.QApplication.translate("dlgSlicer", "Alt+R", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
