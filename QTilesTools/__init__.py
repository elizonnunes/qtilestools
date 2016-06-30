# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QTilesTools
                                 A QGIS plugin
 Tools to use QTiles outputs for offline base map use with QGIS and GeoODK Collect
                             -------------------
        begin                : 2016-06-30
        copyright            : (C) 2016 by Apropos Information Systems
        email                : tsw@aproposinfosystems.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QTilesTools class from file QTilesTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qtilestools import QTilesTools
    return QTilesTools(iface)
