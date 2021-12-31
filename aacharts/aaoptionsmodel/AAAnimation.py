from aacharts.aaenum.AAEnum import AAChartAnimationType

class AAAnimation: 
    duration: int;
    easing: str;

    def durationSet(self, prop: int):
        self.duration = prop
        return self
    
    def easingSet(self, prop: AAChartAnimationType):
        self.easing = prop.value
        return self