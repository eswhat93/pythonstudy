#1
class Calculator:
    def __init__(self):
        self.value=0
    
    def add(self, val):
        self.value +=val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
#객체변수는 객체안에서만 고유한 값

#2
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value>=100:
            self.value=100
cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)

print(cal2.value)
#3
print(all([1,2,abs(-3)-3]))#False 하나라도 걸리면

print(chr(ord('a')))
#4

print(list(filter(lambda x: x>0,[1, -2, 3, -5, 8, -3] )))
#5


#6

#7