class FourCal:
    #pass
    #파이썬 메서드의 첫번째 매개변수 이름은 관례적으로 self를 사용 / 다른이름 사용해도 상관없음
    #self는 객체 자동 전달
    def setdata(self,first,second):
        self.first = first
        self.second = second


a = FourCal()
print(a.setdata(1,2))
#print(type(a)) 
#pass : 아무것도 수행하지 않는 문법/ 임시로 코드 작성할때 주로 사용
#메서드의 또 다른 호출 방법
#1. 클래스를 통해 메서드를 호출
a=FourCal()
FourCal.setdata(a,4,2)
#2. 객체에서 메서드 호출할때는 self 반드시 생략하여 호출
a=FourCal()
a.setdata(4,2)

#객체에 생성되는 객체만의 변수를 객체변수라고 부른다
a = FourCal()
a.setdata(4,2)
print(a.first)

#클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다
#id함수는 객체의 주소를 돌려주는 파이썬 내장함수
print(id(a.first))
#생성자 __init__
class test:
    #생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#b = test()
#b.setdata(1,2)
#print(b.add())

#클래스의 상속
class MoreTest(test):
    #a의 b제곱 계산
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreTest(2,3)
print(c.pow())
#상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용.
#기존 클래스가 라이브러리 형태로 제공되거나 수정 허용되지 않는 상황이라면 상속 사용

#메서드 오버라이딩
class SafeTest(test):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

d=SafeTest(4,0)
print(d.div())
#클래스변수
class Family:
    lastname="김"

print(Family.lastname)

#모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일
#파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다
#import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다. 
#파이썬 라이브러리: 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈
import mod1

print(mod1.add(1,2))
#함수이름만 쓰고 싶을때
from mod1 import add 
#모든 함수 쓰고싶을때
from mod1 import *
