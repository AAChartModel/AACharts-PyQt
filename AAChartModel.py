from enum import Enum


class AAChartAnimationType(Enum):
    EaseInQuad = "easeInQuad"
    EaseOutQuad = "easeOutQuad"
    EaseInOutQuad = "easeInOutQuad"
    EaseInCubic = "easeInCubic"
    EaseOutCubic = "easeOutCubic"
    EaseInOutCubic = "easeInOutCubic"
    EaseInQuart = "easeInQuart"
    EaseOutQuart = "easeOutQuart"
    EaseInOutQuart = "easeInOutQuart"
    EaseInQuint = "easeInQuint"
    EaseOutQuint = "easeOutQuint"
    EaseInOutQuint = "easeInOutQuint"
    EaseInSine = "easeInSine"
    EaseOutSine = "easeOutSine"
    EaseInOutSine = "easeInOutSine"
    EaseInExpo = "easeInExpo"
    EaseOutExpo = "easeOutExpo"
    EaseInOutExpo = "easeInOutExpo"
    EaseInCirc = "easeInCirc"
    EaseOutCirc = "easeOutCirc"
    EaseInOutCirc = "easeInOutCirc"
    EaseOutBounce = "easeOutBounce"
    EaseInBack = "easeInBack"
    EaseOutBack = "easeOutBack"
    EaseInOutBack = "easeInOutBack"
    Elastic = "elastic"
    SwingFromTo = "swingFromTo"
    SwingFrom = "swingFrom"
    SwingTo = "swingTo"
    Bounce = "bounce"
    BouncePast = "bouncePast"
    EaseFromTo = "easeFromTo"
    EaseFrom = "easeFrom"
    EaseTo = "easeTo"


class AAChartType(Enum):
    Column = "column"
    Bar = "bar"
    Area = "area"
    AreaSpline = "areaspline"
    Line = "line"
    Spline = "spline"
    Scatter = "scatter"
    Pie = "pie"
    Bubble = "bubble"
    Pyramid = "pyramid"
    Funnel = "funnel"
    Columnrange = "columnrange"
    Arearange = "arearange"
    Areasplinerange = "areasplinerange"
    Boxplot = "boxplot"
    Waterfall = "waterfall"


class AAChartSubtitleAlignType(Enum):
    Left = "left"
    Center = "center"
    Right = "right"


class AAChartZoomType(Enum):
    X = "x"
    Y = "y"
    XY = "xy"


class AAChartStackingType(Enum):
    Not = ""
    Normal = "normal"
    Percent = "percent"


class AAChartSymbolType(Enum):
    Circle = "circle"
    Square = "square"
    Diamond = "diamond"
    Triangle = "triangle"
    Triangle_down = "triangle-down"


class AAChartSymbolStyleType(Enum):
    Normal = "normal"
    InnerBlank = "innerBlank"
    BorderBlank = "borderBlank"


class AAChartLegendLayoutType(Enum):
    Horizontal = "horizontal"
    Vertical = "vertical"


class AAChartLegendAlignType(Enum):
    Left = "left"
    Center = "center"
    Right = "right"


class AAChartLegendVerticalAlignType(Enum):
    Top = "top"
    Middle = "middle"
    Bottom = "bottom"


class AALineDashStyleType(Enum):
    Solid = "Solid"
    ShortDash = "ShortDash"
    ShortDot = "ShortDot"
    ShortDashDot = "ShortDashDot"
    ShortDashDotDot = "ShortDashDotDot"
    Dot = "Dot"
    Dash = "Dash"
    LongDash = "LongDash"
    DashDot = "DashDot"
    LongDashDot = "LongDashDot"
    LongDashDotDot = "LongDashDotDot"


