def solution(progresses, speeds):
    answer = []
    temp=[]
    i=0
    for a,b in zip(progresses, speeds):
        #a + (b*n) >=100
        n=1
        while n<=100 :
            if b >=(100-a)/n:
                temp.append(n)
                break
            n +=1
    print(temp)
    cnt=1
    for j in range(len(temp)):
        if  j==0:
            stand = temp[0]
        else:
            if temp[j] < stand:
                cnt += 1
            else :
                print(temp[j])
                answer.append(cnt)
                if j == len(temp)-1 and temp[j]!= stand  :
                    answer.append(1)
                stand = temp[j]
                cnt=1
                
    return answer


progresses = [93,30,55]
speeds	=	[1,30,5]
#return =	[2,1]


print(solution(progresses, speeds))
print('test')