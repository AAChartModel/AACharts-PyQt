from random import random

from PySide6 import QtWidgets, QtCore

from aacharts.aachartcreator.PYChartView import PYChartView
from demo.CustomStyleChartComposer import CustomStyleChartComposer


class MainTreeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # https://gist.github.com/fredrikaverpil/1fa4f3360ffdb1e69507
        folderTree = QtWidgets.QTreeWidget()

        sectionTitleArr = [
            "Basic Type Chart --- 基础类型图表",
            "Special Type Chart --- 特殊类型图表",
            "Custom Style Chart---一些自定义风格样式图表",
            "Mixed Chart --- 混合图形",
            "Draw Chart With AAOptions---通过Options绘图",
            "JS Function For AAOptionns ---通过带有 JS 函数的 Options 绘图",
        ]


        chartTypeTitleArr = [
            # Basic types chart
            [
                "Column Chart---柱形图",
                "Bar Chart---条形图",
                "Area Chart---折线填充图",
                "Areaspline Chart---曲线填充图",
                "Step Area Chart--- 直方折线填充图",
                "Step Line Chart--- 直方折线图",
                "Line Chart---折线图",
                "Spline Chart---曲线图",
            ],
            # Special types chart
            [
                "Polar Chart---极地图",
                "Pie Chart---扇形图",
                "Bubble Chart---气泡图",
                "Scatter Chart---散点图",
                "Arearange Chart---折线区域范围图",
                "Area Spline range Chart--曲线区域范围图",
                "Columnrange Chart--- 柱形范围图",
                "Step Line Chart--- 直方折线图",
                "Step Area Chart--- 直方折线填充图",
                "Boxplot Chart--- 箱线图",
                "Waterfall Chart--- 瀑布图",
                "Pyramid Chart---金字塔图",
                "Funnel Chart---漏斗图",
                "Error Bar Chart---误差图",
            ],
            # Custom chart style by AAChartModel
            [
                "Colorful Column Chart---多彩条形图",
                "Colorful Gradient Color Chart---多彩颜色渐变条形图",
                "Discontinuous Data Chart---数值不连续の图表",
                "Mixed Line Chart---虚实线混合折线图",
                "Random Colors Colorful Column Chart---随机颜色の多彩柱形图",
                "Gradient Color Bar Chart---颜色渐变条形图",
                "Stacking polar chart---百分比堆积效果の极地图",
                "Area Chart with minus--带有负数の区域填充图",
                "Step Line Chart--直方折线图",
                "Step Area Chart--直方折线填充图",
                "Nightingale Rose Chart---南丁格尔玫瑰图",
                "Specific Data Customize Datalabel",
                "Chart With Shadow Style---带有阴影效果の图表",
                "Colorful gradient Areaspline Chart---多层次渐变区域填充图",
                "Colorful gradient Spline Chart---多层次渐变曲线图",
                "Gradient Color Areaspline Chart---半透明渐变效果区域填充图",
                "Special Style Marker Of Single Data Element Chart",
                "Special Style Column Of Single Data Element Chart",
                "configure Area Chart Threshold---自定义阈值",
                "custom Scatter Chart Marker Symbol Content---自定义散点图の标志点内容",
                "custom Line Chart Marker Symbol Content---自定义折线图の标志点内容",
                "Triangle Radar Chart---三角形雷达图",
                "Quadrangle Radar Chart---四角形雷达图",
                "Pentagon Radar Chart---五角形雷达图",
                "Hexagon Radar Chart----六角形雷达图",
                "Draw Line Chart With Points Coordinates----通过点坐标来绘制折线图",
                "custom Special Style DataLabel Of Single Data Element Chart",
                "custom Bar Chart Hover Color and Select Color---自定义条形图手指滑动颜色和单个长条被选中颜色",
                "custom Line Chart Chart Hover And Select Halo Style",
                "custom Spline Chart Marker States Hover Style",
                "customNormalStackingChartDataLabelsContentAndStyle---自定义堆积柱状图 DataLabels の内容及样式",
                "upsideDownPyramidChart---倒立の金字塔图",
                "doubleLayerPieChart---双层嵌套扇形图",
                "doubleLayerDoubleColorsPieChart---双层嵌套双颜色主题扇形图",
                "disableSomeOfLinesMouseTrackingEffect---针对部分数据列关闭鼠标或手指跟踪行为",
                "configureColorfulShadowChart---彩色阴影效果の曲线图",
                "configureColorfulDataLabelsStepLineChart---彩色 DataLabels の直方折线图",
                "configureColorfulGradientColorAndColorfulDataLabelsStepAreaChart---彩色渐变效果且彩色 DataLabels の直方折线填充图",
                "disableSplineChartMarkerHoverEffect---禁用曲线图の手指滑动 marker 点の光圈变化放大の效果",
                "configureMaxAndMinDataLabelsForChart---为图表最大值最小值添加 DataLabels 标记",
                "customVerticalXAxisCategoriesLabelsByHTMLBreakLineTag---通过 HTML 的换行标签来实现图表的 X 轴的 分类文字标签的换行效果",
                "noMoreGroupingAndOverlapEachOtherColumnChart---不分组的相互重叠柱状图📊",
                "noMoreGroupingAndNestedColumnChart---不分组的嵌套柱状图📊",
            ],
            # Mixed Chart
            [
                "Arearange Mixed Line---面积范围均线图",
                "Columnrange Mixed Line---柱形范围图混合折线图",
                "Stacking Column Mixed Line---堆积柱形图混合折线图",
                "Dash Style Types Mixed---多种类型曲线混合图",
                "Negative Color Mixed Column Chart---基准线以下异色混合图",
                "scatterMixedLine---散点图混合折线图",
                "Negative Color Mixed Bubble Chart---基准线以下异色气泡图",
                "Polygon Mixed Scatter---多边形混合散点图",
                "Polar Chart Mixed---极地混合图",
                "Column Mixed Scatter---柱形图混合散点图",
                "Pie Mixed Line Mixed Column---扇形折线柱形混合图",
                "Line Chart With Shadow---带有阴影效果の折线图",
                "Negative Color Mixed Areaspline chart---基准线以下异色混合曲线填充图",
                "Aerasplinerange Mixed Columnrange Mixed Line Chart---曲线面积范围混合柱形范围混合折线图"
            ],

            
            # Draw Chart with AAOptions
            [
                "configureLegendStyle",
                "Custom Chart  Sample Two",
                "Custom Chart  Sample three",
                "Custom Chart  Sample 4",
                "customAreaChartYAxisLabelsAndGridLineStyle---自定义曲线填充图图的 Y 轴 的 Labels 和 网格线样式",
                "Adjust Y Axis Min value",
                "Mirror Chart",
                "Adjust The XAxis Labels",
                "Adjust GroupPadding Between Columns",
                "configureAAPlotBandsForChart || 值域颜色分割带🎀",
                "configureAAPlotLinesForChart || 值域颜色分割线🧶",
                "customAATooltipWithJSFuntion",
                "customXAxisCrosshairStyle",
                "configureXAxisLabelsFontColorWithHTMLString",
                "configureXAxisLabelsFontColorAndFontSizeWithHTMLString",
                "configure_DataLabels_XAXis_YAxis_Legend_Style",
                "configureXAxisPlotBand",
                "configureDoubleYAxisChartOptions",
                "configureTripleYAxesMixedChart || 三重 Y 轴混合图",
                "Double Y Axes And Column Line Mixed Chart || 双 Y 轴柱形曲线混合图",
                "Double Y Axes Market Depth Chart || 双 Y 轴市场深度图",
                "custom Area Chart Tooltip Style Like HTML Table || 自定义区域填充图浮动提示框为 HTML 表格样式",
                "custom Axes Grid Line Style || 自定义 X 轴和 Y 轴网格线の样式",
                "custom Radar Chart Style || 自定义雷达图样式",
                "customColumnrangeChartStyle---自定义柱形范围图样式",
                "self customXAxisLabelsBeImages---自定义曲线面积图 X 轴 labels 为一组图片🖼",
                "Triangle Radar Chart With PlotBands---带有颜色标志带の三角形雷达图",
                "Quadrangle Radar Chart With PlotBands---带有颜色标志带の四角形雷达图",
                "Pentagon Radar Chart With PlotBands---带有颜色标志带の五角形雷达图",
                "Hexagon Radar Char With PlotBands----带有颜色标志带の六角形雷达图",
                "Spider Web Radar Chart With PlotBands----带有颜色标志带の🕸蜘蛛网状雷达图",
                
                "configureComplicatedCustomAreasplineChart---复杂自定义曲线填充图 1",
                "configureComplicatedCustomAreasplineChart2---复杂自定义曲线填充图 2",
                "configureComplicatedCustomAreasplineChart3---复杂自定义曲线填充图 3",
                "yAxisOnTheRightSideChart---y轴在右侧的图表",
                "doubleLayerHalfPieChart---双层嵌套的玉阕图",
                "customAreasplineChartTooltipContentWithHeaderFormat---通过 tooltip 的 headerFormat 属性来自定义 曲线填充图的 tooltip",
                "customAreaChartTooltipStyleWithTotalValueHeader---浮动提示框 header 显示总值信息",
                "configureYAxisLabelsNumericSymbolsMagnitudeOfAerasplineChart---自定义 Y 轴的 Labels 国际单位符基数及国际单位符",
                "timeDataWithIrregularIntervalsChart---X 轴时间不连续的折线图",
                "logarithmicAxisLineChart---对数轴折线图📈",
                "logarithmicAxisScatterChart---对数轴散点图",
                
                "Disable Mixed Chart Inactive Animation Effect----禁用混合图表的 inactive 动画效果",
                "Adjust Bubble Chart Min And Max----调整气泡图的 min 和 max 相关属性",
                "customLineChartDataLabelsFormat---自定义曲线图的 DataLabels 的 format 属性",
                "customLineChartDataLabelsFormat2---自定义曲线图的 DataLabels 的 format 属性2(更简易方法)",
                "complicatedScatterChart---复杂的自定义散点图"
            ],
            # Custom Tooltip With JavaScript Formatter Function 
            [
                "customAreaChartTooltipStyleWithSimpleFormatString---简单字符串拼接",
                "customAreaChartTooltipStyleWithDifferentUnitSuffix---自定义不同单位后缀",
                "customAreaChartTooltipStyleWithColorfulHtmlLabels---自定义多彩颜色文字",
                "customLineChartTooltipStyleWhenValueBeZeroDoNotShow---值为0时,在tooltip中不显示",
                "customBoxplotTooltipContent---自定义箱线图の浮动提示框头部内容",
                "customYAxisLabels---自定义Y轴文字1",
                "customYAxisLabels2---自定义Y轴文字2",
                "customStackedAndGroupedColumnChartTooltip---自定义分组堆积柱状图tooltip内容",
                "Double X Axes Mirror Chart---双 X 轴镜像图表",
                "custom Arearange Chart Tooltip---自定义面积范围图浮动提示框",
                "customLineChartOriginalPointPositionByConfiguringXAxisFormatterAndTooltipFormatter---调整折线图の X 轴左边距",
                "customTooltipWhichDataSourceComeFromOutSideRatherThanSeries---通过来自外部の数据源来自定义 tooltip (而非常规の来自图表の series)",
                "custom Spider Chart Style---自定义蜘蛛图🕷🕸样式",
                "customize Every DataLabel Singlely By DataLabels Formatter---通过 DataLabels 的 formatter 函数来实现单个数据标签🏷自定义",
                "custom XAxis Labels Be Images---自定义柱形图 X 轴 labels 为一组图片🖼",
                "custom Legend Item Click Event---自定义图例点击事件🖱",
                "customTooltipPostionerFunction---自定义浮动提示框 positioner 函数",
                "fixedTooltipPositionByCustomPositionerFunction---通过 Positioner 函数来实现一个位置固定的提示框",
                "disableColumnChartUnselectEventEffectBySeriesPointEventClickFunction---通过 Series 的 Point 的选中事件函数来禁用条形图反选效果",
                "customAreasplineChartTooltipStyleByDivWithCSS---通过自定义 div 的 css 样式来自定义复杂效果的 tooltip 浮动提示框",
                "configureTheAxesLabelsFormattersOfDoubleYAxesChart---配置双 Y 轴图表的 Y 轴文字标签的 Formatter 函数",
                "makePieChartShow0Data---使饼图显示为 0 的数据",
                "customColumnChartXAxisLabelsTextByInterceptTheFirstFourCharacters---通过截取前四个字符来自定义 X 轴 labels",
            ],

        ]

        for index in range(len(sectionTitleArr)):
            sectionTitleStr = sectionTitleArr[index]
            root = QtWidgets.QTreeWidgetItem(folderTree, [sectionTitleStr])

            singleSectionChartTypeTitleArr = chartTypeTitleArr[index]
            for chartTypeStr in singleSectionChartTypeTitleArr:
                QtWidgets.QTreeWidgetItem(root, [chartTypeStr])


        def printer(treeItem):
            foldername = treeItem.text(0)
            comment = treeItem.text(1)
            data = treeItem.text(2)
            # treeItem.indexOfChild()
            print(foldername + ': ' + comment + ' (' + data + ')')

        folderTree.itemClicked.connect(lambda: printer(folderTree.currentItem()))

        self.hello = ["Hallo World", "Hei maailma", "Hola Mundo", "你好，世界"]
        self.button = QtWidgets.QPushButton("点击我")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.chartView = PYChartView()
        testChartModel = CustomStyleChartComposer.configureColorfulBarChart()
        self.chartView.aa_drawChartWithChartModel(testChartModel)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.chartView)
        self.layout.addWidget(folderTree)

        # self.layout.addWidget(self.qtWebView)


        self.button.clicked.connect(self.magic)
        self.setWindowTitle("你好世界")

    def printer(treeItem):
        foldername = treeItem.text(0)
        comment = treeItem.text(1)
        data = treeItem.text(2)
        print
        foldername + ': ' + comment + ' (' + data + ')'


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