class AAChartModel:
    animationType = AAChartAnimationType.Bounce  # 动画类型
    animationDuration = 800  # 动画时间
    title = ""  # 标题内容
    subtitle = ""  # 副标题内容
    chartType = AAChartType.Line  # 图表类型
    stacking = AAChartStackingType.Not  # 堆积样式
    symbol = AAChartSymbolType.Circle  # 折线曲线连接点的类型："circle", "square", "diamond", "triangle","triangle-down"，默认是"circle"
    symbolStyle = AAChartSymbolStyleType.InnerBlank  # 折线或者曲线的连接点是否为空心的
    zoomType = AAChartZoomType.X  # 缩放类型 AAChartZoomTypeX表示可沿着 x 轴进行手势缩放
    inverted = False  # x 轴是否翻转(垂直)
    xAxisReversed = False  # x 轴翻转
    yAxisReversed = False  # y 轴翻转
    polar = False  # 是否极化图形(变为雷达图)
    marginLeft: 0  # 图表左边距
    marginRight: 0  # 图表右边距
    marginBottom: 0  # 图表底部边距
    dataLabelEnabled = True  # 是否显示数据
    xAxisLabelsEnabled = True  # x 轴是否显示数据
    categories: []  # x 轴是否显示数据
    xAxisGridLineWidth: 1  # x 轴网格线的宽度
    xAxisVisible = True  # x 轴是否显示
    yAxisVisible = True  # y 轴是否显示
    yAxisLabelsEnabled = True  # y 轴是否显示数据
    yAxisTitle = ""  # y 轴标题
    yAxisLineWidth: 1  # y 轴轴线的宽度
    yAxisGridLineWidth: 0.5  # y 轴网格线的宽度
    tooltipEnabled = True  # 是否显示浮动提示框(默认显示)
    tooltipValueSuffix = ""  # 浮动提示框单位后缀
    tooltipCrossHairs = True  # 是否显示准星线(默认显示)
    colorsTheme: ["#1e90ff", "#ef476f", "#ffd066", "#04d69f", "#25547c", ]  # 图表主题颜色数组
    series: []  # 图表的数据数组
    legendEnabled = True  # 是否显示图例
    legendLayout = AAChartLegendLayoutType.Horizontal  # 图例数据项的布局。布局类型： "horizontal" 或 "vertical" 即水平布局和垂直布局 默认是：horizontal.
    legendAlign = AAChartLegendAlignType.Center  # 设定图例在图表区中的水平对齐方式，合法值有left，center 和 right。
    legendVerticalAlign = AAChartLegendVerticalAlignType.Bottom  # 设定图例在图表区中的垂直对齐方式，合法值有 top，middle 和 bottom。垂直位置可以通过 y 选项做进一步设定。
    backgroundColor: "#FFFFFF"  # 图表背景色
    borderRadius: 0  # 柱状图长条图头部圆角半径(可用于设置头部的形状,仅对条形图,柱状图有效)
    markerRadius: 5  # 折线连接点的半径长度
    titleColor = "#000000"  # 标题颜色
    subtitleColor = "#000000"  # 副标题颜色
    axisColor = "#000000"  # x 轴和 y 轴文字颜色

    def animationType(self, prop):
        self.animationType = prop
        return self

    def animationDuration(self, prop):
        self.animationDuration = prop
        return self

    def title(self, prop):
        self.title = prop
        return self

    def subtitle(self, prop):
        self.subtitle = prop
        return self

    def chartType(self, prop):
        self.chartType = prop
        return self

    def stacking(self, prop):
        self.stacking = prop
        return self

    def symbol(self, prop):
        self.symbol = prop
        return self

    def symbolStyle(self, prop):
        self.symbolStyle = prop
        return self

    def zoomType(self, prop):
        self.zoomType = prop
        return self

    def inverted(self, prop):
        self.inverted = prop
        return self

    def xAxisReversed(self, prop):
        self.xAxisReversed = prop
        return self

    def yAxisReversed(self, prop):
        self.yAxisReversed = prop
        return self

    def tooltipCrossHairs(self, prop):
        self.tooltipCrossHairs = prop
        return self

    def polar(self, prop):
        self.polar = prop
        return self

    def dataLabelEnabled(self, prop):
        self.dataLabelEnabled = prop
        return self

    def xAxisLabelsEnabled(self, prop):
        self.xAxisLabelsEnabled = prop
        return self

    def categories(self, prop):
        self.categories = prop
        return self

    def xAxisGridLineWidth(self, prop):
        self.xAxisGridLineWidth = prop
        return self

    def yAxisGridLineWidth(self, prop):
        self.yAxisGridLineWidth = prop
        return self

    def yAxisLabelsEnabled(self, prop):
        self.yAxisLabelsEnabled = prop
        return self

    def yAxisTitle(self, prop):
        self.yAxisTitle = prop
        return self

    def colorsTheme(self, prop):
        self.colorsTheme = prop
        return self

    def legendEnabled(self, prop):
        self.legendEnabled = prop
        return self

    def legendLayout(self, prop):
        self.legendLayout = prop
        return self

    def legendAlign(self, prop):
        self.legendAlign = prop
        return self

    def legendVerticalAlign(self, prop):
        self.legendVerticalAlign = prop
        return self

    def backgroundColor(self, prop):
        self.backgroundColor = prop
        return self

    def borderRadius(self, prop):
        self.borderRadius = prop
        return self

    def markerRadius(self, prop):
        self.markerRadius = prop
        return self

    def seriesfff(self, prop):
        self.series = prop
        return self

# aaChartModel = AAChartModel()\
#     .chartType("area")\
#     .color("")\
#     .title("")\
#     .subtitle("")\
#     .backgroundColor("#ffffff").chartType("area")


# aaChartModel = (
# AAChartModel()
#     .chartType("area")
#     # .color("red")
#     .title("图表标题")
#     .subtitle("图表副标题")
#     .backgroundColor("black")
# )
#
# aaChartModel = (
#     AAChartModel()
#         .chartType("bar")
#         .colorsTheme(["#1e90ff", "#ef476f", "#ffd066", "#04d69f", "#25547c", ])  # Colors theme
#         # .axesTextColor("white")color
#         .title("")
#         # .dataLabelsEnabled(False)
#         # .tooltipValueSuffix("℃")
#         .animationType("bounce")
#         .backgroundColor("#22324c")
# To make the chart background color transparent, set backgroundColor to "rgba (0,0,0,0)" or "# 00000000". Also make sure `aaChartView!.IsClearBackgroundColor = true`

# )


# aaChartModel\
#     .title("主标题")
#     .subtitle("副标题")\
#     ;
# aaChartModel.title = "ChartTitle"
# aaChartModel.subtitle = "ChartSubtitle"
# aaChartModel.colorsTheme = ["#longlonglongSring","#longlonglongSring","#longlonglongSring",]
# # aaChartModel.animationType("animationTypeHahahahhahahahha")


# print(AAChartAnimationType.Bounce)
# print(AAChartAnimationType().EaseInBack)
# print(aaChartModel.se)
# print(aaChartModel)
#
# print(aaChartModel.colorsTheme)
# print(aaChartModel.animationType)
# print(aaChartModel.title)
