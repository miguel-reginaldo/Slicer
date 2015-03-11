# -*- coding: utf-8 -*-
"""
/***************************************************************************
Slicer
                                 A QGIS plugin
Grouping of pixels on a raster classes
                              -------------------
        begin                : 2015-02-02
        copyright            : (C) 2014 by Miguel Reginaldo Teixeira da Silva
        email                : miguel.reginaldo@hotmail.com
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
# Import the PyQt and QGIS libraries

from PyQt4.QtGui import QAction, QIcon, QApplication

from PyQt4.QtCore import QFileInfo, QSettings, QLocale, QTranslator,\
                            QCoreApplication

from qgis.core import QGis, QgsApplication

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from slicerdialog import SlicerDialog


class Slicer:
 
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        self.qgsVersion = unicode(QGis.QGIS_VERSION_INT)

        # For i18n support
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/Slicer"
        systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/Slicer"

        overrideLocale = bool(QSettings().value("locale/overrideFlag", False))
        if not overrideLocale:
            localeFullName = QLocale.system().name()
        else:
            localeFullName = QSettings().value("locale/userLocale", "")

        if QFileInfo(userPluginPath).exists():
            translationPath = userPluginPath + "/i18n/slicer_" + localeFullName + ".qm"
        else:
            translationPath = systemPluginPath + "/i18n/slicer_" + localeFullName + ".qm"

        self.localePath = translationPath
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)
 
        # Create the dialog (after translation) and keep reference
        self.dlg = SlicerDialog()
 
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/Slicer/icon.png"),
            QCoreApplication.translate("appl","Slicer", None, QApplication.UnicodeUTF8),
            self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
 
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToRasterMenu(u"&Slicer", self.action)
 
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginRasterMenu(u"&Slicer", self.action)
        self.iface.removeToolBarIcon(self.action)
 
    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass

