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
from aacharts.aaoptionsmodel.AAPlotOptions import AAPlotOptions, AAColumnrange, AAPie
from aacharts.aaoptionsmodel.AAAnimation import AAAnimation
from aacharts.aaoptionsmodel.AALegend import AALegend
from aacharts.aaoptionsmodel.AACredits import AACredits
from aacharts.aaoptionsmodel.AAPlotOptions import AAColumn
from aacharts.aaoptionsmodel.AAPlotOptions import AABar
from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aaenum.AAEnum import *
from aacharts.aatool.AAColor import AAColor
from aacharts.aatool.AAStringPurer import AAStringPurer



class AAOptionsComposer:
    @staticmethod
    def configureChartOptions(aaChartModel: AAChartModel):
        aaChart = (AAChart()
            .typeSet(aaChartModel.chartType)
            .invertedSet(aaChartModel.inverted)
            .backgroundColorSet(aaChartModel.backgroundColor)
            .pinchTypeSet(aaChartModel.zoomType) #Set gesture zoom direction
            .panningSet(True) #Set whether gestures can be panned after zooming
            .polarSet(aaChartModel.polar) #Whether to polarize the chart (turn on polar mode)
            .scrollablePlotAreaSet(aaChartModel.scrollablePlotArea))
        aaChart.margin = aaChartModel.margin

        aaTitle = (AATitle()
            .textSet(aaChartModel.title)) #Title text content

        if aaChartModel.title != "":
            aaTitle.styleSet(aaChartModel.titleStyle)


        #ToDo Optimize in future
        aaSubtitle = (AASubtitle())
        if aaChartModel.subtitle != "":
            (aaSubtitle
                .textSet(aaChartModel.subtitle) #Subtitle text content
                .alignSet(aaChartModel.subtitleAlign) # The horizontal alignment of the chart subtitle text. Possible values are "left", "center", and "right". The default is(): "center".
                .styleSet(aaChartModel.subtitleStyle))


        aaTooltip = (AATooltip()
            .enabledSet(aaChartModel.tooltipEnabled)
            .sharedSet(True) #Multiple groups of data share the same tooltip
            .valueSuffixSet(aaChartModel.tooltipValueSuffix))

        aaPlotOptions = (AAPlotOptions()
            .seriesSet(AASeries()
                        .stackingSet(aaChartModel.stacking)))

        if aaChartModel.animationType != AAChartAnimationType.bounce:
            (aaPlotOptions.series
                .animationSet(AAAnimation()
                            .easingSet(aaChartModel.animationType)
                            .durationSet(aaChartModel.animationDuration)))


        AAOptionsComposer.configurePlotOptionsMarkerStyle(aaChartModel, aaPlotOptions)
        AAOptionsComposer.configurePlotOptionsDataLabels(aaPlotOptions, aaChartModel)

        aaLegend = (AALegend().enabledSet(aaChartModel.legendEnabled))

        aaOptions = (AAOptions()
            .chartSet(aaChart)
            .titleSet(aaTitle)
            .subtitleSet(aaSubtitle)
            .tooltipSet(aaTooltip)
            .plotOptionsSet(aaPlotOptions)
            .legendSet(aaLegend)
            .seriesSet(aaChartModel.series)
            .colorsSet(aaChartModel.colorsTheme)
            .touchEventEnabledSet(aaChartModel.touchEventEnabled))

        AAOptionsComposer.configureAxisContentAndStyle(aaOptions, aaChartModel)

        return aaOptions

    @staticmethod
    def configurePlotOptionsMarkerStyle(
        aaChartModel: AAChartModel,
        aaPlotOptions: AAPlotOptions
    ):
        aaChartType = aaChartModel.chartType

        #Data point markers related configuration. Only linear graphs have data point markers.
        if (   aaChartType == AAChartType.area
            or aaChartType == AAChartType.areaspline
            or aaChartType == AAChartType.line
            or aaChartType == AAChartType.spline
            or aaChartType == AAChartType.scatter
            or aaChartType == AAChartType.arearange
            or aaChartType == AAChartType.areasplinerange
            or aaChartType == AAChartType.polygon
            ):
            aaMarker = (AAMarker()
                .radiusSet(aaChartModel.markerRadius) #Curve connection point radius, default is 4
                .symbolSet(aaChartModel.markerSymbol)) #Curve connection point type(): "circle", "square", "diamond", "triangle", "triangle-down", the default is "circle"
            if aaChartModel.markerSymbolStyle == AAChartSymbolStyleType.innerBlank:
                (aaMarker
                    .fillColorSet(AAColor.white) #The fill color of the point (used to set the fill color of the polyline connection point)
                    # .lineWidthSet(0.4 * aaChartModel.markerRadius) #The width of the outer line (used to set the width of the outline stroke of the polyline connection point)
                    .lineColorSet("")) #The color of the outer edge (used to set the outline stroke color of the polyline connection point. When the value is an empty string, the color of the data point or data column is taken by default)
            elif aaChartModel.markerSymbolStyle == AAChartSymbolStyleType.borderBlank:
                (aaMarker
                    .lineWidthSet(2.0)
                    .lineColorSet(aaChartModel.backgroundColor))

            aaSeries = aaPlotOptions.series
            aaSeries.markerSet(aaMarker)


    @staticmethod
    def configurePlotOptionsDataLabels(
        aaPlotOptions: AAPlotOptions,
        aaChartModel: AAChartModel
    ):
        aaChartType = aaChartModel.chartType

        aaDataLabels = (AADataLabels()
            .enabledSet(aaChartModel.dataLabelsEnabled))
        if aaChartModel.dataLabelsEnabled == True:
            (aaDataLabels
                .styleSet(aaChartModel.dataLabelsStyle))



        if aaChartType == AAChartType.column:
            aaColumn = (AAColumn()
                .borderWidthSet(0)
                .borderRadiusSet(aaChartModel.borderRadius))
            if aaChartModel.polar == True:
                (aaColumn
                    .pointPaddingSet(0)
                    .groupPaddingSet(0.005))

            aaPlotOptions.columnSet(aaColumn)

        elif aaChartType == AAChartType.bar:
            aaBar = (AABar()
                .borderWidthSet(0)
                .borderRadiusSet(aaChartModel.borderRadius))
            if aaChartModel.polar == True:
                (aaBar
                    .pointPaddingSet(0)
                    .groupPaddingSet(0.005))

            aaPlotOptions.barSet(aaBar)

        elif aaChartType == AAChartType.pie:
            if aaChartModel.dataLabelsEnabled == True:
                aaDataLabels.formatSet("<b>point.name</b>(): point.percentage():.1f %")

            (aaPlotOptions
                .pieSet(AAPie()
                         .allowPointSelectSet(True)
                         .cursorSet("pointer")
                         .showInLegendSet(True)))

        elif aaChartType == AAChartType.columnrange:
            (aaPlotOptions
                .columnrangeSet(AAColumnrange()
                                 .borderRadiusSet(aaChartModel.borderRadius)
                                 .borderWidthSet(0)))

        aaPlotOptions.series.dataLabelsSet(aaDataLabels)

    @staticmethod
    def configureAxisContentAndStyle(
        aaOptions: AAOptions,
        aaChartModel: AAChartModel
    ):
        aaChartType = aaChartModel.chartType
        #The related configuration of the x-axis and the Y-axis, the fan, pyramid, funnel, and meter and dial charts do not need to set the relevant content of the X-axis and Y-axis
        if (   aaChartType == AAChartType.column
            or aaChartType == AAChartType.bar
            or aaChartType == AAChartType.area
            or aaChartType == AAChartType.areaspline
            or aaChartType == AAChartType.line
            or aaChartType == AAChartType.spline
            or aaChartType == AAChartType.scatter
            or aaChartType == AAChartType.bubble
            or aaChartType == AAChartType.columnrange
            or aaChartType == AAChartType.arearange
            or aaChartType == AAChartType.areasplinerange
            or aaChartType == AAChartType.boxplot
            or aaChartType == AAChartType.waterfall
            or aaChartType == AAChartType.polygon
            or aaChartType == AAChartType.gauge
            ):
            # if aaChartType != AAChartType.gauge:
            aaXAxisLabelsEnabled = aaChartModel.xAxisLabelsEnabled
            aaXAxisLabels = (AALabels()
                             .enabledSet(aaXAxisLabelsEnabled)) #Set whether the x-axis displays text
            if aaXAxisLabelsEnabled == True:
                (aaXAxisLabels
                 .styleSet(aaChartModel.xAxisLabelsStyle))


            aaXAxis = (AAXAxis()
                       .labelsSet(aaXAxisLabels)
                       .reversedSet(aaChartModel.xAxisReversed)
                       .gridLineWidthSet(aaChartModel.xAxisGridLineWidth) #x-axis grid line width
                       .categoriesSet(aaChartModel.categories)
                       .visibleSet(aaChartModel.xAxisVisible) #whether the x axis is visible
                       # .tickIntervalSet(aaChartModel.xAxisTickInterval) #Number of x-axis coordinate point intervals
                       .titleSet(AATitle()
                                 .textSet(aaChartModel.xAxisTitle))) #y axis title

            aaOptions.xAxisSet(aaXAxis)


            aaYAxisLabelsEnabled = aaChartModel.yAxisLabelsEnabled
            aaYAxisLabels = (AALabels()
                .enabledSet(aaChartModel.yAxisLabelsEnabled))
            if aaYAxisLabelsEnabled == True:
                (aaYAxisLabels
                    .styleSet(aaChartModel.yAxisLabelsStyle))


            aaYAxis = (AAYAxis()
                .labelsSet(aaYAxisLabels) #Set the y-axis text
                .minSet(aaChartModel.yAxisMin) #Set the minimum value of the y-axis. If the minimum value is equal to zero, negative values ​​cannot be displayed.
                .maxSet(aaChartModel.yAxisMax) #Maximum y-axis
                .allowDecimalsSet(aaChartModel.yAxisAllowDecimals) #Whether to display decimals
                .reversedSet(aaChartModel.yAxisReversed)
                .gridLineWidthSet(aaChartModel.yAxisGridLineWidth) #y-axis grid line width
                .lineWidthSet(aaChartModel.yAxisLineWidth) #Set the width of the y-axis axis, which is 0 to hide the y-axis axis
                .visibleSet(aaChartModel.yAxisVisible)
                .titleSet(AATitle()
                        .textSet(aaChartModel.yAxisTitle))) #y axis title

            aaOptions.yAxisSet(aaYAxis)




