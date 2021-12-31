from aacharts.aachartcreator.AAChartModel import AAChartType, AAChartZoomType
from typing import List
from aacharts.aaoptionsmodel.AAAnimation import AAAnimation
from aacharts.aaoptionsmodel.AAScrollablePlotArea import AAScrollablePlotArea


class AAChart:
    type: str
    backgroundColor: str
    plotBackgroundImage: str
    pinchType: str
    panning: bool
    panKey: str
    polar: bool
    animation: AAAnimation
    inverted: bool
    margin: List
    marginTop: float # 👆
    marginRight: float # 👉
    marginBottom: float # 👇
    marginLeft: float # 👈
    spacing: List
    spacingTop: float # 👆
    spacingRight: float # 👉
    spacingBottom: float # 👇
    spacingLeft: float # 👈
    scrollablePlotArea: AAScrollablePlotArea
    # resetZoomButton: AAResetZoomButton?

    def typeSet(self, prop: AAChartType):
        self.type = prop.value
        return self
    
    

    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self
    
    

    def plotBackgroundImageSet(self, prop: str):
        self.plotBackgroundImage = prop
        return self
    
    

    def pinchTypeSet(self, prop: AAChartZoomType):
        # self.pinchType = prop._name_
        return self
    
    

    def panningSet(self, prop: bool):
        self.panning = prop
        return self
    
    

    def panKeySet(self, prop: str):
        self.panKey = prop
        return self
    
    

    def polarSet(self, prop: bool):
        self.polar = prop
        return self
    
    

    def animationSet(self, prop: AAAnimation):
        self.animation = prop
        return self
    
    

    def invertedSet(self, prop: bool):
        self.inverted = prop
        return self
    
    

    def marginSet(self, prop: List):
        self.margin = prop
        return self
    
    

    def marginTopSet(self, prop: float):
        self.marginTop = prop
        return self
    
    

    def marginRightSet(self, prop: float):
        self.marginRight = prop
        return self
    
    

    def marginBottomSet(self, prop: float):
        self.marginBottom = prop
        return self
    
    

    def marginLeftSet(self, prop: float):
        self.marginLeft = prop
        return self
    
    

    def spacingSet(self, prop: List):
        self.spacing = prop
        return self
    
    

    def spacingTopSet(self, prop: float):
        self.spacingTop = prop
        return self
    
    

    def spacingRightSet(self, prop: float):
        self.spacingRight = prop
        return self
    
    

    def spacingBottomSet(self, prop: float):
        self.spacingBottom = prop
        return self
    
    

    def spacingLeftSet(self, prop: float):
        self.spacingLeft = prop
        return self
    
    

    def scrollablePlotAreaSet(self, prop: AAScrollablePlotArea):
        self.scrollablePlotArea = prop
        return self
    
    

    # def resetZoomButtonSet(self, prop: AAResetZoomButton):
    #     resetZoomButton = prop
    #     return self   