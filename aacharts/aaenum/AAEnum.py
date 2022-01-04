from enum import Enum


class AAChartAnimationType(Enum):
    easeInQuad = "easeInQuad"
    easeOutQuad = "easeOutQuad"
    easeInOutQuad = "easeInOutQuad"
    easeInCubic = "easeInCubic"
    easeOutCubic = "easeOutCubic"
    easeInOutCubic = "easeInOutCubic"
    easeInQuart = "easeInQuart"
    easeOutQuart = "easeOutQuart"
    easeInOutQuart = "easeInOutQuart"
    easeInQuint = "easeInQuint"
    easeOutQuint = "easeOutQuint"
    easeInOutQuint = "easeInOutQuint"
    easeInSine = "easeInSine"
    easeOutSine = "easeOutSine"
    easeInOutSine = "easeInOutSine"
    easeInExpo = "easeInExpo"
    easeOutExpo = "easeOutExpo"
    easeInOutExpo = "easeInOutExpo"
    easeInCirc = "easeInCirc"
    easeOutCirc = "easeOutCirc"
    easeInOutCirc = "easeInOutCirc"
    easeOutBounce = "easeOutBounce"
    easeInBack = "easeInBack"
    easeOutBack = "easeOutBack"
    easeInOutBack = "easeInOutBack"
    elastic = "elastic"
    swingFromTo = "swingFromTo"
    swingFrom = "swingFrom"
    swingTo = "swingTo"
    bounce = "bounce"
    bouncePast = "bouncePast"
    easeFromTo = "easeFromTo"
    easeFrom = "easeFrom"
    easeTo = "easeTo"


class AAChartType(Enum):
    column = "column"
    bar = "bar"
    area = "area"
    areaspline = "areaspline"
    line = "line"
    spline = "spline"
    scatter = "scatter"
    pie = "pie"
    bubble = "bubble"
    pyramid = "pyramid"
    funnel = "funnel"
    columnrange = "columnrange"
    arearange = "arearange"
    areasplinerange = "areasplinerange"
    boxplot = "boxplot"
    waterfall = "waterfall"
    polygon = "polygon"
    gauge = "gauge"
    errorbar = "errorbar"

class AAChartZoomType(Enum):
    none = ""
    x = "x"
    y = "y"
    xy = "xy"

class AAChartStackingType(Enum):
    none = ""
    normal = "normal"
    percent = "percent"

class AAChartSymbolType(Enum):
    circle = "circle"
    square = "square"
    diamond = "diamond"
    triangle = "triangle"
    triangleDown = "triangle-down"

class AAChartSymbolStyleType(Enum):
    normal = "normal"
    innerBlank = "innerBlank"
    borderBlank = "borderBlank"

class AAChartLayoutType(Enum):
    horizontal = "horizontal"
    vertical = "vertical"

class AAChartAlignType(Enum):
    left = "left"
    center = "center"
    right = "right"

class AAChartVerticalAlignType(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"

class AAChartLineDashStyleType(Enum):
    solid = "Solid"
    shortDash = "ShortDash"
    shortDot = "ShortDot"
    shortDashDot = "ShortDashDot"
    shortDashDotDot = "ShortDashDotDot"
    dot = "Dot"
    dash = "Dash"
    longDash = "LongDash"
    dashDot = "DashDot"
    longDashDot = "LongDashDot"
    longDashDotDot = "LongDashDotDot"

class AAChartFontWeightType(Enum):
    thin = "thin"
    regular = "regular"
    bold = "bold"

class AAChartAxisType(Enum):
    linear = "linear"
    logarithmic = "logarithmic"
    datetime = "datetime"
    category = "category"

