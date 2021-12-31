

from typing import List

from aacharts.aaoptionsmodel.AALegend import AALegend
from aacharts.aaoptionsmodel.AAPane import AAPane
from aacharts.aaoptionsmodel.AAPlotOptions import AAPlotOptions
from aacharts.aaoptionsmodel.AATooltip import AATooltip
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaoptionsmodel.AASubtitle import AASubtitle
from aacharts.aaoptionsmodel.AAChart import AAChart
from aacharts.aaoptionsmodel.AAXAxis import AAXAxis
from aacharts.aaoptionsmodel.AAYAxis import AAYAxis
from aacharts.aaoptionsmodel.AACredits import AACredits
from aacharts.aaoptionsmodel.AALang import AALang


class AAOptions:
    chart: AAChart
    title: AATitle
    subtitle: AASubtitle
    xAxis: AAXAxis
    yAxis: AAYAxis
    xAxisArray: List
    yAxisArray: List
    tooltip: AATooltip
    plotOptions: AAPlotOptions
    series: List
    legend: AALegend
    pane: AAPane
    colors: List
    credits: AACredits
    defaultOptions: AALang
    touchEventEnabled: bool
    
    def chartSet(self, prop: AAChart):
        self.chart = prop
        return self
   
    
    def titleSet(self, prop: AATitle):
        self.title = prop
        return self
   
    
    def subtitleSet(self, prop: AASubtitle):
        self.subtitle = prop
        return self
   
    
    def xAxisSet(self, prop: AAXAxis):
        self.xAxis = prop
        return self
   
    
    def yAxisSet(self, prop: AAYAxis):
        self.yAxis = prop
        return self
   
    
    def xAxisArraySet(self, prop: List):
        self.xAxisArray = prop
        return self
   
    
    def yAxisArraySet(self, prop: List):
        self.yAxisArray = prop
        return self
   
    
    def tooltipSet(self, prop: AATooltip):
        self.tooltip = prop
        return self
   
    
    def plotOptionsSet(self, prop: AAPlotOptions):
        self.plotOptions = prop
        return self
   
    
    def seriesSet(self, prop: List):
        self.series = prop
        return self
   
    
    def legendSet(self, prop: AALegend):
        self.legend = prop
        return self
   
    
    def paneSet(self, prop: AAPane):
        self.pane = prop
        return self
   
    
    def colorsSet(self, prop: List):
        self.colors = prop
        return self
   
    
    def creditsSet(self, prop: AACredits):
        self.credits = prop
        return self
   
    
    def defaultOptionsSet(self, prop: AALang):
        self.defaultOptions = prop
        return self
   
    
    def touchEventEnabledSet(self, prop: bool):
        self.touchEventEnabled = prop
        return self
   

 