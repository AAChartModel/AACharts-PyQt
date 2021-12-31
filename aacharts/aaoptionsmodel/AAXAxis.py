
from typing import List
from aacharts.aaenum.AAEnum import AAChartLineDashStyleType
from aacharts.aaoptionsmodel.AACrosshair import AACrosshair
from aacharts.aaoptionsmodel.AALabels import AALabels
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaenum.AAEnum import AAChartAxisType


class AADateTimeLabelFormats:
    millisecond: str
    second: str
    minute: str
    hour: str
    day: str
    week: str
    month: str
    year: str

    def millisecondSet(self, prop: str):
        self.millisecond = prop
        return self

    def secondSet(self, prop: str):
        self.second = prop
        return self

    def minuteSet(self, prop: str):
        self.minute = prop
        return self

    def hourSet(self, prop: str):
        self.hour = prop
        return self

    def daySet(self, prop: str):
        self.day = prop
        return self

    def weekSet(self, prop: str):
        self.week = prop
        return self

    def monthSet(self, prop: str):
        self.month = prop
        return self

    def yearSet(self, prop: str):
        self.year = prop
        return self


class AAXAxis:
    alternateGridColor: str
    title: AATitle
    type: str
    dateTimeLabelFormats: AADateTimeLabelFormats
    plotBands: List
    plotLines: List
    categories: List
    reversed: bool
    lineWidth: float # x-axis line width
    lineColor: str # x-axis line color
    linkedTo: int
    max: float # x-axis maximum
    min: float # x-axis minimum  (set to 0, there will be no negative numbers)
    minRange: int
    minTickInterval: int #The minimum tick interval allowed in axis values. For example on zooming in on an axis with daily data, self can be used to prevent the axis from showing hours. Defaults to the closest distance between two points on the axis.
    minorGridLineColor: str #Color of the minor, secondary grid lines.
    minorGridLineDashStyle: str #The dash or dot style of the minor grid lines.
    minorGridLineWidth: float #Width of the minor, secondary grid lines.
    minorTickColor: str #Color for the minor tick marks.
    minorTickInterval: str #*Specific tick interval in axis units for the minor ticks. On a linear axis, if "auto", the minor tick interval is calculated as a fifth of the tickInterval. If null or undefined, minor ticks are not shown.

    #On logarithmic axes, the unit is the power of the value. For example, setting the minorTickInterval to 1 puts one tick on each of 0.1, 1, 10, 100 etc. Setting the minorTickInterval to 0.1 produces 9 ticks between 1 and 10, 10 and 100 etc.

    #If user settings dictate minor ticks to become too dense, they don't make sense, and will be ignored to prevent performance problems.*/
    minorTickLength: float #The pixel length of the minor tick marks.
    minorTickPosition: str #The position of the minor tick marks relative to the axis line. Can be one of inside and outside. Defaults to outside.
    minorTickWidth: float #The pixel width of the minor tick mark.

    tickColor: str # Color of tick mark below x axis
    gridLineWidth: float # x-axis grid line width
    gridLineColor: str # x-axis grid line color
    gridLineDashStyle: str # x-axis grid line style
    offset: float # x-axis vertical offset
    labels: AALabels # Used to set the x-axis text related
    visible: bool # Used to set whether the x-axis and x-axis text are displayed
    opposite: bool # Whether to display the coordinate axis on the opposite surface. By default, the x axis is displayed below the chart, the y axis is on the left, the coordinate axis is displayed on the opposite surface, and the x axis is displayed on the top. The axis is displayed on the right (that is, the coordinate axis is displayed on the opposite side). This configuration is generally used for multi-axis display, and in Highstock, the y-axis is displayed on the opposite side by default. The default is: false.

    startOnTick: bool # Whether to force the axis to start on a tick. Use self option with the minPadding option to control the axis start. The default is false.
    endOnTick: bool# Whether to force the axis to end on a tick. Use self option with the minPadding option to control the axis end. The default is false.
    tickAmount: int
    tickInterval: float # Number of ticks on the x axis (set the X axis content every few points:
    crosshair: AACrosshair # Focus line style settings
    tickmarkPlacement: str # This parameter is only valid for the classification axis. When the value is on, the tick mark will be displayed above the classification when the value is between, the tick mark will be displayed between the two classifications. When tickInterval is 1, the default is between, otherwise it is on. The default is: null.
    tickWidth: float # The width of the axis tick marks. When set to 0, tick marks are not displayed.
    tickLength: float #/ The length of the axis tick marks. The default is: 10.
    tickPosition: str # Position of the tick line relative to the axis line. Available values ​​are "inside" and "outside", which represent the inside and outside of the axis line, respectively. The default is: "outside".
    tickPositions: List # Custom x-axis coordinates

    def alternateGridColorSet(self, prop: str):
        self.alternateGridColor = prop
        return self

    def titleSet(self, prop: AATitle):
        self.title = prop
        return self

    def typeSet(self, prop: AAChartAxisType):
        self.type = prop.value
        return self

    def dateTimeLabelFormatsSet(self, prop: AADateTimeLabelFormats):
        self.dateTimeLabelFormats = prop
        return self

    def plotBandsSet(self, prop: List):
        self.plotBands = prop
        return self

    def plotLinesSet(self, prop: List):
        self.plotLines = prop
        return self

    def categoriesSet(self, prop: List):
        self.categories = prop
        return self

    def reversedSet(self, prop: bool):
        self.reversed = prop
        return self

    def lineWidthSet(self, prop: float):
        self.lineWidth = prop
        return self

    def lineColorSet(self, prop: str):
        self.lineColor = prop
        return self

    def linkedToSet(self, prop: int):
        self.linkedTo = prop
        return self

    def maxSet(self, prop: float):
        self.max = prop
        return self

    def minSet(self, prop: float):
        self.min = prop
        return self

    def minRangeSet(self, prop: int):
        self.minRange = prop
        return self

    def minTickIntervalSet(self, prop: int):
        self.minTickInterval = prop
        return self

    def minorGridLineColorSet(self, prop: str):
        self.minorGridLineColor = prop
        return self

    def minorGridLineDashStyleSet(self, prop: AAChartLineDashStyleType):
        self.minorGridLineDashStyle = prop.value
        return self

    def minorGridLineWidthSet(self, prop: float):
        self.minorGridLineWidth = prop
        return self

    def minorTickColorSet(self, prop: str):
        self.minorTickColor = prop
        return self

    def minorTickIntervalSet(self, prop: str):
        self.minorTickInterval = prop
        return self

    def minorTickLengthSet(self, prop: float):
        self.minorTickLength = prop
        return self

    def minorTickPositionSet(self, prop: str):
        self.minorTickPosition = prop
        return self

    def minorTickWidthSet(self, prop: float):
        self.minorTickWidth = prop
        return self

    def tickColorSet(self, prop: str):
        self.tickColor = prop
        return self

    def gridLineWidthSet(self, prop: float):
        self.gridLineWidth = prop
        return self

    def gridLineColorSet(self, prop: str):
        self.gridLineColor = prop
        return self

    def gridLineDashStyleSet(self, prop: AAChartLineDashStyleType):
        self.gridLineDashStyle = prop.value
        return self

    def offsetSet(self, prop: float):
        self.offset = prop
        return self

    def labelsSet(self, prop: AALabels):
        self.labels = prop
        return self

    def visibleSet(self, prop: bool):
        self.visible = prop
        return self

    def oppositeSet(self, prop: bool):
        self.opposite = prop
        return self

    def startOnTickSet(self, prop: bool):
        self.startOnTick = prop
        return self

    def endOnTickSet(self, prop: bool):
        self.endOnTick = prop
        return self

    def tickAmountSet(self, prop: int):
        self.tickAmount = prop
        return self

    def tickIntervalSet(self, prop: float):
        self.tickInterval = prop
        return self

    def crosshairSet(self, prop: AACrosshair):
        self.crosshair = prop
        return self

    def tickmarkPlacementSet(self, prop: str):
        self.tickmarkPlacement = prop
        return self

    def tickWidthSet(self, prop: float):
        self.tickWidth = prop
        return self

    def tickLengthSet(self, prop: float):
        self.tickLength = prop
        return self

    def tickPositionSet(self, prop: str):
        self.tickPosition = prop
        return self

    def tickPositionsSet(self, prop: List):
        self.tickPositions = prop
        return self





