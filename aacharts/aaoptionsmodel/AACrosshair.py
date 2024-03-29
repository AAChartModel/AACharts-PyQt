from aacharts.aaenum.AAEnum import AAChartLineDashStyleType

class AACrosshair:
     dashStyle: str
     color: str
     width: float
     zIndex: int
     
     def dashStyleSet(self, prop: AAChartLineDashStyleType):
         self.dashStyle = prop.value
         return self
     
     def colorSet(self, prop: str):
         self.color = prop
         return self
     
     def widthSet(self, prop: float):
         self.width = prop
         return self
     
     def zIndexSet(self, prop: int):
         self.zIndex = prop
         return self
     