from enum import Enum
from typing import List
from aacharts.aaoptionsmodel.AAStyle import AAStyle
from aacharts.aaenum.AAEnum import *
from aacharts.aaoptionsmodel.AAYAxis import AAYAxis
from aacharts.aaoptionsmodel.AALabels import AALabels
from aacharts.aaoptionsmodel.AAXAxis import AAXAxis
from aacharts.aaoptionsmodel.AALabels import AALabels
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AAMarker import AAMarker
from aacharts.aaoptionsmodel.AASeries import AASeries
from aacharts.aaoptionsmodel.AASubtitle import AASubtitle
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aaoptionsmodel.AATitle import AATitle
from aacharts.aaoptionsmodel.AAChart import AAChart
from aacharts.aaoptionsmodel.AATooltip import AATooltip
from aacharts.aaoptionsmodel.AAPlotOptions import AAPlotOptions
from aacharts.aaoptionsmodel.AAAnimation import AAAnimation
from aacharts.aaoptionsmodel.AALegend import AALegend
from aacharts.aaoptionsmodel.AACredits import AACredits
from aacharts.aaoptionsmodel.AAScrollablePlotArea import AAScrollablePlotArea


class AAChartModel:
    animationType: AAChartAnimationType = AAChartAnimationType.bounce # The type of chart animation
    animationDuration: int = None # The chart rendering animation duration
    title: str = None # The chart title
    titleStyle: AAStyle = None # The chart title style
    subtitle: str = None # The chart subtitle
    subtitleAlign: AAChartAlignType = None # The chart subtitle text align style
    subtitleStyle: AAStyle = None # The chart subtitle style
    chartType: AAChartType = AAChartType.column # The default series type for the chart. Can be any of the chart types listed under `AAChartType`. Defaults to line
    stacking: AAChartStackingType = AAChartStackingType.none # Whether to stack the values of each series on top of each other. Possible values are null to disable, "normal" to stack by value or "percent". When stacking is enabled, data must be sorted in ascending X order
    markerSymbol: AAChartSymbolType = AAChartSymbolType.circle # A predefined shape or symbol for the marker. When null, the symbol is pulled from options.symbols. Other possible values are "circle", "square", "diamond", "triangle" and "triangle-down"
    markerSymbolStyle: AAChartSymbolStyleType = None
    zoomType: AAChartZoomType = None # Decides in what dimensions the user can zoom by dragging the mouse. Can be one of x, y or xy
    inverted: bool = None # Whether to invert the axes so that the x axis is vertical and y axis is horizontal. When true, the x axis is reversed by default. If a bar series is present in the chart, it will be inverted automatically.Inverting the chart doesn't have an effect if there are no cartesian series in the chart, or if the chart is polar.Defaults to false
    xAxisReversed: bool = None # Whether to reverse the axis so that the highest number is closest to the origin. If the chart is inverted, the x axis is reversed by default. Defaults to false
    yAxisReversed: bool = None # Whether to reverse the axis so that the highest number is closest to the origin. If the chart is inverted, the x axis is reversed by default. Defaults to false
    crosshairs: bool = None # Enable or disable the crosshairs
    polar: bool = None # When true, cartesian charts like line, spline, area and column are transformed into the polar coordinate system. Requires `AAHighchartsMore.js`. Defaults to false
    margin: List = None
    dataLabelsEnabled: bool = None # Enable or disable the data labels. Defaults to false
    dataLabelsStyle: AAStyle = None # The data labels style
    xAxisLabelsEnabled: bool = None # Enable or disable the axis labels. Defaults to true
    xAxisLabelsStyle: AAStyle = None # The x axis labels style
    categories: List = None # Set new categories for the axis
    xAxisGridLineWidth: float = None # The width of the grid lines extending the ticks across the plot area.Defaults to 0
    xAxisVisible: bool = None # Show the x axis or not
    xAxisTickinterval: float = None # Custom x axis tick interval,It is useful when the x categories array is too long to show all of them
    yAxisVisible: bool = None # Show the y axis or not
    yAxisLabelsEnabled: bool = None # Enable or disable the axis labels. Defaults to true
    yAxisLabelsStyle: AAStyle = None # The y axis labels style
    yAxisTitle: str = None # The actual text of the axis title
    xAxisTitle: str = None # The actual text of the axis title
    yAxisLineWidth: float = None # The width of y axis line
    yAxisGridLineWidth: float = None # The width of the grid lines extending the ticks across the plot area. Defaults to 1
    yAxisMin: float = None # The y axis mini value
    yAxisMax: float = None # The y axis max value
    yAxisAllowDecimals: bool = None # The y axis values label allow decimals or not
    tooltipEnabled: bool = None # Show the tooltip or not
    tooltipValueSuffix: str = None # Custom tooltip value unit suffix
    colorsTheme: List = None # An array containing the default colors for the chart's series. When all colors are used, new colors are pulled from the start again. Defaults to: ["#bb250c","#f67210","#fde680","#257679","#f1c6c5"]
    series: List = None # An array of all the chart's series
    legendEnabled: bool = None # Enable or disable the legend. Defaults to true
    backgroundColor: str = None # The background color or gradient for the outer chart area. Defaults to #FFFFFF
    borderRadius: float = None # The corner radius of the outer chart border. Defaults to 0
    markerRadius: float = None # The radius of the point marker. Defaults to 4
    touchEventEnabled: bool = None # Support touch event call back or not
    scrollablePlotArea: AAScrollablePlotArea = None # Scroll properties if supported

    def animationTypeSet(self, prop: AAChartAnimationType):
        self.animationType = prop
        return self

    def animationDurationSet(self, prop: int):
        self.animationDuration = prop
        return self

    def titleSet(self, prop: str):
        self.title = prop
        return self

    def titleStyleSet(self, prop: AAStyle):
        self.titleStyle = prop
        return self

    def subtitleSet(self, prop: str):
        self.subtitle = prop
        return self

    def subtitleAlignSet(self, prop: AAChartAlignType):
        self.subtitleAlign = prop
        return self

    def subtitleStyleSet(self, prop: AAStyle):
        self.subtitleStyle = prop
        return self

    def chartTypeSet(self, prop: AAChartType):
        self.chartType = prop
        return self

    def stackingSet(self, prop: AAChartStackingType):
        self.stacking = prop
        return self

    def markerRadiusSet(self, prop: float):
        self.markerRadius = prop
        return self

    def markerSymbolSet(self, prop: AAChartSymbolType):
        self.markerSymbol = prop
        return self

    def markerSymbolStyleSet(self, prop: AAChartSymbolStyleType):
        self.markerSymbolStyle = prop
        return self

    def zoomTypeSet(self, prop: AAChartZoomType):
        self.zoomType = prop
        return self

    def invertedSet(self, prop: bool):
        self.inverted = prop
        return self

    def xAxisReversedSet(self, prop: bool):
        self.xAxisReversed = prop
        return self

    def yAxisReversedSet(self, prop: bool):
        self.yAxisReversed = prop
        return self

    def tooltipEnabledSet(self, prop: bool):
        self.tooltipEnabled = prop
        return self

    def tooltipValueSuffixSet(self, prop: str):
        self.tooltipValueSuffix = prop
        return self

    def polarSet(self, prop: bool):
        self.polar = prop
        return self

    def marginSet(self, top: float = 0, right: float = 0, bottom: float = 0, left: float = 0):
        self.margin = [top, right, bottom, left]
        return self

    def dataLabelsEnabledSet(self, prop: bool):
        self.dataLabelsEnabled = prop
        return self

    def dataLabelsStyleSet(self, prop: AAStyle):
        self.dataLabelsStyle = prop
        return self

    def xAxisLabelsEnabledSet(self, prop: bool):
        self.xAxisLabelsEnabled = prop
        return self

    def xAxisLabelsStyleSet(self, prop: AAStyle):
        self.xAxisLabelsStyle = prop
        return self

    def categoriesSet(self, prop: List):
        self.categories = prop
        return self

    def xAxisGridLineWidthSet(self, prop: float):
        self.xAxisGridLineWidth = prop
        return self

    def xAxisVisibleSet(self, prop: bool):
        self.xAxisVisible = prop
        return self

    def xAxisTickintervalSet(self, prop: float):
        self.xAxisTickinterval = prop
        return self

    def yAxisVisibleSet(self, prop: bool):
        self.yAxisVisible = prop
        return self

    def yAxisLabelsEnabledSet(self, prop: bool):
        self.yAxisLabelsEnabled = prop
        return self

    def yAxisLabelsStyleSet(self, prop: AAStyle):
        self.yAxisLabelsStyle = prop
        return self

    def yAxisTitleSet(self, prop: str):
        self.yAxisTitle = prop
        return self

    def xAxisTitleSet(self, prop: str):
        self.xAxisTitle = prop
        return self

    def yAxisLineWidthSet(self, prop: float):
        self.yAxisLineWidth = prop
        return self

    def yAxisMinSet(self, prop: float):
        self.yAxisMin = prop
        return self

    def yAxisMaxSet(self, prop: float):
        self.yAxisMax = prop
        return self

    def yAxisAllowDecimalsSet(self, prop: bool):
        self.yAxisAllowDecimals = prop
        return self

    def yAxisGridLineWidthSet(self, prop: float):
        self.yAxisGridLineWidth = prop
        return self

    def colorsThemeSet(self, prop: List):
        self.colorsTheme = prop
        return self

    def seriesSet(self, prop: List):
        self.series = prop
        return self

    def legendEnabledSet(self, prop: bool):
        self.legendEnabled = prop
        return self

    def backgroundColorSet(self, prop: str):
        self.backgroundColor = prop
        return self

    def borderRadiusSet(self, prop: float):
        self.borderRadius = prop
        return self

    def touchEventEnabledSet(self, prop: bool):
        self.touchEventEnabled = prop
        return self

    def scrollablePlotAreaSet(self, prop: AAScrollablePlotArea):
        self.scrollablePlotArea = prop
        return self


    def aa_toAAOptions(self):
        from aacharts.aachartcreator.AAOptionsComposer import AAOptionsComposer
        aaOptions = AAOptionsComposer.configureChartOptions(self)
        return aaOptions

