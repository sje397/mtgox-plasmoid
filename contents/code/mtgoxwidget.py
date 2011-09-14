# -*- coding: utf-8 -*-
# Copyright Scott Ellis 2011 (sje397@gmail.com)
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdecore import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
 
class MtGoxWidget(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.layout = QGraphicsGridLayout(self.applet)
        self.chart = Plasma.SignalPlotter(self.applet)
        self.chart.setUseAutoRange(False)
        self.chart.setVerticalRange(0.0, 20.0)
        self.chart.setHorizontalLinesCount(20)
        self.chart.addPlot(QColor(0,255,0))
        self.layout.addItem(self.chart, 0, 0)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        self.resize(200, 150)
        self.setHasConfigurationInterface(False)
        self.chart.setTitle("MtGox Ticker")
        self.connectToEngine()
  
    def connectToEngine(self):
        self.mtgoxEngine = self.dataEngine("plasma-dataengine-mtgox")
        print "Engine is: ", self.mtgoxEngine
        #self.mtgoxEngine = self.dataEngine("time")
        self.mtgoxEngine.connectSource('Ticker', self, 2000)
        
    @pyqtSignature("dataUpdated(const QString &, const Plasma::DataEngine::Data &)")
    def dataUpdated(self, sourceName, data):
        price = data[QString("last")]
        self.chart.addSample([price,])
        

def CreateApplet(parent):
    return MtGoxWidget(parent)