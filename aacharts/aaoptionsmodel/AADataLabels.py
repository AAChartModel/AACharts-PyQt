
from aacharts.aaenum.AAEnum import AAChartAlignType, AAChartVerticalAlignType
from aacharts.aaoptionsmodel.AAStyle import AAStyle
from aacharts.aatool.AAStringPurer import AAStringPurer


class AADataLabels:
    enabled: bool
    align: AAChartAlignType
    style: AAStyle
    format: str
    formatter: str
    rotation: float
    allowOverlap: bool
    useHTML: bool
    distance: str
    verticalAlign: AAChartVerticalAlignType
    x: float
    y: float
    color: str
    backgroundColor: str
    borderColor: str
    borderRadius: float
    borderWidth: float
    shape: str
    crop: bool
    inside: bool
    overflow: str
    softConnector: bool
    textPath: map
    filter: map
    connectorColor: str
    connectorPadding: float
    connectorShape: str
    connectorWidth: float
    crookDistance: str
    alignTo: str

    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self
   
    
    def alignSet(self, prop: AAChartAlignType):
        self.align = prop
        return self
   
    
    def styleSet(self, prop: AAStyle):
        self.style = prop
        return self
   
    
    def formatSet(self, prop: str):
        self.format = prop
        return self
   
    
    def formatterSet(self, prop: str):
        if (prop != None):
             self.formatter = AAStringPurer.pureJSString(prop)
        return self
   
    
    def rotationSet(self, prop: float):
        self.rotation = prop
        return self
   
    
    def allowOverlapSet(self, prop: bool):
        self.allowOverlap = prop
        return self
   
    
    def useHTMLSet(self, prop: bool):
        self.useHTML = prop
        return self
   
    
    def distanceSet(self, prop: str):
        self.distance = prop
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
   
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
   
    
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
   
    
    def shapeSet(self, prop: str):
        self.shape = prop
        return self
   
    
    def cropSet(self, prop: bool):
        self.crop = prop
        return self
   
    
    def insideSet(self, prop: bool):
        self.inside = prop
        return self
   
    
    def overflowSet(self, prop: str):
        self.overflow = prop
        return self
   
    
    def softConnectorSet(self, prop: bool):
        self.softConnector = prop
        return self
   
    
    def textPathSet(self, prop: map):
        self.textPath = prop
        return self
   
    
    def filterSet(self, prop: map):
        self.filter = prop
        return self
   
    
    def connectorColorSet(self, prop: str):
        self.connectorColor = prop
        return self
   
    
    def connectorPaddingSet(self, prop: float):
        self.connectorPadding = prop
        return self
   
    
    def connectorShapeSet(self, prop: str):
        self.connectorShape = prop
        return self
   
    
    def connectorWidthSet(self, prop: float):
        self.connectorWidth = prop
        return self
   
    
    def crookDistanceSet(self, prop: str):
        self.crookDistance = prop
        return self
   
    
    def alignToSet(self, prop: str):
        self.alignTo = prop
        return self


  
 

 