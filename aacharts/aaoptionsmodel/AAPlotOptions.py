
from typing import List
from aacharts.aaenum.AAEnum import AAChartType
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AASeries import AASeries

 
class AAColumn:
     name: str
     data: List
     color: str
     grouping: bool#Whether to group non-stacked columns or to let them render independent of each other. Non-grouped columns will be laid out individually and overlap each other. 默认是：true.
     pointPadding: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     pointPlacement: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     groupPadding: float#Padding between each value groups, in x axis units. 默认是：0.2.
     borderWidth: float
     colorByPoint: bool#对每个不同的点设置颜色(当图表类型为 AAColumn 时,设置为 AAColumn 对象的属性,当图表类型为 bar 时,应该设置为 bar 对象的属性才有效)
     dataLabels: AADataLabels
     stacking: str
     borderRadius: float
     yAxis: float
     
     def nameSet(self, prop: str):
        self.name = prop
        return self
     
     def dataSet(self, prop: List):
        self.data = prop
        return self
     
     def colorSet(self, prop: str):
        self.color = prop
        return self
     
     def groupingSet(self, prop: bool):
        self.grouping = prop
        return self
     
     def pointPaddingSet(self, prop: float):
        self.pointPadding = prop
        return self
     
     def pointPlacementSet(self, prop: float):
        self.pointPlacement = prop
        return self
     
     def groupPaddingSet(self, prop: float):
        self.groupPadding = prop
        return self
     
     def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
     
     def colorByPointSet(self, prop: bool):
        self.colorByPoint = prop
        return self
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     
     def stackingSet(self, prop: str):
        self.stacking = prop
        return self
     
     def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self
     
     def yAxisSet(self, prop: float):
        self.yAxis = prop
        return self
     

 
class AABar:
     name: str
     data: List
     color: str
     grouping: bool#Whether to group non-stacked columns or to let them render independent of each other. Non-grouped columns will be laid out individually and overlap each other. 默认是：true.
     pointPadding: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     pointPlacement: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     groupPadding: float#Padding between each value groups, in x axis units. 默认是：0.2.
     borderWidth: float
     colorByPoint: bool#对每个不同的点设置颜色(当图表类型为 AABar 时,设置为 AABar 对象的属性,当图表类型为 bar 时,应该设置为 bar 对象的属性才有效)
     dataLabels: AADataLabels
     stacking: str
     borderRadius: float
     yAxis: float
     
     def nameSet(self, prop: str):
        self.name = prop
        return self
     
     def dataSet(self, prop: List):
        self.data = prop
        return self
     
     def colorSet(self, prop: str):
        self.color = prop
        return self
     
     def groupingSet(self, prop: bool):
        self.grouping = prop
        return self
     
     def pointPaddingSet(self, prop: float):
        self.pointPadding = prop
        return self
     
     def pointPlacementSet(self, prop: float):
        self.pointPlacement = prop
        return self
     
     def groupPaddingSet(self, prop: float):
        self.groupPadding = prop
        return self
     
     def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
     
     def colorByPointSet(self, prop: bool):
        self.colorByPoint = prop
        return self
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     
     def stackingSet(self, prop: str):
        self.stacking = prop
        return self
     
     def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self
     
     def yAxisSet(self, prop: float):
        self.yAxis = prop
        return self
     

 
 
class AALine:
     dataLabels: AADataLabels
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     

 
class AASpline:
     dataLabels: AADataLabels
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     

 
class AAArea:
     dataLabels: AADataLabels
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     

 
class AAAreaspline:
     dataLabels: AADataLabels
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     

 
class AAPie:
     type: AAChartType
     data: List
     dataLabels:AADataLabels
     size: float
     allowPointSelect: bool
     cursor: str
     showInLegend: bool
     startAngle: float
     endAngle: float
     depth: float
     center: List
     
     def typeSet(self, prop: AAChartType):
        self.type = prop
        return self
     
     def dataSet(self, prop: List):
        self.data = prop
        return self
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     
     def sizeSet(self, prop: float):
        self.size = prop
        return self
     
     def allowPointSelectSet(self, prop: bool):
        self.allowPointSelect = prop
        return self
     
     def cursorSet(self, prop: str):
        self.cursor = prop
        return self
     
     def showInLegendSet(self, prop: bool):
        self.showInLegend = prop
        return self
     
     def startAngleSet(self, prop: float):
        self.startAngle = prop
        return self
     
     def endAngleSet(self, prop: float):
        self.endAngle = prop
        return self
     
     def depthSet(self, prop: float):
        self.depth = prop
        return self
     
     def centerSet(self, prop: List):
        self.center = prop
        return self
     
     

 
class AABubble:
     minSize: str # (String | Number)
     maxSize: str # (String | Number)
     zMin: float
     zMax: float
     dataLabels:AADataLabels
     
     def minSizeSet(self, prop: str):
        self.minSize = prop
        return self
     
     def maxSizeSet(self, prop: str):
        self.maxSize = prop
        return self
     
     def zMinSet(self, prop: float):
        self.zMin = prop
        return self
     
     def zMaxSet(self, prop: float):
        self.zMax = prop
        return self
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     

 
class AAColumnrange:
     borderRadius: float#The color of the border surrounding each column or bar
     borderWidth: float#The corner radius of the border surrounding each column or bar. default：0
     dataLabels: AADataLabels
     groupPadding: float#Padding between each value groups, in x axis units. 默认是：0.2.
     grouping: bool
     pointPadding: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     pointPlacement: float#Padding between each column or bar, in x axis units. 默认是：0.1.
     
     def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self
     
     def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
     
     def groupPaddingSet(self, prop: float):
        self.groupPadding = prop
        return self
     
     def groupingSet(self, prop: bool):
        self.grouping = prop
        return self

     def pointPaddingSet(self, prop: float):
        self.pointPadding = prop
        return self
     
     def pointPlacementSet(self, prop: float):
        self.pointPlacement = prop
        return self
     

 
class AAArearange:
     dataLabels: AADataLabels
     
     def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self


class AAPlotOptions:
     column: AAColumn
     bar: AABar
     line: AALine
     spline: AASpline
     area: AAArea
     areaspline: AAAreaspline
     pie: AAPie
     bubble: AABubble
     columnrange: AAColumnrange
     arearange: AAArearange
     series: AASeries 
         
     def columnSet(self, prop: AAColumn):
        self.column = prop
        return self
     
     def barSet(self, prop: AABar):
        self.bar = prop
        return self
     
     def lineSet(self, prop: AALine):
        self.line = prop
        return self
     
     def splineSet(self, prop: AASpline):
        self.spline = prop
        return self
     
     def areaSet(self, prop: AAArea):
        self.area = prop
        return self
     
     def areasplineSet(self, prop: AAAreaspline):
        self.areaspline = prop
        return self
     
     def pieSet(self, prop: AAPie):
        self.pie = prop
        return self
     
     def bubbleSet(self, prop: AABubble):
        self.bubble = prop
        return self
     
     def columnrangeSet(self, prop: AAColumnrange):
        self.columnrange = prop
        return self
     
     def arearangeSet(self, prop: AAArearange):
        self.arearange = prop
        return self
     
     def seriesSet(self, prop: AASeries):
        self.series = prop
        return self
     

 
 
 
 
 