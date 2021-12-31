
from aacharts.aaoptionsmodel.AALabel import AALabel


class AAPlotBandsElement:
    _from: float
    to: float
    color: str
    borderColor: str
    borderWidth: float
    className: str
    label: AALabel
    zIndex: int
    outerRadius: str
    thickness: str
     
     
    def fromSet(self, prop: float):
         self._from = prop
         return self
     
    def toSet(self, prop: float):
         self.to = prop
         return self
     
    def colorSet(self, prop: str):
         self.color = prop
         return self
     
    def borderColorSet(self, prop: str):
         self.borderColor = prop
         return self
     
    def borderWidthSet(self, prop: float):
         self.borderWidth = prop
         return self
     
    def classNameSet(self, prop: str):
         self.className = prop
         return self
     
    def labelSet(self, prop: AALabel):
         self.label = prop
         return self
     
    def zIndexSet(self, prop: int):
         self.zIndex = prop
         return self
     
    def outerRadiusSet(self, prop: str):
         self.outerRadius = prop
         return self
     
    def thicknessSet(self, prop: str):
         self.thickness = prop
         return self
       
 

 