class AAHalo:
    attributes: map
    opacity: float
    size: float


    def attributesSet(self, prop: map):
        self.attributes = prop
        return self


    def opacitySet(self, prop: float):
        self.opacity = prop
        return self


    def sizeSet(self, prop: float):
        self.size = prop
        return self


class AAHover:
    enabled: bool
    borderColor: str
    brightness: float
    color: str
    halo: AAHalo
    lineWidth: float
    lineWidthPlus: float


    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self


    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self


    def brightnessSet(self, prop: float):
        self.brightness = prop
        return self


    def colorSet(self, prop: str):
        self.color = prop
        return self


    def haloSet(self, prop: AAHalo):
        self.halo = prop
        return self


    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self


    def lineWidthPlusSet(self, prop: float):
        self.lineWidthPlus = prop
        return self


class AASelect:
    enabled: bool
    borderColor: str
    color: str
    halo: AAHalo


    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self


    def borderColorSet(self, prop: str):
        self.borderColor = prop
        return self


    def colorSet(self, prop: str):
        self.color = prop
        return self


    def haloSet(self, prop: AAHalo):
        self.halo = prop
        return self




class AAInactive:
    enabled: bool
    opacity: float


    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self


    def opacitySet(self, prop: float):
        self.opacity = prop
        return self


class AAStates:
    hover: AAHover
    select: AASelect
    inactive: AAInactive

    def hoverSet(self, prop: AAHover):
        self.hover = prop
        return self

    def selectSet(self, prop: AASelect):
        self.select = prop
        return self

    def inactiveSet(self, prop: AAInactive):
        self.inactive = prop
        return self
     

 
