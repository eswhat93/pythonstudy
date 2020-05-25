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

#print(solution(array1, commands1))


#20200525
#1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
def solution(board):
    answer = 1234
    cnt=1
    stand=0

    # 첫번째 줄에 1이 있으면 연속되는 길이를 구한다
    for i in range(len(board)-1):
        if board[i] == 1:
            stand = 1
        else:
            stand = 0
        for j in range(i+1,len(board)):
            if board[j] == stand :
                cnt += 1
            else:
                cnt = 1
    return cnt

data = [1,0,0,1]
#data = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,0]]

print(solution(data))