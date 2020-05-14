# 선택정렬 
# 코딩 테스트를 준비하고.... 구조도준비하고....웹도 만들어봐야하느디 킄ㅋ킄킄크ㅡㅡ크크크ㅡ크ㅡ크크ㅡ크ㅡ카ㅡㅏㅢ아리ㅏ

#데이터가 두개일때 동작하는 선책정렬 알고리즘

#배우기전
data = [2,5,1,3,8,7]
 
def sel(dataList):
    for i in range(len(dataList)-1):
        index = dataList.index(min(dataList[i:]))
        dataList[i],dataList[index] = min(dataList[i:]), dataList[i]
        print(dataList)
    return data

print(sel(data))

#배우고나서
#데이터가 두개일때, 세개일때, 네개일때 짜면서 보완
#값대입해보고 알고리즘 구현 시작
#for stand in range(len(dataList) -1)로 반복
#lowest = stand 로 놓고
#for num in range(stand, len(dataList)) stand 이후부터 반복
    #내부 반복문 안에서 dataList[lowest] > dataList[num] 이면 lowest = num
#dataList[num],dataList[lowest]=dataList[lowest],dataList[num]

data2 = [2,5,1,3,8,7]
print("#############")
def selection_sort(data_list):
    for stand in range(len(data_list) - 1):
        lowest = stand
        for num in range(stand, len(data_list)):
            if data_list[lowest] > data_list[num]:
                lowest = num
        data_list[stand], data_list[lowest] = data_list[lowest], data_list[stand]
        print (data_list)
    return data_list

print(selection_sort(data2))

#재귀용법