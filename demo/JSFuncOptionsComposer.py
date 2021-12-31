
from aacharts.aatool.AAColor import AAColor
from aacharts.aatool.AAGradientColor import AAGradientColor
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.AAChartModel import AAChartModel, AAChartSymbolStyleType, AAChartSymbolType, AAChartType
from aacharts.aatool.AAGradientColor import AAGradientColor
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aachartcreator.AAChartModel import *
from aacharts.aaoptionsmodel.AAMarker import AAMarker
from aacharts.aaoptionsmodel.AADataElement import AADataElement
from aacharts.aaoptionsmodel.AADataLabels import AADataLabels
from aacharts.aaoptionsmodel.AACrosshair import AACrosshair
from aacharts.aaoptionsmodel.AAStates import AAStates, AAHover, AAHalo, AAInactive, AASelect
from aacharts.aaoptionsmodel.AALegend import AAItemStyle
from aacharts.aaoptionsmodel.AASeries import AAEvents, AAPoint, AAPointEvents
from aacharts.aaoptionsmodel.AALang import AALang
from aacharts.aatool.AAGradientColor import AALinearGradientDirection
from aacharts.aatool.AAJSArrayConverter import AAJSArrayConverter
from aacharts.aaoptionsmodel.AAPlotOptions import AAColumn
import random
from string import Template


