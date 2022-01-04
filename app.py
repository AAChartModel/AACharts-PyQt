import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QMessageBox
from PySide6 import QtWebEngineWidgets, QtWidgets, QtCore
from PySide6.QtWebEngineWidgets import QWebEngineView
import webview
import wx
from wx.html2 import WebView

# from PyQt6.QtWebEngineWidgets import QWebEnginePage
# from PyQt6.QtWebEngineWidgets import QWebEngineView

import simplejson
import json


import jsonpickle

from aacharts.aachartcreator.AAChartModel import AAChartModel
from aacharts.aachartcreator.AASeriesElement import AASeriesElement
from aacharts.aaenum.AAEnum import AAChartType, AAChartAnimationType
from aacharts.aaoptionsmodel.AAOptions import AAOptions
from aacharts.aatool.AAJsonConverter import AAJsonConverter
from demo.ChartOptionsComposer import ChartOptionsComposer
from demo.CustomStyleChartComposer import CustomStyleChartComposer
from demo.JSFuncOptionsComposer import JSFuncOptionsComposer
from demo.SpecialChartComposer import SpecialChartComposer


class Demo(QWidget):  # 1
    def __init__(self):
        super(Demo, self).__init__()
        # self.web_view = QWebEngineView(self)
        # self.web_view.setMinimumWidth(400)
        # self.web_view.setMinimumHeight(300)
        #
        # self.web_view.load(QUrl("file:#/Users/anan/PycharmProjects/HelloMyPython/AAChartView.html"))

        self.button = QPushButton('Start', self)  # 2
        # self.button.clicked.connect(self.change_text)           # 3
        self.button.clicked.connect(self.change_my_first_text)

        testType = AAChartType.Area

    def change_text(self):
        print('change text')
        self.button.setText('Stop')  # 4
        self.button.clicked.disconnect(self.change_text)  # 5

        # 回调函数
    def js_callback(self, result):
        print("真的收到信息了$" + str(result))
        QMessageBox.information(self, "提示", str(result))

    def change_my_first_text(self):
        print("哈哈哈,我终于可以开发 QT 啦,尼玛终于不用搞什么蛋疼的 C++了")
        self.button.setText("改变了文字了")

        js_string = '''
                function myFunction()
                {
                    return sender;
                }

                myFunction();
                '''

        self.web_view.page().runJavaScript(js_string, self.js_callback)



