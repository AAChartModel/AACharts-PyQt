from typing import List
from enum import Enum

class AALinearGradientDirection(Enum):
    toTop = 0,           #⇧⇧⇧⇧⇧⇧
    toBottom = 1,        #⇩⇩⇩⇩⇩⇩
    toLeft = 2,          #⇦⇦⇦⇦⇦⇦
    toRight = 3,         #⇨⇨⇨⇨⇨⇨
    toTopLeft = 4,       #⇖⇖⇖⇖⇖⇖
    toTopRight = 5,      #⇗⇗⇗⇗⇗⇗
    toBottomLeft = 6,    #⇙⇙⇙⇙⇙⇙
    toBottomRight = 7,   #⇘⇘⇘⇘⇘⇘

class AAGradientColor:

    # oceanBlue: map = AAGradientColor.oceanBlueColor(AALinearGradientDirection.toTop)
    #
    # sanguine: map = AAGradientColor.sanguineColor(AALinearGradientDirection.toTop)
    #
    # lusciousLime: map = AAGradientColor.lusciousLimeColor(AALinearGradientDirection.toTop)
    #
    # purpleLake: map = AAGradientColor.purpleLakeColor(AALinearGradientDirection.toTop)
    #
    # freshPapaya: map = AAGradientColor.freshPapayaColor(AALinearGradientDirection.toTop)
    #
    # ultramarine: map = AAGradientColor.ultramarineColor(AALinearGradientDirection.toTop)
    #
    # pinkSugar: map = AAGradientColor.pinkSugarColor(AALinearGradientDirection.toTop)
    #
    # lemonDrizzle: map = AAGradientColor.lemonDrizzleColor(AALinearGradientDirection.toTop)
    #
    # victoriaPurple: map = AAGradientColor.victoriaPurpleColor(AALinearGradientDirection.toTop)
    #
    # springGreens: map = AAGradientColor.springGreensColor(AALinearGradientDirection.toTop)
    #
    # mysticMauve: map = AAGradientColor.mysticMauveColor(AALinearGradientDirection.toTop)
    #
    # reflexSilver: map = AAGradientColor.reflexSilverColor(AALinearGradientDirection.toTop)

    # neonGlow: map = AAGradientColor.neonGlowColor(AALinearGradientDirection.toTop)
    #
    # berrySmoothie: map = AAGradientColor.berrySmoothieColor(AALinearGradientDirection.toTop)
    #
    # newLeaf: map = AAGradientColor.newLeafColor(AALinearGradientDirection.toTop)
    #
    # cottonCandy: map = AAGradientColor.cottonCandyColor(AALinearGradientDirection.toTop)
    #
    # pixieDust: map = AAGradientColor.pixieDustColor(AALinearGradientDirection.toTop)
    #
    # fizzyPeach: map = AAGradientColor.fizzyPeachColor(AALinearGradientDirection.toTop)
    #
    # sweetDream: map = AAGradientColor.sweetDreamColor(AALinearGradientDirection.toTop)
    #
    # firebrick: map = AAGradientColor.firebrickColor(AALinearGradientDirection.toTop)
    #
    # wroughtIron: map = AAGradientColor.wroughtIronColor(AALinearGradientDirection.toTop)
    #
    # deepSea: map = AAGradientColor.deepSeaColor(AALinearGradientDirection.toTop)
    #
    # coastalBreeze: map = AAGradientColor.coastalBreezeColor(AALinearGradientDirection.toTop)
    #
    # eveningDelight: map = AAGradientColor.eveningDelightColor(AALinearGradientDirection.toTop)

    # @staticmethod
    # def oceanBlue():
    #     return AAGradientColor.linearGradient1(AALinearGradientDirection.toTop, "#2E3192", "#1BFFFF")


    @staticmethod
    def oceanBlueColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#2E3192","#1BFFFF")

    @staticmethod
    def sanguineColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#D4145A","#FBB03B")

    @staticmethod
    def lusciousLimeColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#009245","#FCEE21")

    @staticmethod
    def purpleLakeColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#662D8C","#ED1E79")

    @staticmethod
    def freshPapayaColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#ED1C24","#FCEE21")

    @staticmethod
    def ultramarineColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#00A8C5","#FFFF7E")

    @staticmethod
    def pinkSugarColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#D74177","#FFE98A")

    @staticmethod
    def lemonDrizzleColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#FB872B","#D9E021")

    @staticmethod
    def victoriaPurpleColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#312A6C","#852D91")

    @staticmethod
    def springGreensColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#009E00","#FFFF96")

    @staticmethod
    def mysticMauveColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#B066FE","#63E2FF")

    @staticmethod
    def reflexSilverColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#808080","#E6E6E6")

    @staticmethod
    def neonGlowColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#00FFA1","#00FFFF")

    @staticmethod
    def berrySmoothieColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#8E78FF","#FC7D7B")

    @staticmethod
    def newLeafColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#00537E","#3AA17E")

    @staticmethod
    def cottonCandyColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#FCA5F1","#B5FFFF")

    @staticmethod
    def pixieDustColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#D585FF","#00FFEE")

    @staticmethod
    def fizzyPeachColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#F24645","#EBC08D")

    @staticmethod
    def sweetDreamColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#3A3897","#A3A1FF")

    @staticmethod
    def firebrickColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#45145A","#FF5300")

    @staticmethod
    def wroughtIronColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#333333","#5A5454")

    @staticmethod
    def deepSeaColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#4F00BC","#29ABE2")

    @staticmethod
    def coastalBreezeColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#00B7FF","#FFFFC7")

    @staticmethod
    def eveningDelightColor(direction: AALinearGradientDirection):
        return AAGradientColor.linearGradient1(direction, "#93278F", "#00A99D")

    @staticmethod
    def linearGradient0(
        startColor: str,
        endColor: str):
        return AAGradientColor.linearGradient1(
            AALinearGradientDirection.toTop,
            startColor,
            endColor
            )

    @staticmethod
    def linearGradient1(
        direction: AALinearGradientDirection,
        startColor: str,
        endColor: str):
        return AAGradientColor.linearGradient2(
            direction,[
               [0, startColor],
               [1, endColor]
               ])

    @staticmethod
    def linearGradient2(
        direction: AALinearGradientDirection,
        stops: List):
        linearGradient: map = AAGradientColor.linearGradientDirectionDictionary(direction)
        return {
            "linearGradient": linearGradient,
            "stops": stops #颜色字符串设置支持十六进制类型和 rgba 类型
            }

    @staticmethod
    def linearGradientDirectionDictionary(direction: AALinearGradientDirection):
        if direction == AALinearGradientDirection.toTop:
            return {"x1":0, "y1":1, "x2":0, "y2":0}
        elif direction == AALinearGradientDirection.toBottom:
            return {"x1":0, "y1":0, "x2":0, "y2":1}
        elif direction == AALinearGradientDirection.toLeft:
            return {"x1":1, "y1":0, "x2":0, "y2":0}
        elif direction == AALinearGradientDirection.toRight:
            return {"x1":0, "y1":0, "x2":1, "y2":0}
        elif direction == AALinearGradientDirection.toTopLeft:
            return {"x1":1, "y1":1, "x2":0, "y2":0}
        elif direction == AALinearGradientDirection.toTopRight:
            return {"x1":0, "y1":1, "x2":1, "y2":0}
        elif direction == AALinearGradientDirection.toBottomLeft:
            return {"x1":1, "y1":0, "x2":0, "y2":1}
        elif direction == AALinearGradientDirection.toBottomRight:
            return {"x1":0, "y1":0, "x2":1, "y2":1}

