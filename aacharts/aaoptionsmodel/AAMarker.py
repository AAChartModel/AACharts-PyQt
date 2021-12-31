class AAMarkerHover:
    enabled: bool
    fillColor: str
    lineColor: str
    lineWidth: float
    radius: float

    def enabledSet(self, prop: bool):
        self.enabled = prop
        return self

    def fillColorSet(self, prop: str):
        self.fillColor = prop
        return self

    def lineColorSet(self, prop: str):
        self.lineColor = prop
        return self

    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self

    def radiusSet(self, prop: float):
        self.radius = prop
        return self


class AAMarkerStates:
    hover: AAMarkerHover

    def hoverSet(self, prop: AAMarkerHover):
        self.hover = prop
        return self


class AAMarker:
    radius: float
    symbol: str
    fillColor: str
    lineWidth: float
    lineColor: str
    states: AAMarkerStates

    def radiusSet(self, prop: float):
        self.radius = prop
        return self

    def symbolSet(self, prop: str):
        self.symbol = prop
        return self

    def fillColorSet(self, prop: str):
        self.fillColor = prop
        return self

    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self

    def lineColorSet(self, prop: str):
        self.lineColor = prop
        return self

    def statesSet(self, prop: AAMarkerStates):
        self.states = prop
        return self
