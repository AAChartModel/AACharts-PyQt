
from typing import List
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels

from aacharts.aaoptionsmodel.AAMarker import AAMarker
from aacharts.aaoptionsmodel.AAShadow import AAShadow
from aacharts.aaoptionsmodel.AAStates import AAStates
from aacharts.aaoptionsmodel.AATooltip import AATooltip
from aacharts.aaenum.AAEnum import AAChartLineDashStyleType, AAChartType


class AADataSorting:
    enabled: bool
    matchByName: bool
    
    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self
   
    
    def matchByNameSet(self, prop: bool):
        self.matchByName = prop
        return self



class AASeriesElement:
    type: str             #A chart type series. If the type option is not specified, it is inherited from `chart.type`.
    name: str             #The name of the series as shown in the legend, tooltip etc.
    data: List             #An array of data points for the series
    color: str               #The main color or the series. In line type series it applies to the line and the point markers unless otherwise specified. In bar type series it applies to the bars unless a color is specified per point. The default value is pulled from the options.colors array.
    lineWidth: float         #The line width, It is only valid for line, spline, area, areaspline, arearange and arearangespline chart types
    borderWidth: float        #The border width, It is only valid for column, bar, pie, columnrange, pyramid and funnel chart types
    borderColor: str        #The border color, It is only valid for column, bar, pie, columnrange, pyramid and funnel chart types
    fillColor: str           #The fill color, It is only valid for area, areaspline, arearange and arearangespline chart types
    fillOpacity: float        #The fill opacity, It is only valid for area, areaspline, arearange and arearangespline chart types. Note that when you set an explicit fillColor, the fillOpacity is not applied. Instead, you should define the opacity in the fillColor with an rgba color definition. Deafualt value：0.75.
    threshold: float         #The threshold, also called zero level or base level. For line type series self is only used in conjunction with negativeColor. default：0.
    negativeColor: str        #The color for the parts of the graph or points that are below the threshold
    negativeFillColor: str     #A separate color for the negative part of the area.
    dashStyle: str        #A name for the dash style to use for the graph. Applies only to series type having a graph, like line, spline, area and scatter in case it has a lineWidth.
    yAxis: int
    dataLabels: AADataLabels   #Individual data label for each point. The options are the same as the ones for `plotOptions.series.dataLabels`.
    marker: AAMarker         #Enable or disable the point marker. If null, the markers are hidden when the data is dense, and shown for more widespread data points.
    step: str               #Whether to apply steps to the line. Possible values are left, center and right.
    states: AAStates
    colorByPoint: bool        #When using automatic point colors pulled from the `options.colors` collection, self option determines whether the chart should receive one color per series or one color per point.
    allowPointSelect: bool     #Allow self series' points to be selected by clicking on the markers, bars or pie slices
    zIndex: int              #Define the visual z index of the series.
    size: str               #The innder size for pie chart (String | Number)
    innerSize: str           #The innder size for pie chart (String | Number)
    minSize: str             #The minimum size for a pie in response to auto margins, Only useful for pie, bubble, funnel, Pyramid (String | Number)
    shadow: AAShadow
    zones: List
    zoneAxis: str         #Defines the Axis on which the zones are applied. defalut value：y.
    stack: str
    tooltip: AATooltip
    pointPlacement: str
    enableMouseTracking: bool
    dataSorting: AADataSorting
    reversed: bool           #Only useful for pyramid chart and funnel chart
    
    def typeSet(self, prop: AAChartType):
        self.type = prop
        return self
   
    
    def nameSet(self, prop: str):
        self.name = prop
        return self
   
    
    def dataSet(self, prop: List):
        self.data = prop
        return self
   
    
    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self
   
    
    def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
   
    
    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self
   
    
    def fillColorSet(self, prop: str):
        self.fillColor = prop
        return self
   
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
   
    
    def fillOpacitySet(self, prop: float):
        self.fillOpacity = prop
        return self
   
    
    def thresholdSet(self, prop: float):
        self.threshold = prop
        return self
   
    
    def negativeColorSet(self, prop: str):
        self.negativeColor = prop
        return self
   
    
    def negativeFillColorSet(self, prop: str):
        self.negativeFillColor = prop
        return self
   
    
    def dashStyleSet(self, prop: AAChartLineDashStyleType):
        self.dashStyle = prop
        return self
   
    
    def yAxisSet(self, prop: int):
        self.yAxis = prop
        return self
   
    
    def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
   
    
    def markerSet(self, prop: AAMarker):
        self.marker = prop
        return self
   
    
    def stepSet(self, prop: str):
        self.step = prop
        return self
   
    
    def statesSet(self, prop: AAStates):
        self.states = prop
        return self
   
    
    def colorByPointSet(self, prop: bool):
        self.colorByPoint = prop
        return self
   
    
    def allowPointSelectSet(self, prop: bool):
        self.allowPointSelect = prop
        return self
   
    
    def zIndexSet(self, prop: int):
        self.zIndex = prop
        return self
   
    
    def sizeSet(self, prop: str):
        self.size = prop
        return self
   
    
    def innerSizeSet(self, prop: str):
        self.innerSize = prop
        return self
   
    
    def minSizeSet(self, prop: str):
        self.minSize = prop
        return self
   
    def shadowSet(self, prop: AAShadow):
        self.shadow = prop
        return self
   
    
    def zonesSet(self, prop: List):
        self.zones = prop
        return self
   
    
    def zoneAxisSet(self, prop: str):
        self.zoneAxis = prop
        return self
   
    
    def stackSet(self, prop: str):
        self.stack = prop
        return self
   
    
    def tooltipSet(self, prop: AATooltip):
        self.tooltip = prop
        return self
    
    def pointPlacementSet(self, prop: str):
        self.pointPlacement = prop
        return self
   
    
    def enableMouseTrackingSet(self, prop: bool):
        self.enableMouseTracking = prop
        return self
   
    
    def dataSortingSet(self, prop: AADataSorting):
        self.dataSorting = prop
        return self
   
    
    def reversedSet(self, prop: bool):
        self.reversed = prop
        return self




