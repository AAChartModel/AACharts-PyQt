
class AAShadow:
    color: str
    offsetX: float
    offsetY: float
    opacity: float
    width: float
    
    def colorSet(self, prop: str):
        self.color = prop
        return self
   
    
    def offsetXSet(self, prop: float):
        self.offsetX = prop
        return self
   
    
    def offsetYSet(self, prop: float):
        self.offsetY = prop
        return self
   
    
    def opacitySet(self, prop: float):
        self.opacity = prop
        return self
   
    
    def widthSet(self, prop: float):
        self.width = prop
        return self
