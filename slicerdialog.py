# -*- coding: utf-8 -*-
"""
/***************************************************************************
SlicerDialog
                                 A QGIS plugin
 Grouping of pixels on a raster classes
                             -------------------
        begin                : 2015-02-02
        copyright            : (C) 2015 by Miguel Reginaldo Teixeira da Silva
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

import os

from osgeo import osr, gdal

from qgis import utils

import numpy as np

from PyQt4 import QtCore

from PyQt4.QtGui import QDialog, QMessageBox, QFileDialog, QCursor

from slicer_form import Ui_dlgSlicer
import traceback


class SlicerDialog(QDialog):
    '''
    Create the main form
    ''' 
    
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_dlgSlicer()
        self.ui.setupUi(self)
        
        # Makes invisible the Progress Bar
        prg = self.ui.progressBar
        prg.setVisible(False)
 
        ################ Persistent variables #################
        #Working Directory
        self.direct = os.path.dirname(__file__) + '\\Dados\\'
        
        ##############################################
 
        # Signal from the button 'Select' input file
        self.ui.btSelect.clicked.connect(self.select_file)

        # Signal from the button 'Save' Output file
        self.ui.btSave.clicked.connect(self.save_file)
        
        # Signal from the 'rbVariavel'
        self.ui.rbVariable.clicked.connect(self.type_step)
        
        # Signal from the 'rbFixo'
        self.ui.rbFixed.clicked.connect(self.type_step)
        
        # Signal from the 'Add' button
        self.ui.btAdd.clicked.connect(self.add_step)

        # Signal from the button 'Remove'
        self.ui.btRemove.clicked.connect(self.del_step)

        # Signal from the button 'Slice'
        self.ui.btSlice.clicked.connect(self.slice)


    def type_step(self):
        if self.ui.rbVariable.isChecked():
            self.ui.sbStep.setEnabled(False)
        else:
            self.ui.sbStep.setEnabled(True)
      
    def add_step(self):
        listSlices = self.ui.listSlices
        # List of all the items 'listSlices'
        listItems = []
        for i in range(listSlices.count()):
            listItems.append(listSlices.item(i).text())
            
        ini = self.ui.sbInitial.value()
        fim = self.ui.sbEnd.value()
        # If the step is variable
        if self.ui.rbVariable.isChecked():
            item_vl = str(ini)+' - '+str(fim)
            if item_vl not in listItems:
                listSlices.addItem(item_vl)
                listSlices.item(len(listItems)).setCheckState(0)
        # If the step is fixed
        else:
            # Deletes all items
            for i in range(listSlices.count())[::-1]:
                listSlices.takeItem(i)
            
            pas = self.ui.sbStep.value()
            if pas>0:
                fim_pas = ini + pas
                j = 0
                # The end of the last interval has to be a multiple of the step
                fim_mult = fim
                if (fim-ini)%pas>0:
                    fim_mult = ((fim - ini) // pas + 1) * pas + ini
    
                while fim_pas <= fim_mult:
                    item_vl = str(ini)+' - '+str(fim_pas)
                    listSlices.addItem(item_vl)
                    listSlices.item(j).setCheckState(0)
                    j += 1
                    ini = fim_pas
                    fim_pas += pas

    def del_step(self):
        listSlices = self.ui.listSlices
        # Loop in reverse slices list
        for i in range(listSlices.count())[::-1]:
            # Remove the marked slices
            if listSlices.item(i).checkState()==2:
                listSlices.takeItem(i)

    def slice(self):
        # Get the slices
        slices = []
        listSlices = self.ui.listSlices
        for i in range(listSlices.count()):
            tx = str(listSlices.item(i).text())
            pos = tx.find('-')
            ft = (float(tx[:pos-1]), float(tx[pos+2:]))
            slices.append(ft)
        
        arq_ent = unicode(self.ui.edInput.text())
        arq_sai = unicode(self.ui.edOutput.text())
        
        if os.path.exists(arq_ent) and arq_sai:
            try:
                # Changes the cursor pointer to 'wait'
                self.setCursor(QCursor(QtCore.Qt.WaitCursor))
                
                # Convert Raster to array
                rasterArray = self.rasterTOarray(arq_ent)
                
                rows = rasterArray.shape[0]
                cols = rasterArray.shape[1]
                
                # Get no data value of array
                noDataValue = self.getNoDataValue(arq_ent)
                
                # Creates a zero array to store the sliced data
                array_slice = np.zeros((rows, cols), dtype=np.float)
                
                # Enables Progress Bar
                prg = self.ui.progressBar
                prg.setMinimum(0)
                prg.setMaximum(rasterArray.size)
                prg.setVisible(True)
                self.repaint()
                
                ct = 1
                for i, lin in enumerate(rasterArray):
                    for j, vl in enumerate(lin):
                        # Evolves the progress bar
                        prg.setValue(ct)
                        ct+=1
                        if vl==noDataValue:
                            array_slice[i,j] = noDataValue
                        else:
                            clas = 1
                            for sl in slices:
                                if vl>=sl[0] and vl<sl[1]:
                                    array_slice[i,j] = clas
                                clas += 1
                
                # Write updated array to new raster
                self.arrayTOraster(arq_ent,arq_sai,array_slice)
                
                # Add layers to the raster panel
                if self.ui.cbAddLayer.isChecked():
                    utils.iface.addRasterLayer(arq_sai)
                
                prg.setVisible(False)

                # Changes the cursor pointer to 'Arrow'
                self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
                QMessageBox.information(self, self.tr(u'Slicer'),
                                        self.tr(u'Process completed successfully!'),
                                        buttons=QMessageBox.Ok,
                                        defaultButton=QMessageBox.NoButton)

            except RuntimeError, e:
                # Changes the cursor pointer to 'Arrow'
                self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
                
                QMessageBox.critical(self, self.tr(u'Slicer'),
                                     self.tr(u'The error occurred: %s').arg(e),
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.NoButton)
        else:
            QMessageBox.critical(self, self.tr(u'Slicer'),
                                 self.tr(u'You must enter the Input and Output Files!'),
                                 buttons=QMessageBox.Ok,
                                 defaultButton=QMessageBox.NoButton)
            

        
    def rasterTOarray(self, arq_ent):
        '''Converts a raster into an array'''
        raster = gdal.Open(arq_ent, 0)
        band = raster.GetRasterBand(1)
        return band.ReadAsArray()
    
    def getNoDataValue(self, arq_ent):
        '''Get the value of NoDataValue'''
        raster = gdal.Open(arq_ent)
        band = raster.GetRasterBand(1)
        return band.GetNoDataValue()
    
    def arrayTOraster(self, arq_ent, arq_sai, array):
        '''Converts an array in a raster'''
        raster = gdal.Open(arq_ent, 0)
        geotransform = raster.GetGeoTransform()
        originX = geotransform[0]
        originY = geotransform[3]
        pixelWidth = geotransform[1]
        pixelHeight = geotransform[5]
        cols = raster.RasterXSize
        rows = raster.RasterYSize
    
        driver = gdal.GetDriverByName('GTiff')
        outRaster = driver.Create(arq_sai, cols, rows, 1, gdal.GDT_Float32)
        outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
        outband = outRaster.GetRasterBand(1)
        outband.WriteArray(array)
        outRasterSRS = osr.SpatialReference()
        outRasterSRS.ImportFromWkt(raster.GetProjectionRef())
        outRaster.SetProjection(outRasterSRS.ExportToWkt())
        outband.FlushCache()


    def select_file(self):
        '''
        Opens a dialog window to select a raster file with
         * .tif extension
        '''
        # If the working directory does not exist, updates to the standard
        if not os.path.exists(self.direct):
            self.direct = os.path.dirname(__file__) + '\\Dados\\'

        # Collection and directory name that you want to work file
        arq_ent = unicode(QFileDialog.getOpenFileName(parent=self,
                    caption=self.tr("Select File GeoTif"),
                    directory=self.direct,
                    filter=self.tr("File GeoTif (*.tif)")))
        # Saves the directory and file name in the text line 'edInput'
        self.ui.edInput.setText(arq_ent)
        
        # Updates the Working Directory
        self.direct = os.path.dirname(arq_ent)
        ##############################################

        '''Meets the Minimum and Maximum values of the Matrix'''
        '''Checks if the input file exists'''
        if os.path.exists(arq_ent):
            try:
                # Convert Raster to array
                rasterArray = self.rasterTOarray(arq_ent)
                vl_min = rasterArray.min()
                vl_max = rasterArray.max()
                           
                '''Open the raster'''
                self.ui.lbMin.setText(unicode(vl_min))
                self.ui.lbMax.setText(unicode(vl_max))
            except:
                trace = traceback.format_exc()
                QMessageBox.critical(self, self.tr(u'Slicer'),
                    self.tr(u'The error occurred:\n' + trace),
                    buttons=QMessageBox.Ok,
                    defaultButton=QMessageBox.NoButton)

           
    def save_file(self):
        '''
        Opens a dialog window to save a .tif file with extension * .tif
        '''
        # If the working directory does not exist
        if not os.path.exists(self.direct):
            self.direct = os.path.dirname(__file__) + '\\Dados\\'
            
        # Collection directory and filename to save
        arq_sai = unicode(QFileDialog.getSaveFileName(parent=self,
                    caption=self.tr("Save File geoTif"),
                    directory=self.direct,
                    filter=self.tr("File GeoTif (*.tif)")))
        # Saves the directory and file name in the edit
        self.ui.edOutput.setText(arq_sai)
    
        # Updates the Working Directory
        self.direct = os.path.dirname(arq_sai)

