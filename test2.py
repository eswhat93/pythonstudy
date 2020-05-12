a='881120-1068234'


print('19'+a[:5])
print(a[7:])

if a[7]=='1' : print('남자')
else : print('여자')



a='a:b:c:d'

a.replace(':','#')

print(a.replace(':','#'))


a= [1,3,5,4,2]
a.sort(reverse = True)


print(a)


a= ['Life', 'is', 'too', 'short'] 
print(" ".join(a))

#8
a= (1,2,3)
#b=tuple([4])
#print(a+b)
a = a+(4,)

#9
a= dict()

a['a'] = 'python'

print(a)

b = {'A':90, 'B':80, 'C':70}
print(b.pop('B'))

#11 중복제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = list(set(a))
print(a)

#12
