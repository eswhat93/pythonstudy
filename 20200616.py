# divmond(a,b) = > a를 b로 나눌 때 몫과 나머지 => 큰수 다룰때 후자가 빠름
my_list = [[1,2],[3,4],[5,6]] 
#print(sum(my_list, []))

import itertools
#print(list(itertools.chain.from_iterable(my_list)))
# unpacking
#print(list(itertools.chain(*my_list)))

#list comprehension 이용
#print([element for array in my_list for element in array])

# reduce 함수 이용
from functools import reduce

#print(list(reduce(lambda x, y:x+y, my_list)))


def solution(mylist):
    answer = [[]]
    list(map(list,mylist))
    return answer

mylist = [2, 1]
#print(list(map(list,mylist)))



import collections
my_str = 'dfdefdgf'
answer=''
c=collections.Counter(my_str)
my_str=c.most_common()
print(my_str)
for i in range(len(my_str)):
    print(my_str[i][0])
    if my_str[0][1] == my_str[i][1]:
        print("같다",my_str[i][0])
        answer +=my_str[i][0]
print(answer)


#list comprehension
answer = [ i**2 for i in mylist if i%2==0]


#이진탐색
import bisect
mylist = [1,2,3,7,9,11,33]
print(bisect.bisect(mylist,0))

