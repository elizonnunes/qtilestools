# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tilelayer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgTileLayer(object):
    def setupUi(self, dlgTileLayer):
        dlgTileLayer.setObjectName(_fromUtf8("dlgTileLayer"))
        dlgTileLayer.resize(458, 266)
        self.gridLayout = QtGui.QGridLayout(dlgTileLayer)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlTitle = QtGui.QHBoxLayout()
        self.hlTitle.setObjectName(_fromUtf8("hlTitle"))
        self.lblTitle = QtGui.QLabel(dlgTileLayer)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.hlTitle.addWidget(self.lblTitle)
        self.leTitle = QtGui.QLineEdit(dlgTileLayer)
        self.leTitle.setObjectName(_fromUtf8("leTitle"))
        self.hlTitle.addWidget(self.leTitle)
        self.gridLayout.addLayout(self.hlTitle, 3, 0, 1, 1)
        self.bbActions = QtGui.QDialogButtonBox(dlgTileLayer)
        self.bbActions.setOrientation(QtCore.Qt.Horizontal)
        self.bbActions.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbActions.setObjectName(_fromUtf8("bbActions"))
        self.gridLayout.addWidget(self.bbActions, 5, 0, 1, 1)
        self.hlJSON = QtGui.QHBoxLayout()
        self.hlJSON.setObjectName(_fromUtf8("hlJSON"))
        self.lblJsonFile = QtGui.QLabel(dlgTileLayer)
        self.lblJsonFile.setObjectName(_fromUtf8("lblJsonFile"))
        self.hlJSON.addWidget(self.lblJsonFile)
        self.leJSON = QtGui.QLineEdit(dlgTileLayer)
        self.leJSON.setReadOnly(True)
        self.leJSON.setObjectName(_fromUtf8("leJSON"))
        self.hlJSON.addWidget(self.leJSON)
        self.tbJSON = QtGui.QToolButton(dlgTileLayer)
        self.tbJSON.setObjectName(_fromUtf8("tbJSON"))
        self.hlJSON.addWidget(self.tbJSON)
        self.gridLayout.addLayout(self.hlJSON, 1, 0, 1, 1)
        self.hlDir = QtGui.QHBoxLayout()
        self.hlDir.setObjectName(_fromUtf8("hlDir"))
        self.lblDir = QtGui.QLabel(dlgTileLayer)
        self.lblDir.setObjectName(_fromUtf8("lblDir"))
        self.hlDir.addWidget(self.lblDir)
        self.leDir = QtGui.QLineEdit(dlgTileLayer)
        self.leDir.setReadOnly(True)
        self.leDir.setObjectName(_fromUtf8("leDir"))
        self.hlDir.addWidget(self.leDir)
        self.tbDir = QtGui.QToolButton(dlgTileLayer)
        self.tbDir.setObjectName(_fromUtf8("tbDir"))
        self.hlDir.addWidget(self.tbDir)
        self.gridLayout.addLayout(self.hlDir, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leStyle = QtGui.QLabel(dlgTileLayer)
        self.leStyle.setObjectName(_fromUtf8("leStyle"))
        self.horizontalLayout.addWidget(self.leStyle)
        self.cbTMS = QtGui.QCheckBox(dlgTileLayer)
        self.cbTMS.setObjectName(_fromUtf8("cbTMS"))
        self.horizontalLayout.addWidget(self.cbTMS)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(dlgTileLayer)
        QtCore.QObject.connect(self.bbActions, QtCore.SIGNAL(_fromUtf8("accepted()")), dlgTileLayer.accept)
        QtCore.QObject.connect(self.bbActions, QtCore.SIGNAL(_fromUtf8("rejected()")), dlgTileLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgTileLayer)

    def retranslateUi(self, dlgTileLayer):
        dlgTileLayer.setWindowTitle(_translate("dlgTileLayer", "Create TileLayerPlugin Config File", None))
        self.lblTitle.setText(_translate("dlgTileLayer", "Layer Title:", None))
        self.lblJsonFile.setText(_translate("dlgTileLayer", "QTiles JSON File:", None))
        self.tbJSON.setText(_translate("dlgTileLayer", "...", None))
        self.lblDir.setText(_translate("dlgTileLayer", "QTiles Tilecache Directory:", None))
        self.tbDir.setText(_translate("dlgTileLayer", "...", None))
        self.leStyle.setText(_translate("dlgTileLayer", "Tile Naming Convention:", None))
        self.cbTMS.setText(_translate("dlgTileLayer", "TMS Naming", None))

