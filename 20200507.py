#최소공배수 최대공약수 다시보기
#sum square difference
sum1=0
sum2=0
for i in range(1,101):
    sum2 += i
    sum1 +=i*i

print((sum2*sum2) - (sum1))

#10001st prime 소수 구하기
#모르겄어서 정규표현식을 시작한다
# \d 숫자와 매치[0-9] \D 숫자가 아닌 것과 매치 [^0-9]
# \w 문자+숫자의 매치 [a-zA-Z0-9_]  
# . 어떤문자든 모두 매치 => 예)a.b=>a와 b사이 어떤 문자든 0이든 a든 (\n 뺴고 다됨)
# a.b 를 \n까지 포함하고 싶으면 
# re.compile('a.b', re.DOTALL)
# re.compile('a.b', re.S)

# a[.]b a.b 와 매치

#반복 * ca*t => a가 0번이든 2억번이든 반복 매칭 ct caat caaaaaaaat
#반복 + ca+t => ct(x) cat(o)
#반복 {m,n} m번반복, m ~ n번까지반복
# {1,} + 와 동일/ {0,} * 와 동일
# ? {0,1} 과 같음 ab?c = > ac abc 모두 가능

#파이썬에서 정규 표현식을 지원하는 re 모듈
import re
p = re.compile('ab+')
#매칭되면 객체를 돌려준다 <re.Match object; span=(0, 6), match='abbbbb'>
#매칭 안되면 None 돌려줌
# m = p.match("a")
#print(m)
#search는 문자열 전체 검색! match는 문자열의 처음부터 검색
m = p.search("3 ab")
print(m)

#findall 각 단어를 정규식과 매치하여 리스트로 돌려준다
a = re.compile("[a-z]+")
result = a.findall("life is too short")
print(result)

#finditer 반복 가능한 객체(iterator object)를 돌려준다

#match 객체의 메서드
#group() 매치된 문자열을 돌려준다 
#start() 매치된 문자열의 시작 위치 end() 매치된 문자열의 끝 위치
#span() 매치된 문자열의 (시작,끝) 에 해당하는 튜플을 돌려준다
#컴파일이랑 match 메서드 한번에 수행할때
m = re.match('[a-z]+', "python")

#대소문자 구별없이 매칭하는 옵션 re.I / re.IGNORECASE

# ^ 문자열의 처음 $문자열의 마지막 ^python 문자열의 처음은 항상 python python$ 문자열의 마지막은 항상
#\s - whitespace(공백!!!!!) 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
#\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
#\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
#\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

data = """python one
life is too short
python two
you need python
python three"""

#python 으로 시작하고 공백이고 문자나숫자오고
b = re.compile("^python\s\w+")
print(b.findall(data))

#python 으로 시작하고 공백이고 문자나 숫자가 오는데 그게 라인마다
c = re.compile("^python\s\w+", re.MULTILINE)
print(c.findall(data))

#re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다(단 [ ] 안에 사용한 whitespace는 제외). 그리고 줄 단위로 #기호를 사용하여 주석문을 작성할 수 있다.

#\ 가 문자열 자체임을 알려주기위해 \\로 이스케이프처리 파이썬은 \\\\ 네개
#파이썬 정규식에는 Raw String 규칙
c = re.compile(r'\\section')
print(c.match("\section d"))



#알고리즘 작성 연습하기!!!
# 잘 작성된 알고리즘을 이해하고 스스로 만든다 (모사!!그림을 잘 그리기 위해서는 잘 그린 그림 모방부터 시작?!!?!)
#알고리즘 연습방법
#알고리즘 문제 읽고 분석한 후에 간단하게 테스트용으로 매우 간단한 경우부터 복잡한 경우 순서대로 생각해보면서 연습장과 펜을 어쩌고적자ㅓㄱ비적
#가능한 알고리즘이 보이면 구현할 알고리즘을 세부항목으로 나누고 문장으로 세부항목을 나눠서 적어본돠
#코드화하기위해 데이터구조 또는 사용할 변수를 정리한다
#각 문장을 코드 레벨로 적는다
# 데이터 구조 또는 사용할 변수가 코드에 따라 어떻게 변하는지를 손으로 적음서 임의 데이터로 코드가 정상 동작하는지를 연습장ㄹ관오ㅓ마야ㅗ

#private protect public
#- 파이썬에서는 attribute, method 앞에 __(double underscore)를 붙이면 실제로 해당 이름으로 접근이 허용되지 않음
#- 실은 __(double underscore)를 붙이면, 해당 이름이 _classname__해당 속성 또는 메소드 이름 으로 변경되기 때문임

#정적메서드는 메서드 위에 @staticmethod를 붙인다/ 매개변수에 self 지정하지 않는다
#@ 데코레이터/ 인스턴스 내용과 상관없이 결과만 구하면 될때 정적메서드 사용

#급하지말고 순차적으로 생각해서......지금 이해 좀 안가는게 정적 동적 어쩌고 메타클래스 어쩌고.....크롤링 뭔가 쉬울거같음 그냥 가져오기만 하는거니까......지금은 알고리즘 종류 분석 해야할듯

#데이터구조와 알고리즘이란? 
#대량 데이터를 효율적으로 관리할 수 있는데이터구조, 자료구조=>효율적인 데이터 처리를 위해 데이터의 특성에 따라 체계적으로 데이터를 구조화하는것
# 효율적 예) 