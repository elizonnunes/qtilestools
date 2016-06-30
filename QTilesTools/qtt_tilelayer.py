"""
# -*- coding: utf-8 -*-
#
# ========================================================
# 
# Purpose: Calculate planning unit content
# Author: Trevor Wiens
# Copyright: Apropos Information Systems Inc.
# Date: 2014-10-01
# License: GPL2 
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------
"""

from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *
import math,os,inspect,json
import qtilestools
from ui_tilelayer import Ui_dlgTileLayer


class qttTileLayer(QtGui.QDialog,Ui_dlgTileLayer):

    #
    # initialization

    def __init__(self, iface):

        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface

        # debugging
        self.debug = False
        self.showCalcDef = False
        if self.debug == True:
            self.myself = lambda: inspect.stack()[1][3]
            QgsMessageLog.logMessage(self.myself())
        self.qtDir = '.'
        self.jfName = ''

        # make connections
        QtCore.QObject.connect(self.tbDir, QtCore.SIGNAL("clicked()"), self.selectDir)
        QtCore.QObject.connect(self.tbJSON, QtCore.SIGNAL("clicked()"), self.selectJSON)
        QtCore.QObject.connect(self.bbActions, QtCore.SIGNAL("accepted ()"), self.writeFile)

    #
    # select qtiles directory
    #
    def selectDir(self):
        
        self.qtDir = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory', self.qtDir)
        if self.qtDir <> '' and os.path.exists(self.qtDir):
            self.leDir.setText(self.qtDir)

    #
    # select json file
    #
    def selectJSON(self):
        
        head,tail = os.path.split(self.qtDir)
        self.jfName = QtGui.QFileDialog.getOpenFileName(self, 'Select JSON file', head, '*.json')
        if os.path.exists(self.jfName):
            self.leJSON.setText(self.jfName)
            
    #
    # create file when button bar ok is clicked
    #
    def writeFile(self):

        head,tail = os.path.split(self.qtDir)
        title = self.leTitle.text()
        if title == '':
            title = tail
        #print fName
        if self.cbTMS.isChecked():
            tileType = 0
        else:
            tileType = 1
        if os.path.exists(self.jfName) and len(tail) > 0:
            f = open(self.jfName,'r')
            dDict = json.loads(f.read())
            f.close()
            outLine = "%s\t%s\t" % (tail,title)
            outLine += "file:///%s/{z}/{x}/{y}.%s\t" % (self.qtDir,dDict['format'])
            outLine += "%d\t%d\t%d\t" % (tileType,dDict['minZoom'],dDict['maxZoom'])
            bVals = dDict['bounds'].split(',')
            outLine += "%s\t%s\t%s\t%s\n" % (bVals[0],bVals[1],bVals[2],bVals[3])
            #print outLine
            fName = os.path.join(head,tail + '.tsv')
            f = open(fName,'w')
            f.write(outLine)
            f.close()
            messageText = "%s created." % fName
            response = QtGui.QMessageBox.information(self, 'Success',
                messageText, QtGui.QMessageBox.Ok)
        else:
            messageText = "Unable to create file. Please ensure all values are set before clicking OK."
            response = QtGui.QMessageBox.warning(self, 'Warning',
                messageText, QtGui.QMessageBox.Ok)
