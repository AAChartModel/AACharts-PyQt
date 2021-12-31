from aacharts.aaenum.AAEnum import AAChartAnimationType

class AAAnimation: 
    duration: int;
    easing: AAChartAnimationType;

    def durationSet(self, prop: int):
        self.duration = prop
        return self
    
    def easingSet(self, prop: AAChartAnimationType):
        self.easing = prop
        return self