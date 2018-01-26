# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SampleBuilder
                                 A QGIS plugin
 Build a sampling plane
                             -------------------
        begin                : 2018-01-26
        copyright            : (C) 2018 by Bruno Combal
        email                : bruno.combal@gmail.com
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
    """Load SampleBuilder class from file SampleBuilder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sample_builder import SampleBuilder
    return SampleBuilder(iface)