class JSFuncOptionsComposer:
    @staticmethod
    def customAreaChartTooltipStyleWithSimpleFormatString():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.area)#图形类型
            .titleSet("近三个月金价起伏周期图")#图表主标题
            .subtitleSet("金价Set(元/克)")#图表副标题
            .markerSymbolStyleSet(AAChartSymbolStyleType.borderBlank)#折线连接点样式为外边缘空白
            .dataLabelsEnabledSet(False)
            .categoriesSet([
            "10-01", "10-02", "10-03", "10-04", "10-05", "10-06", "10-07", "10-08", "10-09", "10-10", "10-11",
            "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22",
            "10-23", "10-24", "10-25", "10-26", "10-27", "10-28", "10-29", "10-30", "10-31", "11-01", "11-02",
            "11-03", "11-04", "11-05", "11-06", "11-07", "11-08", "11-09", "11-10", "11-11", "11-12", "11-13",
            "11-14", "11-15", "11-16", "11-17", "11-18", "11-19", "11-20", "11-21", "11-22", "11-23", "11-24",
            "11-25", "11-26", "11-27", "11-28", "11-29", "11-30", "12-01", "12-02", "12-03", "12-04", "12-05",
            "12-06", "12-07", "12-08", "12-09", "12-10", "12-11", "12-12", "12-13", "12-14", "12-15", "12-16",
            "12-17", "12-18", "12-19", "12-20", "12-21", "12-22", "12-23", "12-24", "12-25", "12-26", "12-27",
            "12-28", "12-29", "12-30"
        ])
            .seriesSet([
            AASeriesElement()
                .nameSet("2020")
                .lineWidthSet(3)
                .colorSet("#FFD700")#纯金色
                .fillOpacitySet(0.5)
                .dataSet([
                1.51, 6.70, 0.94, 1.44, 1.60, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10,
                4.17, 3.85, 4.17, 3.46, 3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.51, 12.7, 0.94, 1.44,
                18.6, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10, 4.17, 3.85, 4.17, 3.46,
                3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.33, 4.68, 1.31, 1.10, 13.9, 1.10, 1.16, 1.67,
                2.64, 2.86, 3.00, 3.21, 4.14, 4.07, 3.68, 3.11, 3.41, 3.25, 3.32, 3.07, 3.92, 3.05,
                2.18, 3.24, 3.23, 3.15, 2.90, 1.81, 2.11, 2.43, 5.59, 3.09, 4.09, 6.14, 5.33, 6.05,
                5.71, 6.22, 6.56, 4.75, 5.27, 6.02, 5.48
            ])
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .formatterSet("""
    function () {
        return ' 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 <br/> '
        + ' Support JavaScript Function Just Right Now !!! <br/> '
        + ' The Gold Price For <b>2020 '
        +  this.x
        + ' </b> Is <b> '
        +  this.y
        + ' </b> Dollars ';
        }
             """)
         .valueDecimalsSet(2)#设置取值精确到小数点后几位#设置取值精确到小数点后几位
         .backgroundColorSet(AAColor.black)
         .borderColorSet(AAColor.black)
         .styleSet(AAStyle.colorSize("#FFD700", 12)))

        return aaOptions


    @staticmethod
    def customAreaChartTooltipStyleWithDifferentUnitSuffix():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.areaspline)#图形类型
            .titleSet("2014 ~ 2020 汪星人生存指数")#图表主标题
            .subtitleSet("数据来源：www.无任何可靠依据.com")#图表副标题
            .markerSymbolStyleSet(AAChartSymbolStyleType.innerBlank)
            .colorsThemeSet([
            AAGradientColor.oceanBlue,
            AAGradientColor.sanguine,
        ])
            .dataLabelsEnabledSet(False)
            .stackingSet(AAChartStackingType.normal)
            .seriesSet([
            AASeriesElement()
                .nameSet("🐶狗子")
                .lineWidthSet(5.0)
                .dataSet([0.45, 0.43, 0.50, 0.55, 0.58, 0.62, 0.83, 0.39, 0.56, 0.67, 0.50, 0.34, 0.50, 0.67, 0.58, 0.29, 0.46, 0.23, 0.47, 0.46, 0.38, 0.56, 0.48, 0.36])
            ,
            AASeriesElement()
                .nameSet("🌲树木")
                .lineWidthSet(5.0)
                .dataSet([0.38, 0.31, 0.32, 0.32, 0.64, 0.66, 0.86, 0.47, 0.52, 0.75, 0.52, 0.56, 0.54, 0.60, 0.46, 0.63, 0.54, 0.51, 0.58, 0.64, 0.60, 0.45, 0.36, 0.67])
            ,
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .enabledSet(True)
         .formatterSet("""
    function () {
        var s = '第' + '<b>' +  this.x + '</b>' + '年' + '<br/>';
        let colorDot1 = '<span style=\"' + 'color:#1e90ff; font-size:13px\"' + '>◉</span> ';
        let colorDot2 = '<span style=\"' + 'color:#ef476f; font-size:13px\"' + '>◉</span> ';
        let s1 = colorDot1  + this.points[0].series.name + ': ' + this.points[0].y + '只' + '<br/>';
        let s2 =  colorDot2 + this.points[1].series.name + ': ' + this.points[1].y + '棵';
        s += s1 + s2;
        return s;
    }
             """))

        #禁用图例点击事件
        aaOptions.plotOptions.series.events = (
            AAEvents()
                .legendItemClickSet("""
                        function() {
                          return false;
                        }
             """))

        return aaOptions


    @staticmethod
    def customAreaChartTooltipStyleWithColorfulHtmlLabels():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.areaspline)#图形类型
            .markerSymbolStyleSet(AAChartSymbolStyleType.borderBlank)#折线连接点样式为外边缘空白
            .dataLabelsEnabledSet(False)
            .colorsThemeSet(["#04d69f","#1e90ff","#ef476f","#ffd066",])
            .stackingSet(AAChartStackingType.normal)
            .markerRadiusSet(0)
            .seriesSet([
            AASeriesElement()
                .nameSet("Tokyo Hot")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([0.45, 0.43, 0.50, 0.55, 0.58, 0.62, 0.83, 0.39, 0.56, 0.67, 0.50, 0.34, 0.50, 0.67, 0.58, 0.29, 0.46, 0.23, 0.47, 0.46, 0.38, 0.56, 0.48, 0.36])
            ,
            AASeriesElement()
                .nameSet("Berlin Hot")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([0.38, 0.31, 0.32, 0.32, 0.64, 0.66, 0.86, 0.47, 0.52, 0.75, 0.52, 0.56, 0.54, 0.60, 0.46, 0.63, 0.54, 0.51, 0.58, 0.64, 0.60, 0.45, 0.36, 0.67])
            ,
            AASeriesElement()
                .nameSet("New York Hot")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([0.46, 0.32, 0.53, 0.58, 0.86, 0.68, 0.85, 0.73, 0.69, 0.71, 0.91, 0.74, 0.60, 0.50, 0.39, 0.67, 0.55, 0.49, 0.65, 0.45, 0.64, 0.47, 0.63, 0.64])
            ,
            AASeriesElement()
                .nameSet("London Hot")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([0.60, 0.51, 0.52, 0.53, 0.64, 0.84, 0.65, 0.68, 0.63, 0.47, 0.72, 0.60, 0.65, 0.74, 0.66, 0.65, 0.71, 0.59, 0.65, 0.77, 0.52, 0.53, 0.58, 0.53])
            ,
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .formatterSet("""
    function () {
        let wholeContentStr ='<span style=\"' + 'color:lightGray; font-size:13px\"' + '>◉ Time: ' + this.x + ' year</span><br/>';
        let length = this.points.length;
        for (let i = 0; i < length; i++) {
            let thisPoint = this.points[i];
            let yValue = thisPoint.y;
            if (yValue != 0) {
                let spanStyleStartStr = '<span style=\"' + 'color:'+ thisPoint.color + '; font-size:13px\"' + '>◉ ';
                let spanStyleEndStr = '</span> <br/>';
                wholeContentStr += spanStyleStartStr + thisPoint.series.name + ': ' + thisPoint.y + '℃' + spanStyleEndStr;
            }
        }
        return wholeContentStr;
    }
             """)
         .backgroundColorSet("#050505")
         .borderColorSet("#050505"))

        return aaOptions


    @staticmethod
    def customLineChartTooltipStyleWhenValueBeZeroDoNotShow():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.line)#图形类型
            .markerSymbolStyleSet(AAChartSymbolStyleType.borderBlank)#折线连接点样式为外边缘空白
            .dataLabelsEnabledSet(False)
            .categoriesSet(["临床一期","临床二期","临床三期"])
            .seriesSet([
            AASeriesElement()
                .nameSet("上市")
                .dataSet([0,0,7])
            ,
            AASeriesElement()
                .nameSet("中止")
                .dataSet([4,5,1])
            ,
            AASeriesElement()
                .nameSet("无进展")
                .dataSet([2,0,1])
            ,
            AASeriesElement()
                .nameSet("进行中")
                .dataSet([3,5,2])
            ,
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .formatterSet("""
    function () {
        let wholeContentStr = this.points[0].x + '<br/>';
        let length = this.points.length;
        for (let i = 0; i < length; i++) {
            let thisPoint = this.points[i];
            let yValue = thisPoint.y;
            if (yValue != 0) {
                let prefixStr = '<span style=\"' + 'color:'+ thisPoint.color + '; font-size:13px\"' + '>◉ ';
                wholeContentStr += prefixStr + thisPoint.series.name + ': ' + yValue + '<br/>';
            }
        }
        return wholeContentStr;
    }
             """))

        return aaOptions


    @staticmethod
    def customBoxplotTooltipContent():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.boxplot)
            .titleSet("BOXPLOT CHART")
            .subtitleSet("virtual data")
            .yAxisTitleSet("℃")
            .yAxisVisibleSet(True)
            .seriesSet([
            AASeriesElement()
                .nameSet("Observed Data")
                .colorSet("#ef476f")
                .fillColorSet(AAGradientColor.deepSea)
                .dataSet([
                [760, 801, 848, 895, 965],
                [733, 853, 939, 980, 1080],
                [714,  762, 817, 870, 918],
                [724, 802, 806, 871, 950],
                [834, 836, 864, 882, 910]
            ])
            ,
        ]))

        pointFormatStr = (
                "◉</span> <b> {series.name}</b><br/>"
                + "最大值: {point.high}<br/>"
                + "Q2: {point.q3}<br/>"
                + "中位数: {point.median}<br/>"
                + "Q1: {point.q1}<br/>"
                + "最小值: {point.low}<br/>"
        )

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .headerFormatSet("<em>实验号码： point.key</em><br/>")
         .pointFormatSet(pointFormatStr)
         .valueDecimalsSet(2)#设置取值精确到小数点后几位#设置取值精确到小数点后几位
         .backgroundColorSet(AAColor.black)
         .borderColorSet(AAColor.black)
         .styleSet(AAStyle.colorSize("#1e90ff", 12)))

        return aaOptions


    @staticmethod
    def customYAxisLabels():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.line)#图形类型
            .markerSymbolStyleSet(AAChartSymbolStyleType.borderBlank)#折线连接点样式为外边缘空白
            .dataLabelsEnabledSet(False)
            .colorsThemeSet(["#04d69f","#1e90ff","#ef476f","#ffd066",])
            .stackingSet(AAChartStackingType.normal)
            .markerRadiusSet(8)
            .seriesSet([
            AASeriesElement()
                .nameSet("Scores")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4])
            ,
        ]))

        aaYAxisLabels = (
            AALabels()
                .formatterSet("""
    function () {
        let yValue = this.value;
        if (yValue >= 200) {
            return "Excellent";
        } else if (yValue >= 150 && yValue < 200) {
            return "Very Good";
        } else if (yValue >= 100 && yValue < 150) {
            return "Good";
        } else if (yValue >= 50 && yValue < 100) {
            return "Not Bad";
        } else {
            return "Just So So";
        }
    }
                 """))

        aaOptions = aaChartModel.aa_toAAOptions()

        aaOptions.yAxis.labelsSet(aaYAxisLabels)

        return aaOptions


    @staticmethod
    def customYAxisLabels2():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.line)#图形类型
            .markerSymbolStyleSet(AAChartSymbolStyleType.borderBlank)#折线连接点样式为外边缘空白
            .dataLabelsEnabledSet(False)
            .colorsThemeSet(["#04d69f","#1e90ff","#ef476f","#ffd066",])
            .stackingSet(AAChartStackingType.normal)
            .markerRadiusSet(8)
            .seriesSet([
            AASeriesElement()
                .nameSet("Tokyo Hot")
                .lineWidthSet(5.0)
                .fillOpacitySet(0.4)
                .dataSet([229.9, 771.5, 1106.4, 1129.2, 6644.0, 1176.0, 8835.6, 148.5, 8816.4, 6694.1, 7795.6, 9954.4])
        ]))

        aaYAxisLabels = (
            AALabels()
                .styleSet(AAStyle.colorSizeWeight(AAColor.gray, 10, AAChartFontWeightType.bold))
                .formatterSet("""
    function () {
        let yValue = this.value;
        if (yValue == 0) {
            return "0";
        } else if (yValue == 2500) {
            return "25%";
        } else if (yValue == 5000) {
            return "50%";
        } else if (yValue == 7500) {
            return "75%";
        } else if (yValue == 10000) {
            return "100%";
        }
    }
                 """))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.yAxis
         .oppositeSet(True)
         .tickWidthSet(2)
         .lineWidthSet(1.5)#Y轴轴线颜色
         .lineColorSet(AAColor.lightGray)#Y轴轴线颜色
         .gridLineWidthSet(0)#Y轴网格线宽度
         .tickPositionsSet([0,2500,5000,7500,10000])
         .labelsSet(aaYAxisLabels))

        return aaOptions


    @staticmethod
    def customStackedAndGroupedColumnChartTooltip():
        aaChartModel = (AAChartModel()
            .titleSet("Total fruit consumtion, grouped by gender")
            .subtitleSet("stacked and grouped")
            .yAxisTitleSet("Number of fruits")
            .chartTypeSet(AAChartType.column)
            .legendEnabledSet(False)#隐藏图例Set(底部可点按的小圆点)
            .stackingSet(AAChartStackingType.normal)
            .categoriesSet(["Apples", "Oranges", "Pears","Grapes","Bananas",])
            .dataLabelsEnabledSet(True)
            .seriesSet([
            AASeriesElement()
                .nameSet("John")
                .dataSet([5,3,4,7,2,])
                .stackSet("male")
            ,
            AASeriesElement()
                .nameSet("Joe")
                .dataSet([3,4,4,2,5,])
                .stackSet("male")
            ,
            AASeriesElement()
                .nameSet("Jane")
                .dataSet([2,5,6,2,1,])
                .stackSet("female")
            ,
            AASeriesElement()
                .nameSet("Janet")
                .dataSet([3,0,4, 4,3,])
                .stackSet("female")
            ,
        ]))

        #/*Custom Tooltip Style --- 自定义图表浮动提示框样式及内容*/
        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .sharedSet(False)
         .formatterSet("""
            function () {
                return '<b>'
                + this.x
                + '</b><br/>'
                + this.series.name
                + ': '
                + this.y
                + '<br/>'
                + 'Total: '
                + this.point.stackTotal;
            }
                 """))

        return aaOptions


    @staticmethod
    def customDoubleXAxesChart():
        gradientColorDic1 = (AAGradientColor.linearGradient1(
            AALinearGradientDirection.toTop,
            "#7052f4",
            "#00b0ff"#颜色字符串设置支持十六进制类型和 rgba 类型
        ))

        gradientColorDic2 = (AAGradientColor.linearGradient1(
            AALinearGradientDirection.toTop,
            "#EF71FF",
            "#4740C8"#颜色字符串设置支持十六进制类型和 rgba 类型
        ))

        aaChart = (AAChart()
                   .typeSet(AAChartType.bar))

        aaTitle = (AATitle()
                   .textSet("2015 年德国人口金字塔")
                   .styleSet(AAStyle()
                             .colorSet(AAColor.black)
                             .fontSizeSet(12.0)))

        aaCategories = [
            "0-4", "5-9", "10-14", "15-19",
            "20-24", "25-29", "30-34", "35-39", "40-44",
            "45-49", "50-54", "55-59", "60-64", "65-69",
            "70-74", "75-79", "80-84", "85-89", "90-94",
            "95-99", "100 + "
        ]

        aaXAxis1 = (AAXAxis()
                    .reversedSet(True)
                    .categoriesSet(aaCategories)
                    .labelsSet(AALabels()
                               .stepSet(1)))

        aaXAxis2 = (AAXAxis()
                    .reversedSet(True)
                    .oppositeSet(True)
                    .categoriesSet(aaCategories)
                    .linkedToSet(0)
                    .labelsSet(AALabels()
                               .stepSet(1)))

        aaYAxis = (AAYAxis()
                   .gridLineWidthSet(0)# Y 轴网格线宽度
                   .titleSet(AATitle()
                             .textSet(""))#Y 轴标题
                   .labelsSet(AALabels()
                              .formatterSet("""
function () {
    return (Math.abs(this.value) / 1000000) + 'M';
}
                     """))
                   .minSet( -4000000)
                   .maxSet( 4000000))

        aaPlotOptions = (AAPlotOptions()
                         .seriesSet(AASeries()
                                    .animationSet(AAAnimation()
                                                  .durationSet(800)
                                                  .easingSet(AAChartAnimationType.bounce))
                                    .stackingSet(AAChartStackingType.normal)))

        aaTooltip = (AATooltip()
                     .enabledSet(True)
                     .sharedSet(False)
                     .formatterSet("""
function () {
    return '<b>' + this.series.name + ', age ' + this.point.category + '</b><br/>' +
        '人口: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);
}
                 """))

        aaSeriesElement1 = (AASeriesElement()
            .nameSet("Men")
            .colorSet(gradientColorDic1)
            .dataSet([
            -1746181, -1884428, -2089758, -2222362, -2537431, -2507081, -2443179,
            -2664537, -3556505, -3680231, -3143062, -2721122, -2229181, -2227768,
            -2176300, -1329968, -836804, -354784, -90569, -28367, -3878
        ]))

        aaSeriesElement2 = (AASeriesElement()
            .nameSet("Women")
            .colorSet(gradientColorDic2)
            .dataSet([
            1656154, 1787564, 1981671, 2108575, 2403438, 2366003, 2301402, 2519874,
            3360596, 3493473, 3050775, 2759560, 2304444, 2426504, 2568938, 1785638,
            1447162, 1005011, 330870, 130632, 21208
        ]))

        aaOptions = (AAOptions()
                     .chartSet(aaChart)
                     .titleSet(aaTitle)
                     .xAxisArraySet([aaXAxis1,aaXAxis2])
                     .yAxisSet(aaYAxis)
                     .plotOptionsSet(aaPlotOptions)
                     .tooltipSet(aaTooltip)
                     .seriesSet([aaSeriesElement1,aaSeriesElement2]))

        return aaOptions



    @staticmethod
    def customArearangeChartTooltip():
        aaChartModel = (AAChartModel()
            .titleSet("LANGUAGE MARKET SHARES JANUARY,2020 TO MAY")
            .subtitleSet("virtual data")
            .chartTypeSet(AAChartType.arearange)
            .markerSymbolStyleSet(AAChartSymbolStyleType.innerBlank)
            .seriesSet([
            AASeriesElement()
                .nameSet("Range")
                .colorSet("#1E90FF")
                .typeSet(AAChartType.arearange)
                .lineWidthSet(0)
                .fillOpacitySet(0.3)
                .dataSet([
                [12464064, 14.3, 27.7],
                [12464928, 14.5, 27.8],
                [12465792, 15.5, 29.6],
                [12466656, 16.7, 30.7],
                [12467520, 16.5, 25.0],
                [12468384, 17.8, 25.7],
                [12469248, 13.5, 24.8],
                [12470112, 10.5, 21.4],
                [12470976, 9.2,  23.8],
                [12471840, 11.6, 21.8],
                [12472704, 10.7, 23.7],
                [12473568, 11.0, 23.3],
                [12474432, 11.6, 23.7],
                [12475296, 11.8, 20.7],
                [12476160, 12.6, 22.4],
                [12477024, 13.6, 19.6],
                [12477888, 11.4, 22.6],
                [12478752, 13.2, 25.0],
                [12479616, 14.2, 21.6],
                [12480480, 13.1, 17.1],
                [12481344, 12.2, 15.5],
                [12482208, 12.0, 20.8],
                [12483072, 12.0, 17.1],
                [12483936, 12.7, 18.3],
                [12484800, 12.4, 19.4],
                [12485664, 12.6, 19.9],
                [12486528, 11.9, 20.2],
                [12487392, 11.0, 19.3],
                [12488256, 10.8, 17.8],
                [12489120, 11.8, 18.5],
                [12489984, 10.8, 16.1]
            ])
                .zIndexSet(0)
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .formatterSet("""
        function () {
            let myPointOptions = this.points[0].point.options;
            let xValue = myPointOptions.x;
            let lowValue = myPointOptions.low;
            let highValue = myPointOptions.high;
            let titleStr = '🌕 this is my custom tooltip description text content <br>';
            let xValueStr = '🌖 this is x value  : ' + xValue + '<br>';
            let lowValueStr = ' 🌗 this is low value  : ' + lowValue + '<br>';
            let highValueStr = '🌘 this is high value : ' + highValue + '<br>';
            let tooltipDescStr =  titleStr + xValueStr + lowValueStr + highValueStr;
            return tooltipDescStr;
        }
                         """)
         .backgroundColorSet(AAColor.black)
         .borderColorSet(AAColor.black)
         .styleSet(AAStyle.colorSize("#FFD700", 12)))

        return aaOptions


    @staticmethod
    def customLineChartOriginalPointPositionByConfiguringXAxisFormatterAndTooltipFormatter():
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        categoryJSArrStr = (AAJSArrayConverter.JSArrayWithHaxeArray(categories))

        tooltipFormatter = Template("""
    function () {
        return  'The value for <b>' + ${categoryJSArr}[this.x] +
        '</b> is <b>' + this.y + '</b> ' + "℃";
        }
             """)

        tooltipFormatter.safe_substitute(categoryJSArr=categoryJSArrStr)

        xAxisLabelsFormatter = """
             """

        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.line)
            .colorsThemeSet(["#1e90ff","#ef476f","#ffd066","#04d69f","#25547c",])#Colors theme
            .xAxisLabelsStyleSet(AAStyle.colorStr(AAColor.white))
            .dataLabelsEnabledSet(False)
            .tooltipValueSuffixSet("℃")
            .animationTypeSet(AAChartAnimationType.bounce)
            .backgroundColorSet("#22324c")#To make the chart background color transparent, set backgroundColor to "rgba Set(0,0,0,0)" or "# 00000000". Also make sure `aaChartView!.IsClearBackgroundColor = True`
            .touchEventEnabledSet(True)
            .seriesSet([
            AASeriesElement()
                .nameSet("Tokyo")
                .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6])
            ,
            AASeriesElement()
                .nameSet("New York")
                .dataSet([0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5])
            ,
            AASeriesElement()
                .nameSet("Berlin")
                .dataSet([0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0])
            ,
            AASeriesElement()
                .nameSet("London")
                .dataSet([3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8])
            ,
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .formatterSet(tooltipFormatter))

        (aaOptions.xAxis.labels
         .formatterSet(xAxisLabelsFormatter))

        return aaOptions

    @staticmethod
    def customTooltipWhichDataSourceComeFromOutSideRatherThanSeries():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.column)#图表类型
            .yAxisTitleSet("")#设置 Y 轴标题
            .yAxisLineWidthSet(1)#Y轴轴线线宽为0即是隐藏Y轴轴线
            .yAxisGridLineWidthSet(1)#y轴横向分割线宽度为1Set(为0即是隐藏分割线)
            .colorsThemeSet(["#FFD700"])#/*纯金色*/
            .categoriesSet(["一月", "二月", "三月", "四月", "五月", "六月",
                            "七月", "八月", "九月", "十月", "十一月", "十二月"])
            .yAxisMaxSet(110)
            .seriesSet([
            AASeriesElement()
                .nameSet("2017")
                .dataSet([55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, ])
        ]))

        看近时长数组 = [70, 69, 95, 14, 18, 21, 25, 26, 23, 18, 13, 96]
        看中时长数组 = [20, 80, 57, 11, 17, 22, 24, 24, 20, 14, 86, 25]
        看远时长数组 = [90, 60, 35, 84, 13, 17, 18, 17, 14, 90, 39, 10]

        总时长数组 = list()

        # for i in 0 ... 12
        #     单个总时长 = 看近时长数组[i] + 看中时长数组[i] + 看远时长数组[i]
        #     总时长数组.appendSet(FloatSet(单个总时长))


        有效时长数组 = [39, 42, 57, 85, 19, 15, 17, 16, 14, 13, 66, 48]

        切换次数数组 = [
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            ]

        停止次数数组 = [
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            ]

        干预次数数组 = [
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
        ]

        总时长JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(总时长数组)
        有效时长JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(有效时长数组)
        看近时长JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(看近时长数组)
        看中时长JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(看中时长数组)
        看远时长JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(看远时长数组)
        切换次数JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(切换次数数组)
        停止次数JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(停止次数数组)
        干预次数JS数组字符串 = AAJSArrayConverter.JSArrayWithHaxeArray(干预次数数组)

        jsFormatterStr = Template("""
        function () {
        let 总时长数组 = ${总时长JS数组};
        let 有效时长数组 = ${有效时长JS数组};
        let 看近时长数组 = ${看近时长JS数组};
        let 看中时长数组 = ${看中时长JS数组};
        let 看远时长数组 = ${看远时长JS数组};
        let 切换次数数组 = ${切换次数JS数组};
        let 停止次数数组 = ${停止次数JS数组};
        let 干预次数数组 = ${干预次数JS数组};
        let 时间单位后缀 = "min<br/>";
        let 频率单位后缀 = "次<br/>";
        
        let pointIndex = this.point.index;
        let 单个总时长字符串 = "总时长: &nbsp &nbsp" + 总时长数组[pointIndex] + 时间单位后缀;
        let 单个有效时长字符串 = "有效时长: &nbsp" + 有效时长数组[pointIndex] + 时间单位后缀;
        let 单个看近时长字符串 = "看近时长: &nbsp" + 看近时长数组[pointIndex] + 时间单位后缀;
        let 单个看中时长字符串 = "看中时长: &nbsp" + 看中时长数组[pointIndex] + 时间单位后缀;
        let 单个看远时长字符串 = "看远时长: &nbsp" + 看远时长数组[pointIndex] + 时间单位后缀;
        let 单个切换次数字符串 = "切换次数: &nbsp" + 切换次数数组[pointIndex] + 频率单位后缀;
        let 单个停止次数字符串 = "停止次数: &nbsp" + 停止次数数组[pointIndex] + 频率单位后缀;
        let 单个干预次数字符串 = "干预次数: &nbsp" + 干预次数数组[pointIndex] + 频率单位后缀;
        
        let wholeContentString =  单个总时长字符串 + 单个有效时长字符串 + 单个看近时长字符串 + 单个看中时长字符串 + 单个看远时长字符串 + 单个切换次数字符串 + 单个停止次数字符串 + 单个干预次数字符串;
        
        return wholeContentString;
        }
        """)

        jsFormatterStr.safe_substitute(
        总时长JS数组=总时长JS数组字符串,
        有效时长JS数组=有效时长JS数组字符串,
        看近时长JS数组=看近时长JS数组字符串,
        看中时长JS数组=看中时长JS数组字符串,
        看远时长JS数组=看远时长JS数组字符串,
        切换次数JS数组=切换次数JS数组字符串,
        停止次数JS数组=停止次数JS数组字符串,
        干预次数JS数组=干预次数JS数组字符串
        )

        print(jsFormatterStr)

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         #‼️以 this.point.index 这种方式获取选中的点的索引必须设置 tooltip 的 shared 为 False
         #‼️共享时是 this.points Set(由多个 point 组成的 points 数组)
         #‼️非共享时是 this.point 单个 point 对象
         .sharedSet(False)
         .useHTMLSet(True)
         .formatterSet(jsFormatterStr)
         .backgroundColorSet(AAColor.black)#黑色背景色
         .borderColorSet("#FFD700")#边缘颜色纯金色
         .styleSet(AAStyle.colorSize("#FFD700", 12)))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/852 自定义蜘蛛🕷图样式
    @staticmethod
    def customSpiderChartStyle():
        categoryArr = [
            "周转天数Set(天)",
            "订单满足率",
            "订单履约时效",
            "动销率",
            "畅销商品缺货率",
            "高库存金额占比",
            "不动销金额占比",
            "停采金额占比",
        ]
        categoryJSArrStr = (AAJSArrayConverter.JSArrayWithHaxeArray(categoryArr))

        xAxisLabelsFormatter = Template("""
    function () {
        return ${categoryJSArr}[this.value];
        }
             """)

        xAxisLabelsFormatter.substitute(categoryJSArr=categoryJSArrStr)

        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.line)#图表类型
            .titleSet("健康体检表")#图表主标题
            .colorsThemeSet(["#fe117c","#ffc069",])#设置主体颜色数组
            .yAxisLineWidthSet(0)
            .yAxisGridLineWidthSet(1)#y轴横向分割线宽度为0Set(即是隐藏分割线)
            .yAxisTickPositionsSet([0, 5, 10, 15, 20, 25, 30, 35])
            .markerRadiusSet(5)
            .markerSymbolSet(AAChartSymbolType.circle)
            .polarSet(True)
            .seriesSet([
            AASeriesElement()
                .nameSet("本月得分")
                .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5,]),
            AASeriesElement()
                .nameSet("上月得分")
                .dataSet([0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, ]),
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.chart
         .marginLeftSet(80)
         .marginRightSet(80))

        (aaOptions.xAxis
         .lineWidthSet(0)#避免多边形外环之外有额外套了一层无用的外环
         .labels
         .styleSet(AAStyle.colorStr(AAColor.black))
         .formatterSet(xAxisLabelsFormatter))

        (aaOptions.yAxis
         .gridLineInterpolationSet("polygon")#设置蜘蛛网🕸图表的网线为多边形
         .labelsSet(AALabels()
                    .styleSet(AAStyle()
                              .colorSet(AAColor.black))))

        #设定图例项的CSS样式。只支持有关文本的CSS样式设定。
        # /* 默认是：
        #  "color"(): "#333333",
        #  "cursor"(): "pointer",
        #  "fontSize"(): "12px",
        #  "fontWeight"(): "bold"
        #
        #  */
        aaItemStyle = (AAItemStyle()
                       .colorSet(AAColor.gray)#字体颜色
                       .cursorSet("pointer")#Set(在移动端这个属性没什么意义,其实不用设置)指定鼠标滑过数据列时鼠标的形状。当绑定了数据列点击事件时，可以将此参数设置为 "pointer"，用来提醒用户改数据列是可以点击的。
                       .fontSizeSet(14)#字体大小
                       .fontWeightSet(AAChartFontWeightType.thin))#字体为细体字


        (aaOptions.legend
         .enabledSet(True)
         .alignSet(AAChartAlignType.center)#设置图例位于水平方向上的右侧
         .layoutSet(AAChartLayoutType.horizontal)#设置图例排列方式为垂直排布
         .verticalAlignSet(AAChartVerticalAlignType.top)#设置图例位于竖直方向上的顶部
         .itemStyleSet(aaItemStyle))


        return aaOptions


    # Refer to the issue https():#github.com/AAChartModel/AAChartKit/issues/589
    @staticmethod
    def customizeEveryDataLabelSinglelyByDataLabelsFormatter():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.areaspline)#图表类型
            .dataLabelsEnabledSet(True)
            .tooltipEnabledSet(False)
            .colorsThemeSet([AAGradientColor.fizzyPeach])
            .markerRadiusSet(0)
            .legendEnabledSet(False)
            .categoriesSet(["美国🇺🇸","欧洲🇪🇺","中国🇨🇳","日本🇯🇵","韩国🇰🇷","越南🇻🇳","中国香港🇭🇰",])
            .seriesSet([
            AASeriesElement()
                .dataSet([7.0, 6.9, 2.5, 14.5, 18.2, 21.5, 5.2])
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()
        #  aaOptions.yAxis.gridLineDashStyle = (AAChartLineDashStyleType.longDash#设置Y轴的网格线样式为 AAChartLineDashStyleTypeLongDash

        aaOptions.tooltip.shared = True


        unitArr = ["美元", "欧元", "人民币", "日元", "韩元", "越南盾", "港币", ]
        unitJSArrStr = (AAJSArrayConverter.JSArrayWithHaxeArray(unitArr))
        #单组 series 图表, 获取选中的点的索引是 this.point.index ,多组并且共享提示框,则是this.points[0].index
        dataLabelsFormatter = Template("""
    function () {
        return this.y + ${unitJSArr}[this.point.index];
        }
             """)

        dataLabelsFormatter.substitude(unitJSArr=unitJSArrStr)

        aaDataLabels = (AADataLabels()
                        .styleSet(AAStyle.colorSizeWeight(AAColor.red, 10, AAChartFontWeightType.bold))
                        .formatterSet(dataLabelsFormatter)
                        .backgroundColorSet(AAColor.white)# white color
                        .borderColorSet(AAColor.red)# red color
                        .borderRadiusSet(1.5)
                        .borderWidthSet(1.3)
                        .xSet(3).ySet(-20)
                        .verticalAlignSet(AAChartVerticalAlignType.middle))

        aaOptions.plotOptions.series.dataLabels = aaDataLabels

        return aaOptions


    # Refer to GitHub issue(): https():#github.com/AAChartModel/AAChartKit/issues/938
    # Refer to online chart sample(): https():#www.highcharts.com/demo/column-comparison
    @staticmethod
    def customXAxisLabelsBeImages():
        nameArr = [
            "South Korea",
            "Japan",
            "Australia",
            "Germany",
            "Russia",
            "China",
            "Great Britain",
            "United States"
        ]

        colorArr = [
            "rgbSet(201, 36, 39)",
            "rgbSet(201, 36, 39)",
            "rgbSet(0, 82, 180)",
            "rgbSet(0, 0, 0)",
            "rgbSet(240, 240, 240)",
            "rgbSet(255, 217, 68)",
            "rgbSet(0, 82, 180)",
            "rgbSet(215, 0, 38)"
        ]


        imageLinkFlagArr = [
            "197582",
            "197604",
            "197507",
            "197571",
            "197408",
            "197375",
            "197374",
            "197484"
        ]

        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.column)
            .titleSet("Custom X Axis Labels Be Images")
            .subtitleSet("use HTML")
            .categoriesSet(nameArr)
            .colorsThemeSet(colorArr)
            .borderRadiusSet(5)
            .seriesSet([
            AASeriesElement()
                .nameSet("AD 2020")
                .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5])
                .colorByPointSet(True)
        ]))

        imageLinkFlagJSArrStr = (AAJSArrayConverter.JSArrayWithHaxeArray(imageLinkFlagArr))

        xLabelsFormatter = """
function () {
    let imageFlag = ${imageLinkFlagJSArr}[this.pos];
    let imageLink = "<span><img src=\"https://image.flaticon.com/icons/svg/197/" + imageFlag + ".svg\" style=\"width: 30px; height: 30px;\"/><br></span>";
    return imageLink;
}
        """

        xLabelsFormatter.substitude(imageLinkFlagJSArr=imageLinkFlagJSArrStr)

        #    https():#api.highcharts.com.cn/highcharts#xAxis.labels.formatter
        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.xAxis.labels
         .useHTMLSet(True)
         .formatterSet(xLabelsFormatter))

        aaOptions.plotOptions.column.groupPaddingSet(0.005)

        #Custom tooltip style
        tooltipFormatter = """
function () {
    let imageFlag = ${imageLinkFlagJSArr}[this.point.index];
    let imageLink = "<span><img src=\"https://image.flaticon.com/icons/svg/197/" + imageFlag + ".svg\" style=\"width: 30px; height: 30px;\"/><br></span>";
    return imageLink
    + " 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 <br/> "
    + " Support JavaScript Function Just Right Now !!! <br/> "
    + " The Gold Price For <b>2020 "
    +  this.x
    + " </b> Is <b> "
    +  this.y
    + " </b> Dollars ";
}
        """

        tooltipFormatter.substitute(imageLinkFlagJSArr=imageLinkFlagJSArrStr)

        (aaOptions.tooltip
         .sharedSet(False)
         .useHTMLSet(True)
         .formatterSet(tooltipFormatter))

        return aaOptions



    #https():#bbs.hcharts.cn/article-109-1.html
    #图表自带的图例点击事件是：
    #点击某个显示/隐藏的图例，该图例对应的serie就隐藏/显示。
    #个人觉得不合理，正常来说，有多条折线Set(或其他类型的图表)，点击某个图例是想只看该图例对应的数据；
    #于是修改了图例点击事件。
    #
    #实现的效果是Set(以折线图为例)：
    #1. 当某条折线隐藏时，点击该折线的图例 --> 该折线显示；
    #2. 当全部折线都显示时，点击某个图例 --> 该图例对应的折线显示，其他折线均隐藏；
    #3. 当只有一条折线显示时，点击该折线的图例 --> 全部折线均显示；
    #4. 其他情况，按默认处理：
    #显示 --> 隐藏；
    #隐藏 --> 显示；
    #Customized legendItemClick Event online(): http():#code.hcharts.cn/rencht/hhhhLv/share
    @staticmethod
    def customLegendItemClickEvent():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.column)
            .stackingSet(AAChartStackingType.normal)
            .colorsThemeSet(["#fe117c","#ffc069","#06caf4","#7dffc0"])#设置主题颜色数组
            .markerRadiusSet(0)
            .seriesSet([
            AASeriesElement()
                .nameSet("2017")
                .dataSet([7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]),
            AASeriesElement()
                .nameSet("2018")
                .dataSet([0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]),
            AASeriesElement()
                .nameSet("2019")
                .dataSet([0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]),
            AASeriesElement()
                .nameSet("2020")
                .dataSet([3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]),
        ]))
        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.legend
         .enabledSet(True)
         .alignSet(AAChartAlignType.center)#设置图例位于水平方向上的右侧
         .layoutSet(AAChartLayoutType.horizontal)#设置图例排列方式为垂直排布
         .verticalAlignSet(AAChartVerticalAlignType.top))#设置图例位于竖直方向上的顶部


        #自定义图例点击事件
        aaOptions.plotOptions.series.events = (
            AAEvents()
                .legendItemClickSet("""
            function(event) {
                function getVisibleMode(series, serieName) {
                    var allVisible = true;
                    var allHidden = true;
                    for (var i = 0; i < series.length; i++) {
                        if (series[i].name == serieName)
                            continue;
                        allVisible &= series[i].visible;
                        allHidden &= (!series[i].visible);
                    }
                    if (allVisible && !allHidden)
                        return 'all-visible';
                    if (allHidden && !allVisible)
                        return 'all-hidden';
                    return 'other-cases';
                }
                
                var series = this.chart.series;
                var mode = getVisibleMode(series, this.name);
                var enableDefault = false;
                if (!this.visible) {
                    enableDefault = true;
                }
                else if (mode == 'all-visible') {
                    var seriesLength = series.length;
                    for (var i = 0; i < seriesLength; i++) {
                        var serie = series[i];
                        serie.hide();
                    }
                    this.show();
                }
                else if (mode == 'all-hidden') {
                    var seriesLength = series.length;
                    for (var i = 0; i < seriesLength; i++) {
                        var serie = series[i];
                        serie.show();
                    }
                }
                else {
                    enableDefault = true;
                }
                return enableDefault;
            }
        """))

        return aaOptions


    # https():#github.com/AAChartModel/AAChartKit-Swift/issues/233
    @staticmethod
    def customTooltipPositionerFunction():
        categories = [
            "孤岛危机",
            "使命召唤",
            "荣誉勋章",
            "狙击精英",
            "神秘海域",
            "最后生还者",
            "巫师3狂猎",
            "对马之魂",
            "死亡搁浅",
            "地狱边境",
            "闪客",
            "忍者之印"
        ]

        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.column)
            .yAxisTitleSet("")
            .yAxisGridLineWidthSet(0)
            .categoriesSet(categories)
            .seriesSet([
            AASeriesElement()
                .nameSet("单机大作")
                .colorSet(AAColor.red)
                .dataSet([0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5])
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .shadowSet(False)
         .positionerSet("""
            function (labelWidth, labelHeight, point) {
                return {
                 x : point.plotX,
                 y : 20
                };
            }
            """))

        return aaOptions



    @staticmethod
    def fixedTooltipPositionByCustomPositionerFunction():
        aaOptions = JSFuncOptionsComposer.customTooltipPositionerFunction()

        (aaOptions.tooltip
         .positionerSet("""
            function (labelWidth, labelHeight, point) {
                return {
                 x : 50,
                 y : 50
                };
            }
            """))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/967
    @staticmethod
    def disableColumnChartUnselectEventEffectBySeriesPointEventClickFunction():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.bar)
            .titleSet("Custom Bar Chart select color")
            .yAxisTitleSet("")
            .yAxisReversedSet(True)
            .xAxisReversedSet(True)
            .seriesSet([
            AASeriesElement()
                .nameSet("ElementOne")
                .dataSet([211,183,157,133,111,91,73,57,43,31,21,13,7,3])
                .allowPointSelectSet(True)
                .statesSet(AAStates()
                           .hoverSet(AAHover()
                                     .colorSet(AAColor.yellow))
                           .selectSet(AASelect()
                                      .colorSet(AAColor.red)))
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.plotOptions.series
         .pointSet(AAPoint()
                   .eventsSet(AAPointEvents()
                              .clickSet(("""
                    function () {
                        if (this.selected == true) {
                            this.selected = false;
                        }
                        return;
                    }
                    """)))))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/970
    #https():#github.com/AAChartModel/AAChartKit-Swift/issues/239
    #通过自定义 div 的 css 样式来自定义复杂效果的 tooltip 浮动提示框
    @staticmethod
    def customAreasplineChartTooltipStyleByDivWithCSS():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.areaspline)#图形类型
            .stackingSet(AAChartStackingType.normal)
            .categoriesSet([
            "10-01", "10-02", "10-03", "10-04", "10-05", "10-06", "10-07", "10-08", "10-09", "10-10", "10-11",
            "10-12", "10-13", "10-14", "10-15", "10-16", "10-17", "10-18", "10-19", "10-20", "10-21", "10-22",
            "10-23", "10-24", "10-25", "10-26", "10-27", "10-28", "10-29", "10-30", "10-31", "11-01", "11-02",
            "11-03", "11-04", "11-05", "11-06", "11-07", "11-08", "11-09", "11-10", "11-11", "11-12", "11-13",
            "11-14", "11-15", "11-16", "11-17", "11-18", "11-19", "11-20", "11-21", "11-22", "11-23", "11-24",
            "11-25", "11-26", "11-27", "11-28", "11-29", "11-30", "12-01", "12-02", "12-03", "12-04", "12-05",
            "12-06", "12-07", "12-08", "12-09", "12-10", "12-11", "12-12", "12-13", "12-14", "12-15", "12-16",
            "12-17", "12-18", "12-19", "12-20", "12-21", "12-22", "12-23", "12-24", "12-25", "12-26", "12-27",
            "12-28", "12-29", "12-30"
        ])
            .seriesSet([
            AASeriesElement()
                .nameSet("黄金上涨")
                .lineWidthSet(3)
                .colorSet("#FFD700")#/*纯金色*/)
                .fillOpacitySet(0.5)
                .dataSet([
                1.51, 6.70, 0.94, 1.44, 1.60, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10,
                4.17, 3.85, 4.17, 3.46, 3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.51, 12.7, 0.94, 1.44,
                18.6, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10, 4.17, 3.85, 4.17, 3.46,
                3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.33, 4.68, 1.31, 1.10, 13.9, 1.10, 1.16, 1.67,
                2.64, 2.86, 3.00, 3.21, 4.14, 4.07, 3.68, 3.11, 3.41, 3.25, 3.32, 3.07, 3.92, 3.05,
                2.18, 3.24, 3.23, 3.15, 2.90, 1.81, 2.11, 2.43, 5.59, 3.09, 4.09, 6.14, 5.33, 6.05,
                5.71, 6.22, 6.56, 4.75, 5.27, 6.02, 5.48
            ])
            ,
            AASeriesElement()
                .nameSet("房价下跌")
                .lineWidthSet(3)
                .colorSet("#ffc069")
                .fillOpacitySet(0.5)
                .dataSet([
                1.51, 6.70, 0.94, 1.44, 1.60, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10,
                4.17, 3.85, 4.17, 3.46, 3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.51, 12.7, 0.94, 1.44,
                18.6, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10, 4.17, 3.85, 4.17, 3.46,
                3.46, 3.55, 3.50, 4.13, 2.58, 2.28, 1.33, 4.68, 1.31, 1.10, 13.9, 1.10, 1.16, 1.67,
                2.64, 2.86, 3.00, 3.21, 4.14, 4.07, 3.68, 3.11, 3.41, 3.25, 3.32, 3.07, 3.92, 3.05,
                2.18, 3.24, 3.23, 3.15, 2.90, 1.81, 2.11, 2.43, 5.59, 3.09, 4.09, 6.14, 5.33, 6.05,
                5.71, 6.22, 6.56, 4.75, 5.27, 6.02, 5.48
            ])
            ,
        ]))

    #https():#zhidao.baidu.com/question/301691908.html
    #https():#jshare.com.cn/highcharts/hhhhGc
        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.tooltip
         .useHTMLSet(True)
         .paddingSet(0)
         .borderWidthSet(0)
         .formatterSet("""
            function () {
                var box1Text = "&nbsp 2021-" + this.x + this.points[0].series.name + this.y;
                var box2Text = "&nbsp 2021-" + this.x + this.points[1].series.name + this.y;
                
                return '<style>\
                div{margin:0;padding:0}\
                #container{width:300px;height:40px;border:80px;}\
                #container .box1{width:150px;height:40px;float:left;background:red;line-height:40px;color:#fff}\
                #container .box2{width:150px;height:40px;float:right;background:green;line-height:40px;color:#fff}\
                </style>\
                <div id=\"container\">'
                +
                '<div class=\"box1\">' + box1Text + '</div>'
                +
                '<div class=\"box2\">' + box2Text + '</div>'
                +
                '</div>';
            }
            """))

        #禁用图例点击事件
        aaOptions.plotOptions.series.events = (
            AAEvents()
                .legendItemClickSet("""
                        function() {
                          return false;
                        }
            """))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/901
    #https():#github.com/AAChartModel/AAChartKit/issues/952
    @staticmethod
    def configureTheAxesLabelsFormattersOfDoubleYAxesChart():
        aaChart = (AAChart()
                   .backgroundColorSet(AAColor.white))

        aaTitle = (AATitle()
                   .textSet(""))

        aaXAxis = (AAXAxis()
            .visibleSet(True)
            .minSet(0)
            .categoriesSet([
            "Java", "Swift", "Python", "Ruby", "PHP", "Go","C",
            "C#", "C++", "Perl", "R", "MATLAB", "SQL"
        ]))

        aaPlotOptions = (AAPlotOptions()
                         .seriesSet(AASeries()
                                    .markerSet(AAMarker()
                                               .radiusSet(7)#曲线连接点半径，默认是4
                                               .symbolSet(AAChartSymbolType.circle)#曲线点类型："circle", "square", "diamond", "triangle","triangle-down"，默认是"circle"
                                               .fillColorSet(AAColor.white)#点的填充色Set(用来设置折线连接点的填充色)
                                               .lineWidthSet(3)#外沿线的宽度Set(用来设置折线连接点的轮廓描边的宽度)
                                               .lineColorSet("")#外沿线的颜色Set(用来设置折线连接点的轮廓描边颜色，当值为空字符串时，默认取数据点或数据列的颜色)
                                               )))

        yAxis1 = (AAYAxis()
                  .visibleSet(True)
                  .lineWidthSet(1)
                  .startOnTickSet(False)
                  .endOnTickSet(False)
                  .tickPositionsSet([0, 50, 100, 150, 200])
                  .labelsSet(AALabels()
                             .enabledSet(True)
                             .styleSet(AAStyle()
                                       .colorSet("DodgerBlue"))
                             .formatterSet(("""
            function () {
                let yValue = this.value;
                if (yValue >= 200) {
                    return "极佳";
                } else if (yValue >= 150 && yValue < 200) {
                    return "非常棒";
                } else if (yValue >= 100 && yValue < 150) {
                    return "相当棒";
                } else if (yValue >= 50 && yValue < 100) {
                    return "还不错";
                } else {
                    return "一般";
                }
            }
            """)))
                  .gridLineWidthSet(0)
                  .titleSet(AATitle()
                            .textSet("中文")
                            .styleSet(AAStyle.colorSizeWeight("DodgerBlue", 14, AAChartFontWeightType.bold))))

        yAxis2 = (AAYAxis()
                  .visibleSet(True)
                  .lineWidthSet(1)
                  .startOnTickSet(False)
                  .endOnTickSet(False)
                  .tickPositionsSet([0, 50, 100, 150, 200])
                  .labelsSet(AALabels()
                             .enabledSet(True)
                             .styleSet(AAStyle()
                                       .colorSet(AAColor.red))
                             .formatterSet("""
            function () {
                let yValue = this.value;
                if (yValue >= 200) {
                    return "Awesome";
                } else if (yValue >= 150 && yValue < 200) {
                    return "Great";
                } else if (yValue >= 100 && yValue < 150) {
                    return "Very Good";
                } else if (yValue >= 50 && yValue < 100) {
                    return "Not Bad";
                } else {
                    return "Just So So";
                }
            }
           """))
                  .gridLineWidthSet(0)
                  .titleSet(AATitle()
                            .textSet("ENGLISH")
                            .styleSet(AAStyle.colorSizeWeight(AAColor.red, 14, AAChartFontWeightType.bold)))
                  .oppositeSet(True))

        aaTooltip = (AATooltip()
                     .enabledSet(True)
                     .sharedSet(True))

        seriesArr = [
            AASeriesElement()
                .nameSet("2020")
                .typeSet(AAChartType.spline)
                .lineWidthSet(7)
                .colorSet(AAGradientColor.deepSea)
                .yAxisSet(1)
                .dataSet([
                0, 71.5, 106.4, 129.2, 144.0, 176.0,
                135.6, 148.5, 216.4, 194.1, 95.6, 54.4
            ]),
            AASeriesElement()
                .nameSet("2021")
                .typeSet(AAChartType.spline)
                .lineWidthSet(7)
                .colorSet(AAGradientColor.sanguine)
                .yAxisSet(0)
                .dataSet([
                135.6, 148.5, 216.4, 194.1, 95.6, 54.4,
                0, 71.5, 106.4, 129.2, 144.0, 176.0
            ])
        ]

        aaOptions = (AAOptions()
                     .chartSet(aaChart)
                     .titleSet(aaTitle)
                     .plotOptionsSet(aaPlotOptions)
                     .xAxisSet(aaXAxis)
                     .yAxisArraySet([yAxis1,yAxis2])
                     .tooltipSet(aaTooltip)
                     .seriesSet(seriesArr))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/1042
    @staticmethod
    def makePieChartShow0Data():
        aaOptions = (AAOptions()
            .titleSet(AATitle()
                      .textSet(""))
            .chartSet(AAChart()
                      .typeSet(AAChartType.pie))
            .seriesSet([
            AASeriesElement()
                .nameSet("ZeroDataPie")
                .dataSet([

            ])
                .tooltipSet(AATooltip()
                            .sharedSet(False)
                            .pointFormatterSet("""
                                function() {
                                    return "<span style=\'color:" + this.color + "\'> ◉ </span>"
                                    + this.series.name
                                    + ": <b>"
                                    + (this.options.isZero ? 0 : this.y)
                                    + "</b><br/>";
                                }
                                """))
        ]))

        return aaOptions


    #https():#github.com/AAChartModel/AAChartKit/issues/1217
    @staticmethod
    def customColumnChartXAxisLabelsTextByInterceptTheFirstFourCharacters():
        aaChartModel = (AAChartModel()
            .chartTypeSet(AAChartType.bar)#图表类型
            .titleSet("春江花月夜")#图表主标题
            .subtitleSet("张若虚")#图表副标题
            .xAxisReversedSet(True)
            .xAxisLabelsStyleSet(AAStyle.colorStr(AAColor.black))
            .legendEnabledSet(False)
            .categoriesSet([
            "春江潮水连海平", "海上明月共潮生",
            "滟滟随波千万里", "何处春江无月明",
            "江流宛转绕芳甸", "月照花林皆似霰",
            "空里流霜不觉飞", "汀上白沙看不见",
            "江天一色无纤尘", "皎皎空中孤月轮",
            "江畔何人初见月", "江月何年初照人",
            "人生代代无穷已", "江月年年望相似",
            "不知江月待何人", "但见长江送流水",
            "白云一片去悠悠", "青枫浦上不胜愁",
            "谁家今夜扁舟子", "何处相思明月楼",
            "可怜楼上月裴回", "应照离人妆镜台",
            "玉户帘中卷不去", "捣衣砧上拂还来",
            "此时相望不相闻", "愿逐月华流照君",
            "鸿雁长飞光不度", "鱼龙潜跃水成文",
            "昨夜闲潭梦落花", "可怜春半不还家",
            "江水流春去欲尽", "江潭落月复西斜",
            "斜月沉沉藏海雾", "碣石潇湘无限路",
            "不知乘月几人归", "落月摇情满江树",
        ])
            .seriesSet([
            AASeriesElement()
                .lineWidthSet(1.5)
                .colorSet(AAGradientColor.linearGradient1(
                AALinearGradientDirection.toTop,
                "#7052f4",
                "#00b0ff"
            ))
                .nameSet("2018")
                .dataSet([
                1.51, 3.7, 0.94, 1.44, 1.6, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90, 4.61, 4.10,
                4.17, 3.85, 4.17, 3.46, 3.46, 3.55, 3.50, 4.13, 2.58, 2.28,1.51, 2.7, 0.94, 1.44,
                3.6, 1.63, 1.56, 1.91, 2.45, 3.87, 3.24, 4.90,
            ])
        ]))

        aaOptions = aaChartModel.aa_toAAOptions()

        (aaOptions.xAxis.labels
         .formatterSet("""
        function () {
            let xAxisCategory = this.value;
            if (xAxisCategory.length > 4) {
                return xAxisCategory.substr(0, 4);
            } else {
                return xAxisCategory;
            }
        }
        """))

        return aaOptions
     
     


  
 
 