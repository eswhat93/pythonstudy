#mod1.py
def add(a, b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "__main__" :
    #수행될때 = cmd에 직접 파일 실행했을때 
    #수행안될때 = 대화형인터프리터/ 다른파일에서 이모듈 불러서 수행
    print(add(1,4))
    print(sub(4,2))

import sys
#명령프롬프트 창에서는 /\상관없음. 소스코드 안에서는 \\ 써야됨
#sys.path.append("C:\\javaTest\\mymod")
print(sys.path)
#mkdir mymod
#C:\javaTest>move mod1.py mymod

