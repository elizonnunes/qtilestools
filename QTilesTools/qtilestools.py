# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QTilesTools
                                 A QGIS plugin
 Tools to use QTiles outputs for offline base map use with QGIS and GeoODK Collect
                              -------------------
        begin                : 2016-06-30
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Apropos Information Systems
        email                : tsw@aproposinfosystems.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtGui, QtCore, QtSql
# Initialize Qt resources from file resources.py
import resources, os
# Import the code for the dialog
from qtt_tilelayer import qttTileLayer



class QTilesTools:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QtCore.QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'QTilesTools_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QtCore.QTranslator()
            self.translator.load(locale_path)

            if QtCore.qVersion() > '4.3.3':
                QtCore.QCoreApplication.installTranslator(self.translator)


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

       # Add toolbar 
        self.toolBar = self.iface.addToolBar("QTiles Tools")
        self.toolBar.setObjectName("QTilesTools")

        # Settings and GIS Action
        self.tileLayerAction = QtGui.QAction(
            QtGui.QIcon(":/plugins/QTilesTools/tilelayer_icon.png"),
            u"Create TileLayerPlugin configuration file", self.iface.mainWindow())
        # connect the action to the run method
        self.tileLayerAction.triggered.connect(self.tileLayerConfig)
        self.toolBar.addAction(self.tileLayerAction)
        
        # Project Definition Action
        self.geoODKAction = QtGui.QAction(
            QtGui.QIcon(":/plugins/QTilesTools/geoodkcollect_icon.png"),
            u"Configure mbTiles database for GeoODK Collect", self.iface.mainWindow())
        # connect the action to the run method
        self.geoODKAction.triggered.connect(self.geoODKConfig)
        self.toolBar.addAction(self.geoODKAction)

        # add to menu
        self.iface.addPluginToMenu(u"&QTiles Tools", self.tileLayerAction)
        self.iface.addPluginToMenu(u"&QTiles Tools", self.geoODKAction)

    #--------------------------------------------------------------------------

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&QTiles Tools", self.tileLayerAction)
        self.iface.removePluginMenu(u"&QTiles Tools", self.geoODKAction)

        # remove tool bar
        self.toolBar.hide()
        self.toolBar = None

    #--------------------------------------------------------------------------
    
    def tileLayerConfig(self):

         # Create the dialog (after translation) and keep reference
        self.dlg = qttTileLayer(self.iface)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
       
    def geoODKConfig(self):

        dbName = QtGui.QFileDialog.getOpenFileName(self.iface.parent(), 'Select mbTiles database', '.', '*.mbtiles')
        if os.path.exists(dbName):
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(dbName)
            db.open()
            model = QtSql.QSqlTableModel()
            model.setTable('images')
            if not model.select():
                query = QtSql.QSqlQuery()
                try:
                    query.exec_("CREATE TABLE images (tile_data blob, tile_id text);")
                    db.close()
                    messageText = "Required table created in %s." % dbName
                    response = QtGui.QMessageBox.information(self.iface.parent(), 'Success',
                        messageText, QtGui.QMessageBox.Ok)
                except:
                    messageText = "Unable to create required table in %s." % dbName
                    response = QtGui.QMessageBox.warning(self.iface.parent(), 'Warning',
                        messageText, QtGui.QMessageBox.Ok)
            else:
                messageText = "Required table already exists in %s." % dbName
                response = QtGui.QMessageBox.information(self.iface.parent(), 'Information',
                    messageText, QtGui.QMessageBox.Ok)
                
            
