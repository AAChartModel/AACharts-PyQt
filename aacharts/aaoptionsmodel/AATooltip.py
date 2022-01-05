

from aacharts.aaoptionsmodel.AAStyle import AAStyle
from aacharts.aaoptionsmodel.AAXAxis import AADateTimeLabelFormats
from aacharts.aatool.AAStringPurer import AAStringPurer


class AATooltip:
    backgroundColor: str
    borderColor: str
    borderRadius: float
    borderWidth: float
    style: AAStyle
    enabled: bool = True
    useHTML: bool
    formatter: str
    headerFormat: str
    pointFormat: str
    footerFormat: str
    valueDecimals: int
    shared: bool
    valueSuffix: str
    followTouchMove: bool#https:#api.highcharts.com.cn/highcharts#chart.panning
    shadow: bool
    padding: float
    pointFormatter: str
    positioner: str
    dateTimeLabelFormats: AADateTimeLabelFormats
    
    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self
   
    
    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self
   
    
    def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self
   
    
    def borderWidthSet(self, prop: float):
        self.borderWidth = prop
        return self
   
    
    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self
   
    
    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self
   
    
    def useHTMLSet(self, prop: bool):
        self.useHTML = prop
        return self
   
    
    def formatterSet(self, prop: str):
        self.formatter = AAStringPurer.pureJSString(prop)
        return self
   
    
    def headerFormatSet(self, prop: str):
        self.headerFormat = prop
        return self
   
    
    def pointFormatSet(self, prop: str):
        self.pointFormat = prop
        return self
   
    
    def footerFormatSet(self, prop: str):
        self.footerFormat = prop
        return self
   
    
    def valueDecimalsSet(self, prop: int):
        self.valueDecimals = prop
        return self
   
    
    def sharedSet(self, prop: bool):
        self.shared = prop
        return self
   
    
    def valueSuffixSet(self, prop: str):
        self.valueSuffix = prop
        return self
   
    
    def followTouchMoveSet(self, prop: bool):
        self.followTouchMove = prop
        return self
   
    
    def shadowSet(self, prop: bool):
        self.shadow = prop
        return self
   
    
    def paddingSet(self, prop: float):
        self.padding = prop
        return self
   
    
    def pointFormatterSet(self, prop: str):
        self.pointFormatter = AAStringPurer.pureJSString(prop)
        return self
   
    
    def positionerSet(self, prop: str):
        self.positioner = AAStringPurer.pureJSString(prop)
        return self
   
    
    def dateTimeLabelFormatsSet(self, prop: AADateTimeLabelFormats):
        self.dateTimeLabelFormats = prop
        return self

    
