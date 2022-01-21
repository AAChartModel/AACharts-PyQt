from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType, AAChartSymbolType, AAChartSymbolStyleType
from aacharts.aatool.AAGradientColor import AAGradientColor, AALinearGradientDirection


class BasicChartComposer:
    @staticmethod
    def configureBasicOptions():
        return (
            AAChartModel()
                .backgroundColor("#4b2b7f")
                .dataLabelsEnabled(False)
                .yAxisGridLineWidth(0)
                .touchEventEnabled(True)
        )

    @staticmethod
    def configureAreaChart():
        element1 = (
            AASeriesElement()
                .name("Tokyo")
                .data([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6])
        )
        element2 = (
            AASeriesElement()
                .name("NewYork")
                .data([0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5])
        )
        element3 = (
            AASeriesElement()
                .name("London")
                .data([0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0])
        )
        element4 = (
            AASeriesElement()
                .name("Berlin")
                .data([3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8])
        )

        aaChartModel = (
            BasicChartComposer.configureBasicOptions()
                .chartType(AAChartType.area)
                .categories(["Java","Swift","Python","Ruby", "PHP","Go","C","C#","C++"])
                .series([element1, element2, element3, element4])
        )

        return aaChartModel


        def configureStepAreaChartAndStepLineChart():
            element1 = (
                AASeriesElement()
                    .name("Tokyo")
                    .step(True)
                    .data([149.9, 171.5, 106.4, 129.2, 144.0, 176.0, 135.6, 188.5, 276.4, 214.1, 95.6, 54.4])
            )

            element2 = (
                AASeriesElement()
                    .name("NewYork")
                    .step(True)
                    .data([83.6, 78.8, 188.5, 93.4, 106.0, 84.5, 105.0, 104.3, 131.2, 153.5, 226.6, 192.3])
            )

            element3 = (
                AASeriesElement()
                    .name("London")
                    .step(True)
                    .data([48.9, 38.8, 19.3, 41.4, 47.0, 28.3, 59.0, 69.6, 52.4, 65.2, 53.3, 72.2])
            )

            aaChartModel = (
                BasicChartComposer.configureBasicOptions()
                    .chartType(AAChartType.Area)
                    .series([element1, element2, element3,])
            )
            return aaChartModel


        def configureColumnChartAndBarChart():
            aaChartModel = (
                BasicChartComposer.configureAreaChart()
                    .categories([
                    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                ])
                    .legendEnabled(True)
                    .colorsTheme(["#fe117c","#ffc069","#06caf4","#7dffc0"])
                    .animationType(AAChartAnimationType.easeOutCubic)
                    .animationDuration(1200)
            )

            return aaChartModel


        def configureAreaChartAndAreasplineChartStyle(chartType: str):
            aaChartModel = (BasicChartComposer.configureAreaChart()
                            .animationType(AAChartAnimationType.easeOutQuart)
                            .legendEnabled(True)
                            .markerRadius(5)
                            .markerSymbol(AAChartSymbolType.circle)
                            .markerSymbolStyle(AAChartSymbolStyleType.innerBlank))

            if chartType == AAChartType.areaspline:
                gradientColorDic = AAGradientColor.linearGradient1(
                    AALinearGradientDirection.toBottomRight,
                    "rgba(138,43,226,1)",
                    "rgba(30,144,255,1)" #颜色字符串设置支持十六进制类型和 rgba 类型
                )

                element1 = (AASeriesElement()
                            .name("Predefined symbol")
                            .fillColor(gradientColorDic)
                            .data([0.45, 0.43, 0.50, 0.55, 0.58, 0.62, 0.83, 0.39, 0.56, 0.67, 0.50, 0.34, 0.50, 0.67, 0.58, 0.29, 0.46, 0.23, 0.47, 0.46, 0.38, 0.56, 0.48, 0.36]))

                element2 = (AASeriesElement()
                            .name("Image symbol")
                            .data([0.38, 0.31, 0.32, 0.32, 0.64, 0.66, 0.86, 0.47, 0.52, 0.75, 0.52, 0.56, 0.54, 0.60, 0.46, 0.63, 0.54, 0.51, 0.58, 0.64, 0.60, 0.45, 0.36, 0.67]))

                element3 = (AASeriesElement()
                            .name("Base64 symbol (*)")
                            .data([0.46, 0.32, 0.53, 0.58, 0.86, 0.68, 0.85, 0.73, 0.69, 0.71, 0.91, 0.74, 0.60, 0.50, 0.39, 0.67, 0.55, 0.49, 0.65, 0.45, 0.64, 0.47, 0.63, 0.64]))

                element4 = (AASeriesElement()
                            .name("Custom symbol")
                            .data([0.60, 0.51, 0.52, 0.53, 0.64, 0.84, 0.65, 0.68, 0.63, 0.47, 0.72, 0.60, 0.65, 0.74, 0.66, 0.65, 0.71, 0.59, 0.65, 0.77, 0.52, 0.53, 0.58, 0.53]))

                (aaChartModel
                 .animationType(AAChartAnimationType.easeFrom)#设置图表渲染动画类型为 EaseFrom
                 .series([element1, element2, element3, element4]))

            return aaChartModel

    def configureLineChartAndSplineChartStyle(chartType: AAChartType):
        aaChartModel = (BasicChartComposer.configureAreaChart()
                        .chartType(chartType)
                        .markerSymbolStyle(AAChartSymbolStyleType.borderBlank)#设置折线连接点样式为:边缘白色
                        .markerRadius(6))

        if chartType == AAChartType.spline:
            element1 = (AASeriesElement()
                        .name("Tokyo")
                        .lineWidth(7)
                        .data([50, 320, 230, 370, 230, 400,]))

            element2 = (AASeriesElement()
                        .name("Berlin")
                        .lineWidth(7)
                        .data([80, 390, 210, 340, 240, 350,]))

            element3 = (AASeriesElement()
                        .name("New York")
                        .lineWidth(7)
                        .data([100, 370, 180, 280, 260, 300,]))

            element4 = (AASeriesElement()
                        .name("London")
                        .lineWidth(7)
                        .data([130, 350, 160, 310, 250, 268,]))

            (aaChartModel
             .animationType(AAChartAnimationType.swingFromTo)
             .series([element1, element2, element3, element4]))

        return aaChartModel