class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        web_view.RunScript("alert('测试运行 JS')")
        web_view.RunScript("document.write('Hello from wx.Widgets!')")
        web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.optionsJson = ""

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, 'New', size=(90, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rename', size=(90, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, 'Delete', size=(90, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Clear', size=(90, 30))

        self.web_view = WebView.New(btnPanel, -1, size=(900,600))
        # web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/AAChartView.html")
        # self.web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/aacharts/AAJSFiles/AAChartView.html")
        self.web_view.Bind(wx.html2.EVT_WEBVIEW_ERROR, self.on_webview_error)
        self.web_view.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.on_webview_load)
        # web_view.RunScript("alert('测试运行 JS')")
        # web_view.RunScript("document.write('Hello from wx.Widgets!')")
        # web_view.RunScript("document.write('--------------这个世上本没有路, 走的人多了,也便成了路Hello from wx.Widgets!')")



        self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        # self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)
        vbox.Add(self.web_view, 0, wx.TOP, 5)


        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 1, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('wx.ListBox')

        # self.listbox.Append("Polar Chart---极地图")
        # self.listbox.Append("Pie Chart---扇形图")
        # self.listbox.Append("Bubble Chart---气泡图")
        # self.listbox.Append("Scatter Chart---散点图")
        # self.listbox.Append("Arearange Chart---折线区域范围图")
        # self.listbox.Append("Area Spline range Chart--曲线区域范围图")
        # self.listbox.Append("Columnrange Chart--- 柱形范围图")
        # self.listbox.Append("Step Line Chart--- 直方折线图")
        # self.listbox.Append("Step Area Chart--- 直方折线填充图")
        # self.listbox.Append("Boxplot Chart--- 箱线图")
        # self.listbox.Append("Waterfall Chart--- 瀑布图")
        # self.listbox.Append("Pyramid Chart---金字塔图")
        # self.listbox.Append("Funnel Chart---漏斗图")
        # self.listbox.Append("Error Bar Chart---误差图")




        # self.listbox.Append("Colorful Column Chart---多彩条形图")
        # self.listbox.Append("Colorful Gradient Color Chart---多彩颜色渐变条形图")
        # self.listbox.Append("Discontinuous Data Chart---数值不连续の图表")
        # self.listbox.Append("Mixed Line Chart---虚实线混合折线图")
        # self.listbox.Append("Random Colors Colorful Column Chart---随机颜色の多彩柱形图")
        # self.listbox.Append("Gradient Color Bar Chart---颜色渐变条形图")
        # self.listbox.Append("Stacking polar chart---百分比堆积效果の极地图")
        # self.listbox.Append("Area Chart with minus--带有负数の区域填充图")
        # self.listbox.Append("Step Line Chart--直方折线图")
        # self.listbox.Append("Step Area Chart--直方折线填充图")
        # self.listbox.Append("Nightingale Rose Chart---南丁格尔玫瑰图")
        # self.listbox.Append("Specific Data Customize Datalabel")
        # self.listbox.Append("Chart With Shadow Style---带有阴影效果の图表")
        # self.listbox.Append("Colorful gradient Areaspline Chart---多层次渐变区域填充图")
        # self.listbox.Append("Colorful gradient Spline Chart---多层次渐变曲线图")
        # self.listbox.Append("Gradient Color Areaspline Chart---半透明渐变效果区域填充图")
        # self.listbox.Append("Special Style Marker Of Single Data Element Chart")
        # self.listbox.Append("Special Style Column Of Single Data Element Chart")
        # self.listbox.Append("configure Area Chart Threshold---自定义阈值")
        # self.listbox.Append("custom Scatter Chart Marker Symbol Content---自定义散点图の标志点内容")
        # self.listbox.Append("custom Line Chart Marker Symbol Content---自定义折线图の标志点内容")
        # self.listbox.Append("Triangle Radar Chart---三角形雷达图")
        # self.listbox.Append("Quadrangle Radar Chart---四角形雷达图")
        # self.listbox.Append("Pentagon Radar Chart---五角形雷达图")
        # self.listbox.Append("Hexagon Radar Chart----六角形雷达图")
        # self.listbox.Append("Draw Line Chart With Points Coordinates----通过点坐标来绘制折线图")
        # self.listbox.Append("custom Special Style DataLabel Of Single Data Element Chart")
        # self.listbox.Append("custom Bar Chart Hover Color and Select Color---自定义条形图手指滑动颜色和单个长条被选中颜色")
        # self.listbox.Append("custom Line Chart Chart Hover And Select Halo Style")
        # self.listbox.Append("custom Spline Chart Marker States Hover Style")
        # self.listbox.Append("customNormalStackingChartDataLabelsContentAndStyle---自定义堆积柱状图 DataLabels の内容及样式")
        # self.listbox.Append("upsideDownPyramidChart---倒立の金字塔图")
        # self.listbox.Append("doubleLayerPieChart---双层嵌套扇形图")
        # self.listbox.Append("doubleLayerDoubleColorsPieChart---双层嵌套双颜色主题扇形图")
        # self.listbox.Append("disableSomeOfLinesMouseTrackingEffect---针对部分数据列关闭鼠标或手指跟踪行为")
        # self.listbox.Append("configureColorfulShadowChart---彩色阴影效果の曲线图")
        # self.listbox.Append("configureColorfulDataLabelsStepLineChart---彩色 DataLabels の直方折线图")
        # self.listbox.Append("configureColorfulGradientColorAndColorfulDataLabelsStepAreaChart---彩色渐变效果且彩色 DataLabels の直方折线填充图")
        # self.listbox.Append("disableSplineChartMarkerHoverEffect---禁用曲线图の手指滑动 marker 点の光圈变化放大の效果")
        # self.listbox.Append("configureMaxAndMinDataLabelsForChart---为图表最大值最小值添加 DataLabels 标记")
        # self.listbox.Append("customVerticalXAxisCategoriesLabelsByHTMLBreakLineTag---通过 HTML 的换行标签来实现图表的 X 轴的 分类文字标签的换行效果")
        # self.listbox.Append("noMoreGroupingAndOverlapEachOtherColumnChart---不分组的相互重叠柱状图📊")
        # self.listbox.Append("noMoreGroupingAndNestedColumnChart---不分组的嵌套柱状图📊")

        self.listbox.Append("configureLegendStyle")
        self.listbox.Append("Custom Chart  Sample Two")
        self.listbox.Append("Custom Chart  Sample three")
        self.listbox.Append("Custom Chart  Sample 4")
        self.listbox.Append("customAreaChartYAxisLabelsAndGridLineStyle---自定义曲线填充图图的 Y 轴 的 Labels 和 网格线样式")
        self.listbox.Append("Adjust Y Axis Min value")
        self.listbox.Append("Mirror Chart")
        self.listbox.Append("Adjust The XAxis Labels")
        self.listbox.Append("Adjust GroupPadding Between Columns")
        self.listbox.Append("configureAAPlotBandsForChart || 值域颜色分割带🎀")
        self.listbox.Append("configureAAPlotLinesForChart || 值域颜色分割线🧶")
        self.listbox.Append("customAATooltipWithJSFuntion")
        self.listbox.Append("customXAxisCrosshairStyle")
        self.listbox.Append("configureXAxisLabelsFontColorWithHTMLString")
        self.listbox.Append("configureXAxisLabelsFontColorAndFontSizeWithHTMLString")
        self.listbox.Append("configure_DataLabels_XAXis_YAxis_Legend_Style")
        self.listbox.Append("configureXAxisPlotBand")
        self.listbox.Append("configureDoubleYAxisChartOptions")
        self.listbox.Append("configureTripleYAxesMixedChart || 三重 Y 轴混合图")
        self.listbox.Append("Double Y Axes And Column Line Mixed Chart || 双 Y 轴柱形曲线混合图")
        self.listbox.Append("Double Y Axes Market Depth Chart || 双 Y 轴市场深度图")
        self.listbox.Append("custom Area Chart Tooltip Style Like HTML Table || 自定义区域填充图浮动提示框为 HTML 表格样式")
        self.listbox.Append("custom Axes Grid Line Style || 自定义 X 轴和 Y 轴网格线の样式")
        self.listbox.Append("custom Radar Chart Style || 自定义雷达图样式")
        self.listbox.Append("customColumnrangeChartStyle---自定义柱形范围图样式")
        self.listbox.Append("self customXAxisLabelsBeImages---自定义曲线面积图 X 轴 labels 为一组图片🖼")
        self.listbox.Append("Triangle Radar Chart With PlotBands---带有颜色标志带の三角形雷达图")
        self.listbox.Append("Quadrangle Radar Chart With PlotBands---带有颜色标志带の四角形雷达图")
        self.listbox.Append("Pentagon Radar Chart With PlotBands---带有颜色标志带の五角形雷达图")
        self.listbox.Append("Hexagon Radar Char With PlotBands----带有颜色标志带の六角形雷达图")
        self.listbox.Append("Spider Web Radar Chart With PlotBands----带有颜色标志带の🕸蜘蛛网状雷达图")

        self.listbox.Append("configureComplicatedCustomAreasplineChart---复杂自定义曲线填充图 1")
        self.listbox.Append("configureComplicatedCustomAreasplineChart2---复杂自定义曲线填充图 2")
        self.listbox.Append("configureComplicatedCustomAreasplineChart3---复杂自定义曲线填充图 3")
        self.listbox.Append("yAxisOnTheRightSideChart---y轴在右侧的图表")
        self.listbox.Append("doubleLayerHalfPieChart---双层嵌套的玉阕图")
        self.listbox.Append("customAreasplineChartTooltipContentWithHeaderFormat---通过 tooltip 的 headerFormat 属性来自定义 曲线填充图的 tooltip")
        self.listbox.Append("customAreaChartTooltipStyleWithTotalValueHeader---浮动提示框 header 显示总值信息")
        self.listbox.Append("configureYAxisLabelsNumericSymbolsMagnitudeOfAerasplineChart---自定义 Y 轴的 Labels 国际单位符基数及国际单位符")
        self.listbox.Append("timeDataWithIrregularIntervalsChart---X 轴时间不连续的折线图")
        self.listbox.Append("logarithmicAxisLineChart---对数轴折线图📈")
        self.listbox.Append("logarithmicAxisScatterChart---对数轴散点图")

        self.listbox.Append("Disable Mixed Chart Inactive Animation Effect----禁用混合图表的 inactive 动画效果")
        self.listbox.Append("Adjust Bubble Chart Min And Max----调整气泡图的 min 和 max 相关属性")
        self.listbox.Append("customLineChartDataLabelsFormat---自定义曲线图的 DataLabels 的 format 属性")
        self.listbox.Append("customLineChartDataLabelsFormat2---自定义曲线图的 DataLabels 的 format 属性2(更简易方法)")
        self.listbox.Append("complicatedScatterChart---复杂的自定义散点图")

        # 添加事件处理
        self.Bind(wx.EVT_LISTBOX, self.on_choice, self.listbox)

        self.Centre()

    def on_choice(self, event):
        listbox = event.GetEventObject()
        print("选择{0}".format(listbox.GetSelections()))
        selectedIndex = listbox.GetSelections()[0]
        testChartModel = self.chartOptionsConfigurationWithSelectedIndex(selectedIndex)
        # testChartModel2 = self.chartConfigurationWithSelectedIndex(listbox.GetSelections())

        self.aa_drawChartWithChartOptions(testChartModel)

    def on_webview_error(self, evt):
        self.URL = evt.GetURL()
        print(self.URL)
        self.retries += 1
        if self.retries > self.max_retries:  # Give up
            self.Destroy()
        print("💀💀💀💀💀Error {} of {} attempts to load {}, trying again in 3 seconds.".format(self.retries, self.max_retries,
                                                                                      self.URL))
        if self.retries > 5:  # Try alternate
            self.URL = "http:#wxPython.org"
            print("Swapping to alternate Url " + self.URL)
        self.browser.Destroy()


    def on_webview_load(self, evt):
        print("哈哈哈🔥, 图表加载完成事件捕获成功")
        self.drawChart()

    def drawChart(self):
        jsStr = f"loadTheHighChartView('{self.optionsJson}','0','0')"
        self.web_view.RunScript(jsStr)

    def aa_drawChartWithChartModel(self, aaChartModel: AAChartModel):
        aaOptions = aaChartModel.aa_toAAOptions()
        self.aa_drawChartWithChartOptions(aaOptions)

    def aa_drawChartWithChartOptions(self, aaOptions: AAOptions):
        if len(self.optionsJson) < 1:
            self.configureOptionsJsonStringWithAAOptions(aaOptions)
            self.web_view.LoadURL("/Users/admin/Documents/GitHub/AACharts-PyQt/aacharts/AAJSFiles/AAChartView.html")
        else:
            self.aa_refreshChartWholeContentWithChartOptions(aaOptions)

    def configureOptionsJsonStringWithAAOptions(self, aaOptions: AAOptions):
        pureJson = AAJsonConverter.convertChartOptionsToPureJson(aaOptions)
        self.optionsJson = pureJson

    def aa_refreshChartWholeContentWithChartOptions(self, aaOptions: AAOptions):
        self.configureOptionsJsonStringWithAAOptions(aaOptions)
        self.drawChart()
        
    def specialChartConfigurationWithSelectedIndex(self, selectedIndex):
        if selectedIndex == 0: return SpecialChartComposer.configureColumnChart()
        elif selectedIndex == 1: return SpecialChartComposer.configurePieChart()
        elif selectedIndex == 2: return SpecialChartComposer.configureBubbleChart()
        elif selectedIndex == 3: return SpecialChartComposer.configureScatterChart()
        elif selectedIndex == 4: return SpecialChartComposer.configureArearangeChart()
        elif selectedIndex == 5: return SpecialChartComposer.configureAreasplinerangeChart()
        elif selectedIndex == 6: return SpecialChartComposer.configureColumnrangeChart()
        elif selectedIndex == 7: return SpecialChartComposer.configureStepLineChart()
        elif selectedIndex == 8: return SpecialChartComposer.configureStepAreaChart()
        elif selectedIndex == 9: return SpecialChartComposer.configureBoxplotChart()
        elif selectedIndex == 10: return SpecialChartComposer.configureWaterfallChart()
        elif selectedIndex == 11: return SpecialChartComposer.configurePyramidChart()
        elif selectedIndex == 12: return SpecialChartComposer.configureFunnelChart()
        elif selectedIndex == 13: return SpecialChartComposer.configureErrorbarChart()

    def chartConfigurationWithSelectedIndex(self, selectedIndex):
        if selectedIndex == 0:  return CustomStyleChartComposer.configureColorfulBarChart()
        elif selectedIndex == 1:  return CustomStyleChartComposer.configureColorfulGradientColorBarChart()
        elif selectedIndex == 2:  return CustomStyleChartComposer.configureDiscontinuousDataChart()
        elif selectedIndex == 3:  return CustomStyleChartComposer.configureMixedLineChart()
        elif selectedIndex == 4:  return CustomStyleChartComposer.configureColorfulColumnChart()
        elif selectedIndex == 5:  return CustomStyleChartComposer.configureGradientColorBarChart()
        elif selectedIndex == 6:  return CustomStyleChartComposer.configureColorfulBarChart()# 待添加
        elif selectedIndex == 7:  return CustomStyleChartComposer.configureWithMinusNumberChart()
        elif selectedIndex == 8:  return CustomStyleChartComposer.configureStepLineChart()
        elif selectedIndex == 9:  return CustomStyleChartComposer.configureStepAreaChart()
        elif selectedIndex == 10: return CustomStyleChartComposer.configureNightingaleRoseChart()
        elif selectedIndex == 11: return CustomStyleChartComposer.configureCustomSingleDataLabelChart()
        elif selectedIndex == 12: return CustomStyleChartComposer.configureChartWithShadowStyle()
        elif selectedIndex == 13: return CustomStyleChartComposer.configureColorfulGradientAreaChart()
        elif selectedIndex == 14: return CustomStyleChartComposer.configureColorfulGradientSplineChart()
        elif selectedIndex == 15: return CustomStyleChartComposer.configureGradientColorAreasplineChart()
        elif selectedIndex == 16: return CustomStyleChartComposer.configureSpecialStyleMarkerOfSingleDataElementChart()
        elif selectedIndex == 17: return CustomStyleChartComposer.configureSpecialStyleColumnOfSingleDataElementChart()
        elif selectedIndex == 18: return CustomStyleChartComposer.configureAreaChartThreshold()
        elif selectedIndex == 19: return CustomStyleChartComposer.customScatterChartMarkerSymbolContent()
        elif selectedIndex == 20: return CustomStyleChartComposer.customLineChartMarkerSymbolContent()
        elif selectedIndex == 21: return CustomStyleChartComposer.configureTriangleRadarChart()
        elif selectedIndex == 22: return CustomStyleChartComposer.configureQuadrangleRadarChart()
        elif selectedIndex == 23: return CustomStyleChartComposer.configurePentagonRadarChart()
        elif selectedIndex == 24: return CustomStyleChartComposer.configureHexagonRadarChart()
        elif selectedIndex == 25: return CustomStyleChartComposer.drawLineChartWithPointsCoordinates()
        elif selectedIndex == 26: return CustomStyleChartComposer.customSpecialStyleDataLabelOfSingleDataElementChart()
        elif selectedIndex == 27: return CustomStyleChartComposer.customBarChartHoverColorAndSelectColor()
        elif selectedIndex == 28: return CustomStyleChartComposer.customChartHoverAndSelectHaloStyle()
        elif selectedIndex == 29: return CustomStyleChartComposer.customSplineChartMarkerStatesHoverStyle()
        elif selectedIndex == 30: return CustomStyleChartComposer.customNormalStackingChartDataLabelsContentAndStyle()
        elif selectedIndex == 31: return CustomStyleChartComposer.upsideDownPyramidChart()
        elif selectedIndex == 32: return CustomStyleChartComposer.doubleLayerPieChart()
        elif selectedIndex == 33: return CustomStyleChartComposer.doubleLayerDoubleColorsPieChart()
        elif selectedIndex == 34: return CustomStyleChartComposer.disableSomeOfLinesMouseTrackingEffect()
        elif selectedIndex == 35: return CustomStyleChartComposer.configureColorfulShadowSplineChart()
        elif selectedIndex == 36: return CustomStyleChartComposer.configureColorfulDataLabelsStepLineChart()
        elif selectedIndex == 37: return CustomStyleChartComposer.configureColorfulGradientColorAndColorfulDataLabelsStepAreaChart()
        elif selectedIndex == 38: return CustomStyleChartComposer.disableSplineChartMarkerHoverEffect()
        elif selectedIndex == 39: return CustomStyleChartComposer.configureMaxAndMinDataLabelsForChart()
        elif selectedIndex == 40: return CustomStyleChartComposer.customVerticalXAxisCategoriesLabelsByHTMLBreakLineTag()
        elif selectedIndex == 41: return CustomStyleChartComposer.noMoreGroupingAndOverlapEachOtherColumnChart()
        elif selectedIndex == 42: return CustomStyleChartComposer.noMoreGroupingAndNestedColumnChart()

    def chartOptionsConfigurationWithSelectedIndex(self, selectedIndex):
        if selectedIndex ==  0:   return ChartOptionsComposer.configureLegendStyle()
        elif selectedIndex ==  1: return ChartOptionsComposer.simpleGaugeChart()
        elif selectedIndex ==  2: return ChartOptionsComposer.gaugeChartWithPlotBand()
        elif selectedIndex ==  3: return ChartOptionsComposer.configureChartWithBackgroundImage()
        elif selectedIndex ==  4: return ChartOptionsComposer.customAreaChartYAxisLabelsAndGridLineStyle()#自定义曲线填充图图的 Y 轴 的 Labels 和 elif selectedIndex ==式
        elif selectedIndex ==  5: return ChartOptionsComposer.adjustYAxisMinValueForChart()
        elif selectedIndex ==  6: return ChartOptionsComposer.configureTheMirrorColumnChart()
        elif selectedIndex ==  7: return ChartOptionsComposer.adjustTheXAxisLabels()
        elif selectedIndex ==  8: return ChartOptionsComposer.adjustGroupPaddingBetweenColumns()
        elif selectedIndex ==  9: return ChartOptionsComposer.configureAAPlotBandsForChart()
        elif selectedIndex == 10: return ChartOptionsComposer.configureAAPlotLinesForChart()
        elif selectedIndex == 11: return ChartOptionsComposer.customAATooltipWithJSFuntion()
        elif selectedIndex == 12: return ChartOptionsComposer.customXAxisCrosshairStyle()
        elif selectedIndex == 13: return ChartOptionsComposer.configureXAxisLabelsFontColorWithHTMLString()
        elif selectedIndex == 14: return ChartOptionsComposer.configureXAxisLabelsFontColorAndFontSizeWithHTMLString()
        elif selectedIndex == 15: return ChartOptionsComposer.configure_DataLabels_XAXis_YAxis_Legend_Style()
        elif selectedIndex == 16: return ChartOptionsComposer.configureXAxisPlotBand()
        elif selectedIndex == 17: return ChartOptionsComposer.configureDoubleYAxisChartOptions()
        elif selectedIndex == 18: return ChartOptionsComposer.configureTripleYAxesMixedChart()
        elif selectedIndex == 19: return ChartOptionsComposer.configureDoubleYAxesAndColumnLineMixedChart()
        elif selectedIndex == 20: return ChartOptionsComposer.configureDoubleYAxesMarketDepthChart()
        elif selectedIndex == 21: return ChartOptionsComposer.customAreaChartTooltipStyleLikeHTMLTable()
        elif selectedIndex == 22: return ChartOptionsComposer.customAxesGridLineStyle()
        elif selectedIndex == 23: return ChartOptionsComposer.customRadarChartStyle()
        elif selectedIndex == 24: return ChartOptionsComposer.customColumnrangeChartStyle()
        elif selectedIndex == 25: return ChartOptionsComposer.customXAxisLabelsBeImages()#自定义曲线面积图 X 轴 labels 为一组图片🖼
        elif selectedIndex == 26: return ChartOptionsComposer.configureTriangleRadarChart()#带有颜色标志带の三角形雷达图
        elif selectedIndex == 27: return ChartOptionsComposer.configureQuadrangleRadarChart()#带有颜色标志带の四角形雷达图
        elif selectedIndex == 28: return ChartOptionsComposer.configurePentagonRadarChart()#带有颜色标志带の五角形雷达图
        elif selectedIndex == 29: return ChartOptionsComposer.configureHexagonRadarChart()#带有颜色标志带の六角形雷达图
        elif selectedIndex == 30: return ChartOptionsComposer.configureSpiderWebRadarChart()#带有颜色标志带の🕸蜘蛛网状雷达elif selectedIndex ==
        elif selectedIndex == 31: return ChartOptionsComposer.configureComplicatedCustomAreasplineChart()#复杂自定义曲线填充图 1
        elif selectedIndex == 32: return ChartOptionsComposer.configureComplicatedCustomAreasplineChart2()#复杂自定义曲线填充图 2
        elif selectedIndex == 33: return ChartOptionsComposer.configureComplicatedCustomAreasplineChart3()#复杂自定义曲线填充图 3
        elif selectedIndex == 34: return ChartOptionsComposer.yAxisOnTheRightSideChart()#y轴在右侧的图表
        elif selectedIndex == 35: return ChartOptionsComposer.doubleLayerHalfPieChart()#双层嵌套的玉阕图
        elif selectedIndex == 36: return ChartOptionsComposer.customAreasplineChartTooltipContentWithHeaderFormat()#通过 tooltip 的 elif selectedIndex ==erFormat 属性来自定义 曲线填充图的 to
        elif selectedIndex == 37: return ChartOptionsComposer.customAreaChartTooltipStyleWithTotalValueHeader()#浮动提示框 header 显示总值信息
        elif selectedIndex == 38: return ChartOptionsComposer.configureYAxisLabelsNumericSymbolsMagnitudeOfAerasplineChart()#自定义 Y 轴的 elif selectedIndex ==ls 国际单位符基数及国际单位符
        elif selectedIndex == 39: return ChartOptionsComposer.timeDataWithIrregularIntervalsChart()#X 轴时间不连续的折线图
        elif selectedIndex == 40: return ChartOptionsComposer.logarithmicAxisLineChart()#对数轴折线图📈
        elif selectedIndex == 41: return ChartOptionsComposer.logarithmicAxisScatterChart()#对数轴散点elif selectedIndex ==
        elif selectedIndex == 42: return ChartOptionsComposer.disableMixedChartInactiveAnimationEffect()#禁用混合图表的 inactive 动画效果
        elif selectedIndex == 43: return ChartOptionsComposer.adjustBubbleChartMinAndMax()#调整气泡图的 min 和 max 相关属性
        elif selectedIndex == 44: return ChartOptionsComposer.customLineChartDataLabelsFormat()#自定义曲线图的 DataLabels 的 format 属性
        elif selectedIndex == 45: return ChartOptionsComposer.customLineChartDataLabelsFormat2()#自定义曲线图的 DataLabels 的 format elif selectedIndex ==简易方法)
        elif selectedIndex == 46: return ChartOptionsComposer.complicatedScatterChart()#复杂的自定义散点图


    def NewItem(self, event):
        testChartModel = CustomStyleChartComposer.setUpColorfulBarChart()
        self.aa_drawChartWithChartModel(testChartModel)

        # text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        # if text != '':
        #     self.listbox.Append(text)

    def OnRename(self, event):
        testChartModel = CustomStyleChartComposer.setUpColorfulGradientColorChart()
        self.aa_drawChartWithChartModel(testChartModel)

        # sel = self.listbox.GetSelection()
        # text = self.listbox.GetString(sel)
        # renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)
        #
        # if renamed != '':
        #     self.listbox.Delete(sel)
        #     item_id = self.listbox.Insert(renamed, sel)
        #     self.listbox.SetSelection(item_id)

    def OnDelete(self, event):
        testChartModel = CustomStyleChartComposer.setUpDiscontinuousDataChart()
        self.aa_drawChartWithChartModel(testChartModel)

        # sel = self.listbox.GetSelection()
        # if sel != -1:
        #     self.listbox.Delete(sel)

    def OnClear(self, event):
        testChartModel = CustomStyleChartComposer.configureMixedLineChart()
        self.aa_drawChartWithChartModel(testChartModel)

        # self.listbox.Clear()/


def main():

    app = wx.App()
    ex = Example(None)

    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    # app = QApplication(sys.argv)

    # testChartOptions = ChartOptionsComposer.configureDoubleYAxesAndColumnLineMixedChart()
    # testChartOptions = testChartModel.aa_toAAOptions()

    # testChartOptions = JSFuncOptionsComposer.customAreasplineChartTooltipStyleByDivWithCSS()

    # testJson = AAJsonConverter.convertObjectToPureJson(testChartOptions)
    # print(testJson)
    #
    # testPrettyJson = AAJsonConverter.convertObjectToPureJson(testChartOptions)
    # print(testPrettyJson)
    # json_str = json.dumps(aaChartModel2, ensure_ascii=False)
    # json_str2 = json.dumps(aaChartModel2, ensure_ascii=False)
    # print(json_str)

    main()

    # app = wx.App()
    # frm = MyHtmlFrame(None, "Simple HTML Browser")
    # frm.Show()
    # app.MainLoop()
