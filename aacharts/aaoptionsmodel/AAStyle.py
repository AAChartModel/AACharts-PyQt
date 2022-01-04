from aacharts.aaenum.AAEnum import *

class AAStyle:
    background: str
    backgroundColor: str
    border: str
    borderRadius: str
    color: str
    cursor: str
    fontFamily: str
    fontSize: str
    fontWeight: str
    height: float
    lineWidth: float
    opacity: float
    padding: str
    pointerEvents: str
    position: str
    textAlign: str
    textDecoration: str
    textOutline: str
    textOverflow: str
    top: str
    transition: str
    whiteSpace: str
    width: float

    def backgroundSet(self, prop: str):
        self.background = prop
        return self

    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self

    def borderSet(self, prop: str):
        self.border = prop
        return self

    def borderRadiusSet(self, prop: float):
        if (prop != None):
             self.borderRadius = f"{prop}px"
        return self

    def colorSet(self, prop: str):
        self.color = prop
        return self

    def cursorSet(self, prop: str):
        self.cursor = prop
        return self

    def fontFamilySet(self, prop: str):
        self.fontFamily = prop
        return self

    def fontSizeSet(self, prop: float):
        if (prop != None):
            self.fontSize = f"{prop}px"
        return self

    def fontWeightSet(self, prop: AAChartFontWeightType):
        if (prop != None):
            self.fontWeight = prop.value
        return self

    def heightSet(self, prop: float):
        self.height = prop
        return self

    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self

    def opacitySet(self, prop: float):
        self.opacity = prop
        return self

    def paddingSet(self, prop: float):
        if (prop != None):
            self.padding = f"{prop}px"
        return self

    def pointerEventsSet(self, prop: str):
        self.pointerEvents = prop
        return self

    def positionSet(self, prop: str):
        self.position = prop
        return self

    def textAlignSet(self, prop: str):
        self.textAlign = prop
        return self

    def textDecorationSet(self, prop: str):
        self.textDecoration = prop
        return self

    def textOutlineSet(self, prop: str):
        self.textOutline = prop
        return self

    def textOverflowSet(self, prop: str):
        self.textOverflow = prop
        return self

    def topSet(self, prop: str):
        self.top = prop
        return self

    def transitionSet(self, prop: str):
        self.transition = prop
        return self

    def whiteSpaceSet(self, prop: str):
        self.whiteSpace = prop
        return self

    def widthSet(self, prop: float):
        self.width = prop
        return self

    @staticmethod
    def colorStr(color: str):
        aaStyle = AAStyle.colorSize(color, None)
        return aaStyle

    @staticmethod
    def colorSize(color: str, fontSize: float):
        aaStyle = AAStyle.colorSizeWeight(color, fontSize, None)
        return aaStyle

    @staticmethod
    def colorSizeWeight(color: str, fontSize: float, weight: AAChartFontWeightType):
        aaStyle = AAStyle.colorSizeWeightOutline(color, fontSize, weight, None)
        return aaStyle

    @staticmethod
    def colorSizeWeightOutline(color: str, fontSize: float, weight: AAChartFontWeightType, outline: str):
        aaStyle = (AAStyle()
        .colorSet(color)
        .fontSizeSet(fontSize)
        .fontWeightSet(weight)
        .textOutlineSet(outline)
        )

        return aaStyle
        

        