AAGradientColor.oceanBlue = AAGradientColor.oceanBlueColor(AALinearGradientDirection.toTop)
AAGradientColor.sanguine = AAGradientColor.sanguineColor(AALinearGradientDirection.toTop)
AAGradientColor.lusciousLime = AAGradientColor.lusciousLimeColor(AALinearGradientDirection.toTop)
AAGradientColor.purpleLake = AAGradientColor.purpleLakeColor(AALinearGradientDirection.toTop)
AAGradientColor.freshPapaya = AAGradientColor.freshPapayaColor(AALinearGradientDirection.toTop)
AAGradientColor.ultramarine = AAGradientColor.ultramarineColor(AALinearGradientDirection.toTop)
AAGradientColor.pinkSugar = AAGradientColor.pinkSugarColor(AALinearGradientDirection.toTop)
AAGradientColor.lemonDrizzle = AAGradientColor.lemonDrizzleColor(AALinearGradientDirection.toTop)
AAGradientColor.victoriaPurple = AAGradientColor.victoriaPurpleColor(AALinearGradientDirection.toTop)
AAGradientColor.springGreens = AAGradientColor.springGreensColor(AALinearGradientDirection.toTop)
AAGradientColor.mysticMauve = AAGradientColor.mysticMauveColor(AALinearGradientDirection.toTop)
AAGradientColor.reflexSilver = AAGradientColor.reflexSilverColor(AALinearGradientDirection.toTop)
AAGradientColor.neonGlow = AAGradientColor.neonGlowColor(AALinearGradientDirection.toTop)
AAGradientColor.berrySmoothie = AAGradientColor.berrySmoothieColor(AALinearGradientDirection.toTop)
AAGradientColor.newLeaf = AAGradientColor.newLeafColor(AALinearGradientDirection.toTop)
AAGradientColor.cottonCandy = AAGradientColor.cottonCandyColor(AALinearGradientDirection.toTop)
AAGradientColor.pixieDust = AAGradientColor.pixieDustColor(AALinearGradientDirection.toTop)
AAGradientColor.fizzyPeach = AAGradientColor.fizzyPeachColor(AALinearGradientDirection.toTop)
AAGradientColor.sweetDream = AAGradientColor.sweetDreamColor(AALinearGradientDirection.toTop)
AAGradientColor.firebrick = AAGradientColor.firebrickColor(AALinearGradientDirection.toTop)
AAGradientColor.wroughtIron = AAGradientColor.wroughtIronColor(AALinearGradientDirection.toTop)
AAGradientColor.deepSea = AAGradientColor.deepSeaColor(AALinearGradientDirection.toTop)
AAGradientColor.coastalBreeze = AAGradientColor.coastalBreezeColor(AALinearGradientDirection.toTop)
AAGradientColor.eveningDelight = AAGradientColor.eveningDelightColor(AALinearGradientDirection.toTop)


