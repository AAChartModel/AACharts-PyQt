from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AAMarker import AAMarker


class AADataElement:
    name: str
    x: float
    y: float
    color: str
    dataLabels: AADataLabels
    marker: AAMarker
    
    def nameSet(self, prop: str):
        self.name = prop
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
   
    
    def dataLabelsSet(self, prop: AADataLabels):
        self.dataLabels = prop
        return self
   
    
    def markerSet(self, prop: AAMarker):
        self.marker = prop
        return self
   

