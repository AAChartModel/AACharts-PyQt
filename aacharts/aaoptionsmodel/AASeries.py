

from typing import List
from aacharts.aaenum.AAEnum import AAChartStackingType
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AAMarker import AAMarker
from aacharts.aaoptionsmodel.AAShadow import AAShadow
from aacharts.aaoptionsmodel.AAStates import AAStates
from aacharts.aaoptionsmodel.AAAnimation import AAAnimation
from aacharts.aatool.AAStringPurer import AAStringPurer


class AAPointEvents:
    click: str
    mouseOver: str
    remove: str
    select: str
    unselect: str
    update: str

    def clickSet(self, prop: str):
        if (prop != None):
            self.click = AAStringPurer.pureJSString(prop)
        return self


    def mouseOverSet(self, prop: str):
        if (prop != None):
            self.mouseOver = AAStringPurer.pureJSString(prop)
        return self


    def removeSet(self, prop: str):
        if (prop != None):
            self.remove = AAStringPurer.pureJSString(prop)
        return self


    def selectSet(self, prop: str):
        if (prop != None):
            self.select = AAStringPurer.pureJSString(prop)
        return self


    def unselectSet(self, prop: str):
        if (prop != None):
            self.unselect = AAStringPurer.pureJSString(prop)
        return self


    def updateSet(self, prop: str):
        if (prop != None):
            self.update = AAStringPurer.pureJSString(prop)
        return self


class AAPoint:
    events: AAPointEvents

    def eventsSet(self, prop: AAPointEvents):
        self.events = prop
        return self


class AAEvents:
    legendItemClick: str

    def legendItemClickSet(self, prop: str):
        if (prop != None):
            self.legendItemClick = AAStringPurer.pureJSString(prop)
        return self



class AASeries:
    borderRadius: float
    marker: AAMarker
    stacking: AAChartStackingType
    animation: AAAnimation
    keys: List
    colorByPoint: bool
    connectNulls: bool #Whether reconnects the broken line of the chart
    events: AAEvents
    shadow: AAShadow
    dataLabels: AADataLabels
    states: AAStates
    allowPointSelect: bool
    point: AAPoint
    pointInterval: float
    pointIntervalUnit: str
    pointPlacement: str #String | Number
    pointStart: float
    pointPadding: float
    groupPadding: float


    def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self

    def markerSet(self, prop: AAMarker):
        self.marker = prop
        return self

    def stackingSet(self, prop: AAChartStackingType):
        self.stacking = prop
        return self

    def animationSet(self, prop: AAAnimation):
        self.animation = prop
        return self

    def keysSet(self, prop: List):
        self.keys = prop
        return self

    def colorByPointSet(self, prop: bool):
        self.colorByPoint = prop
        return self

    def connectNullsSet(self, prop: bool):
        self.connectNulls = prop
        return self

    def eventsSet(self, prop: AAEvents):
        self.events = prop
        return self

    def shadowSet(self, prop: AAShadow):
        self.shadow = prop
        return self

    def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self

    def statesSet(self, prop: AAStates):
        self.states = prop
        return self

    def pointSet(self, prop: AAPoint):
        self.point = prop
        return self

    def pointIntervalSet(self, prop: float):
        self.pointInterval = prop
        return self

    def pointIntervalUnitSet(self, prop: str):
        self.pointIntervalUnit = prop
        return self

    def pointPlacementSet(self, prop: str):
        self.pointPlacement = prop
        return self

    def pointStartSet(self, prop: float):
        self.pointStart = prop
        return self

    def pointPaddingSet(self, prop: float):
        self.pointPadding = prop
        return self

    def groupPaddingSet(self, prop: float):
        self.groupPadding = prop
        return self





 
 
 