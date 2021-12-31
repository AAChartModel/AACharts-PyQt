
from aacharts.aaenum.AAEnum import AAChartAlignType, AAChartFontWeightType, AAChartLayoutType, AAChartVerticalAlignType

class AAItemStyle:
     color: str
     cursor: str
     pointer: str
     fontSize: str
     fontWeight: AAChartFontWeightType
     
     def colorSet(self, prop: str):
          self.color = prop
          return self
     
     def cursorSet(self, prop: str):
          self.cursor = prop
          return self
     
     def pointerSet(self, prop: str):
          self.pointer = prop
          return self
     
     def fontSizeSet(self, prop: float):
          if (prop != None):
              self.fontSize = f"{prop}px"
          return self
     
     def fontWeightSet(self, prop: AAChartFontWeightType):
          self.fontWeight = prop
          return self
 

class AALegend:
    layout: AAChartLayoutType #The layout of the legend data items. Layout type: "horizontal" or "vertical" ie horizontal and vertical layout The default is: "horizontal".
    align: AAChartAlignType #Set the horizontal alignment of the legend in the chart area. Legal values are "left", "center", and "right".  The default is: "center".
    verticalAlign: AAChartVerticalAlignType #Set the vertical alignment of the legend in the chart area. Legal values are "top", "middle", and "bottom". The vertical position can be further set by the y option.The default is: "bottom".
    enabled: bool
    borderColor: str
    borderWidth: float
    itemMarginTop: float #The top margin of each item of the legend, in px. The default is: 0.
    itemMarginBottom: float#The bottom margin of each item of the legend, in px. The default is: 0.
    itemStyle: AAItemStyle
    symbolHeight: float
    symbolPadding: float
    symbolRadius: float
    symbolWidth: float
    x: float
    y: float
    floating: bool
     
    def layoutSet(self, prop: AAChartLayoutType):
          self.layout = prop
          return self
     
    def alignSet(self, prop: AAChartAlignType):
          self.align = prop
          return self
     
    def verticalAlignSet(self, prop: AAChartVerticalAlignType):
          self.verticalAlign = prop
          return self
     
    def enabledSet(self, prop: bool):
          self.enabled = prop
          return self
     
    def borderColorSet(self, prop: str):
          self.borderColor = prop
          return self
     
    def borderWidthSet(self, prop: float):
          self.borderWidth = prop
          return self
     
    def itemMarginTopSet(self, prop: float):
          self.itemMarginTop = prop
          return self
     
    def itemStyleSet(self, prop: AAItemStyle):
          self.itemStyle = prop
          return self
     
    def symbolHeightSet(self, prop: float):
          self.symbolHeight = prop
          return self
     
    def symbolPaddingSet(self, prop: float):
          self.symbolPadding = prop
          return self
     
    def symbolRadiusSet(self, prop: float):
          self.symbolRadius = prop
          return self
     
    def xSet(self, prop: float):
          self.x = prop
          return self
     
    def symbolWidthSet(self, prop: float):
          self.symbolWidth = prop
          return self
     
    def ySet(self, prop: float):
          self.y = prop
          return self
     
    def floatingSet(self, prop: bool):
          self.floating = prop
          return self
     
     
     

    

 