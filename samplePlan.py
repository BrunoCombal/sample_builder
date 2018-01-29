# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SampleBuilder
                                 A QGIS plugin
 Build a sampling plane
                              -------------------
        begin                : 2018-01-26
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Bruno Combal
        email                : bruno.combal@gmail.com
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

import os.path
from osgeo import ogr

#
# a samplePlan is defined by
# SRS, spatial extent
# object distribution: distribution type (random regular), distribution properties (spacing, number), sample type (point, rectangle, hexagon)
# file output
#
class samplePlan:
	def __init__(self):
		self.distributionType = 'random'
		self.distributionProperties = {'random':{'number':0, 'referenceRaster':u''}, 'regular':{'spacingX':None,'spacingY':None}}
		self.samplesType='point'
		self.samplesProperties = {'square':{'paddingX':None}, 'rectangle':{'paddingX':None,'paddingY':None},'hexagon':{'paddingX':None}}
		self.srs = 'epsg:4326'
		self.extent = None
		self.stratified=None # None, 'raster', 'vector'
		self.stratifiedProperties={'raster':{'file':u'','selectCode':None}, 'vector':{'file':u'','field':u'','value'=None}}
		self.outputFile = None
		self.outputFileType = None

		self.readyToWrite = False

	def setDistribution(self, type, properties):
		self.distributionType = type
		self.distributionProperties = properties

	# compute the sample point, assuming all parameters are set
	# lock conditions:
	# distributionProperties['random']['number']==0
	# distributionProperties['regular']['spacingX']==None
	# distributionProperties['regular']['spacingY'] is None
	# self.samplesProperties['point']['number']==0
	# self.samplesProperties['square']['paddingX'] is None
	# self.samplesProperties['rectance']['paddingX'] is None
	# self.samplesProperties['rectangle']['paddingY'] is None
	# self.samplesProperties['hexagon']['paddingY']==0
	def doSamplePoint(self):
		returnCode = True
		errorMsg = "Error, sample plan can't be generated."
		# check lock conditions
		if self.distributionType=='random':
			if self.distributionProperties['random']['number']==0:
				returnCode = False
				errorMsg += u'\nMissing number of random samples to draw.'
		if self.distributionType=='regular':
			if self.distributionProperties['regular']['spacingX'] is None:
				returnCode = False
				errorMsg += u'\nHorizontal spacing is not defined for the regular grid.'
			if self.distributionProperties['regular']['spacingY'] is None:
				returnCode = False
				errorMsg += u'\nVertical spacing is not defined for the regular grid.'
		if self.samplesType='square':
			if self.samplesProperties['square']['paddingX'] == 0:
				returnCode=False
				errorMsg += u'\nSquare dimension must be > 0.'
		if self.samplesType='rectangle':
			if self.samplesProperties['rectangle']['paddingX'] == 0:
				returnCode=False
				errorMsg += u'\nRectangle horizontal dimension must be >0.'
			if self.samplesProperties['rectangle']['paddingY'] == 0:
				returnCode=False
				errorMsg += u'\nRectangle vertical dimension must be >0.'
		if self.samplesType='hexagon':
			if self.samplesProperties['hexagon']['paddingX'] == 0:
				returnCode=False
				errorMsg += u'\nHexagon dimension must be >0'
		if self.stratified=='raster':
			if self.stratifiedProperties['raster']['file']==u'':
				returnCode=False
				errorMsg += u'\nStratification raster file is missing.'
			if self.stratifiedProperties['raster']['selectCode'] is None:
				returnCode=False
				errorMsg += u'\nChoose raster pixel value defining the strata to sample.'
		if self.stratified=='vector':
			if self.stratifiedProperties['vector']['file']==u'':
				returnCode=False
				errorMsg == u'\nStratification vector file is missing.'
			if self.stratifiedProperties['vector']['field']==u'':
				returnCode=False
				errorMsg += u'\nChoose stratification vector field to use.'
			if self.stratifiedProperties['vector']['value'] is None:
				returnCode=False
				errorMsg += u'\nDefine a value to define the strata from the selected field of the vector file.'

		# more tests to add

		if returnCode==False:
			self.readyToWrite = False
			return errorMsg

		if self.distributionType == 'random':
			if self.samplesType == 'point'
			self.doRandomPoint(self.samplesProperties, self.srs, self.extent)

	def doRandomPoint(self, properties, srs, extent):
		self.readyToWrite = False

		rangeX = []
		rangeY = []

		thisX = 


		# if success
		self.readyToWrite = True

	# to do: ensure a sampling plane was created
	def saveSampleToFile(self):
		pass


