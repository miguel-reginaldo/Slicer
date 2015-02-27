# -*- coding: utf-8 -*-
"""
/***************************************************************************
Slicer
                                 A QGIS plugin
 Grouping of pixels on a raster classes.
                             -------------------
        begin                : 2015-02-18
        copyright            : (C) 2014 by Miguel Reginaldo Teixeira da Silva
        email                : miguel.reginaldo@tsa.incra.gov.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    from slicer import Slicer
    return Slicer(iface)