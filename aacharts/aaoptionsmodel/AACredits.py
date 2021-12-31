

from aacharts.aaenum.AAEnum import AAChartAlignType, AAChartVerticalAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle


class AAPosition:
    align: AAChartAlignType
    verticalAlign: AAChartVerticalAlignType
    x: float
    y: float

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


class AACredits:
    enabled: bool
    href: str
    position: AAPosition
    style: AAStyle
    text: str

    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self

    def hrefSet(self, prop: str):
        self.href = prop
        return self

    def positionSet(self, prop: AAPosition):
        self.position = prop
        return self

    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self

    def textSet(self, prop: str):
        self.text = prop
        return self




 
 