

from aacharts.aaenum.AAEnum import AAChartLineDashStyleType
from aacharts.aaoptionsmodel.AALabel import AALabel


class AAPlotLinesElement:
    color: str
    dashStyle: str
    width: float
    value: float
    zIndex: int
    label: AALabel
     
    def colorSet(self, prop: str):
        self.color = prop
        return self
     
    def dashStyleSet(self, prop: AAChartLineDashStyleType):
        self.dashStyle = prop.value
        return self
     
    def widthSet(self, prop: float):
        self.width = prop
        return self
     
    def valueSet(self, prop: float):
        self.value = prop
        return self
     
    def zIndexSet(self, prop: int):
        self.zIndex = prop
        return self
     
    def labelSet(self, prop: AALabel):
        self.label = prop
        return self
     
 

 
 
 