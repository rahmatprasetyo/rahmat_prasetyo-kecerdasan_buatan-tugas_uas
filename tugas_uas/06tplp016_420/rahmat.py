from matplotlib import pyplot as plt

class BaseFuzzy():

    def init(self):
        self.minimum = 0
        self.maximum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)
    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)

class Temp(BaseFuzzy):
    def _init_(self):
        self.t1 = 5
        self.t2 = 10
        self.t3 = 20
        self.t4 = 50
        self.tn = 60
        
    def freeze(self, x):
        # 0 - t1 = 1
        # t1 - t2 = down
        if x < self.t1:
            return 1
        elif self.t1 <= x <= self.t2:
            self.minimum = self.t1
            self.maximum = self.t2
            return self.down(x)
        else:
            return 0
        
    def cold(self, x):
        # t1 - t2 = up
        # t2 - t3 = down
        if self.t1 <= x <= self.t2:
            self.minimum = self.t1
            self.maximum = self.t2
            return self.up(x)
        elif self.t2 <= x <= self.t3:
            self.minimum = self.t2
            self.maximum = self.t3
            return self.down(x)
        else:
            return 0
    
    def warm(self, x):
        # t2 - t3 = up
        # t3 - t4 = down
        if self.t2 <= x <= self.t3:
            self.minimum = self.t2
            self.maximum = self.t3
            return self.up(x)
        elif self.t3 <= x <= self.t4:
            self.minimum = self.t3
            self.maximum = self.t4
            return self.down(x)
        else:
            return 0
        
    def hot(self, x):
        # t3 - t4 = up
        # t4-.... = 1
        if self.t3 <= x <= self.t4:
            self.minimum = self.t3
            self.maximum = self.t4
            return self.up(x)
        elif x > self.t4:
            return 1
        else:
            return 0

class Pressure(BaseFuzzy):
    def _init_(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 27
        self.p7 = 32
        self.p8 = 37
        self.p9 = 40
        self.pn = 45
    
    def verylow(self, x):
        if x < self.p1:
            return 1
        elif self.p1 <= x <= self.p3:
            self.minimum = self.p1
            self.maximum = self.p3
            return self.down(x)
        else:
            return 0

    def low(self, x):
        if self.p2 <= x <= self.p3:
            self.minimum = self.p2
            self.maximum = self.p3
            return self.up(x)
        if self.p3 <= x <= self.p4:
            self.minimum = self.p3
            self.maximum = self.p4
            return self.down(x)
        else:
            return 0

    def medium(self, x):
        if self.p3 <= x <= self.p5:
            self.minimum = self.p3
            self.maximum = self.p5
            return self.up(x)
        if self.p5 <= x <= self.p6:
            return 1
        if self.p6 <= x <= self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.down(x)
        else:
            return 0

    def high(self, x):
        if self.p6 <= x <= self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.up(x)
        if self.p7 <= x <= self.p9:
            self.minimum = self.p7
            self.maximum = self.p9
            return self.down(x)
        else:
            return 0

    def veryhigh(self, x):
        if self.p8 <= x <= self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.up(x)
        elif x > self.p9:
            return 1
        else:
            return 0

class Speed(BaseFuzzy):
    def _init_(self):
        self.s1 = 20
        self.s2 = 40
        self.s3 = 60
        self.s4 = 80
        self.sn = 100
        
        self.freeze = Temp.freeze(x)
        self.cold = Temp.cold(x)
        self.warm = Temp.warm(x)
        self.hot = Temp.hot(x)
        
        self.verylow = Temp.verylow(x)
        self.low = Temp.low(x)
        self.medium = Temp.medium(x)
        self.high = Temp.high(x)
        self.veryhigh = Temp.veryhigh(x)
        
    def slow(self, x):
        if self.hot == 1 and self.high == 1:
            return 1
        elif self.freeze == 1 and self.veryhigh == 1:
            return 1
        elif self.cold == 1 and self.veryhigh == 1:
            return 1
        elif self.warm == 1 and self.veryhigh == 1:
            return 1
        elif self.hot == 1 and self.veryhigh == 1:
            return 1
        else:
            return 0
        
    def fast(self):
        if self.freeze == 1 and self.verylow == 1:
            return 1
        elif self.cold == 1 and self.verylow == 1:
            return 1
        elif self.warm == 1 and self.verylow == 1:
            return 1
        elif self.hot == 1 and self.verylow == 1:
            return 1
        elif self.freeze == 1 and self.low == 1:
            return 1
        else:
            return 0
        
    def steady(self):
        if self.cold == 1 and self.low == 1:
            return 1
        elif self.warm == 1 and self.low == 1:
            return 1
        elif self.hot == 1 and self.low == 1:
            return 1
        elif self.freeze == 1 and self.medium == 1:
            return 1
        elif self.cold == 1 and self.medium == 1:
            return 1
        elif self.warm == 1 and self.medium == 1:
            return 1
        elif self.hot == 1 and self.medium == 1:
            return 1
        elif self.freeze == 1 and self.high == 1:
            return 1
        elif self.cold == 1 and self.high == 1:
            return 1
        elif self.warm == 1 and self.high == 1:
            return 1
        else:
            return 0
        
    
    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x = [0, 40, 60, 80, 100, 120]
        #Slow
        y = [1, 1, 0, 0, 0, 0]
        plt.plot(x, y, label='Slow', color='C0')
        
        #steady
        y = [0, 0, 1, 1, 0, 0]
        plt.plot(x, y, label='Steady', color='C1')
        
        #FAST
        y = [0, 0, 0, 0, 1, 1]
        plt.plot(x, y, label='Fast', color='C2')
        
        plt.show()
    

temp =Temp()
press = Pressure()

x = 30

print('freeze', temp.freeze(x))
print('cold', temp.cold(x))
print('warm', temp.warm(x))
print('hot', temp.hot(x))

print('very low', press.verylow(x))
print('low', press.low(x))
print('medium', press.medium(x))
print('high', press.high(x))
print('very High', press.veryhigh(x))

Speed.graph(x)