
from aacharts.aaenum.AAEnum import AAChartAlignType, AAChartVerticalAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle


class AASubtitle:
    text: str
    style: AAStyle
    align: AAChartAlignType
    verticalAlign: AAChartVerticalAlignType
    x: float
    y: float
    userHTML: bool
     
    def textSet(self, prop: str):
        self.text = prop
        return self
     
    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self
     
    def alignSet(self, prop: AAChartAlignType):
        self.align = prop
        return self
     
    def verticalAlignSet(self, prop: AAChartVerticalAlignType):
        self.verticalAlign = prop
        return self
     
    def xSet(self, prop: float):
        self.x = prop
        return self
     
    def ySet(self, prop: float):
        self.y = prop
        return self
     
    def userHTMLSet(self, prop: bool):
        self.userHTML = prop
        return self

 
 