

from aacharts.aaenum.AAEnum import AAChartAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle


class AALabel:
    align: AAChartAlignType # Alignment of axis labels. Available values are "left", "center", and "right". The default value is intelligently judged based on the position of the coordinate axis (position in the chart), that is, the rotation angle of the label.
    rotation: float # The rotation angle of the axis label. The default is: 0.
    text: str # text
    textAlign: str # Text alignment
    useHTML: bool # Enable HTML rendering
    verticalAlign: str # Vertical alignment
    style: AAStyle # CSS style for axis labels
    x: float # The horizontal offset from the axis axis tick marks. The default is: 0.
    y: float # The vertical flat offset from the axis axis tick marks. The default is: null.     

    def alignSet(self, prop: AAChartAlignType):
        self.align = prop
        return self

    def rotationSet(self, prop: float):
        self.rotation = prop
        return self

    def textSet(self, prop: str):
        self.text = prop
        return self

    def textAlignSet(self, prop: str):
        self.textAlign = prop
        return self

    def useHTMLSet(self, prop: bool):
        self.useHTML = prop
        return self

    def verticalAlignSet(self, prop: str):
        self.verticalAlign = prop
        return self

    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self

    def xSet(self, prop: float):
        self.x = prop
        return self

    def ySet(self, prop: float):
        self.y = prop
        return self
     
     

 