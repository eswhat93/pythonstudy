#array=[], commands= [a,b,c]
# array에서 a번째 부터 b번째까지 잘라서 배열을 만들고 그 배열의 c번째 수 출력
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        first = commands[i][0]
        end =commands[i][1]
        key =commands[i][2]

        test = array[first-1:end]
        test.sort()
        print(key)
        #print(test[key])
        #answer.append(test[key])

        #array = array.sort()
    #return answer

array1 = [1, 5, 2, 6, 3, 7, 4]
commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array1, commands1))