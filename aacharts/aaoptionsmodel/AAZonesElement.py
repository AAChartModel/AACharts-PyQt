

from aacharts.aaenum.AAEnum import AAChartLineDashStyleType


class AAZonesElement:
    value: float
    color: str
    fillColor: str
    dashStyle: AAChartLineDashStyleType

    def valueSet(self, prop: float):
        self.value = prop
        return self
   
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
   
    
    def fillColorSet(self, prop: str):
        self.fillColor = prop
        return self
   
    
    def dashStyleSet(self, prop: AAChartLineDashStyleType):
        self.dashStyle = prop
        return self

