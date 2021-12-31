
class AAScrollablePlotArea:
    minHeight: int
    minWidth: int
    opacity: float
    scrollPositionX: float
    scrollPositionY: float
     
    def minHeightSet(self, prop: int):
        self.minHeight = prop
        return self
     
    def minWidthSet(self, prop: int):
        self.minWidth = prop
        return self
     
    def opacitySet(self, prop: float):
        self.opacity = prop
        return self
     
    def scrollPositionXSet(self, prop: float):
        self.scrollPositionX = prop
        return self
     
    def scrollPositionYSet(self, prop: float):
        self.scrollPositionY = prop
        return self
     

 