k = int(input())
A = input()
B = input()
zichuan = []
for i in range(len(A)-k+1):
    zichuan.append(A[i:i+k-1])
zichuanset = set(zichuan)
zichuan = list(zichuanset)

count = 0
for chuan in zichuan:
    for i in range(len(B)-k+1):
        if B[i:i+k-1] == chuan:
            count += 1

print(count)






# a= 'asfsdgsdgsdg'
# print(a[2])




import itertools
result = []
for i in itertools.combinations([1,2,3,4], 2):
    print(list(i))
    result.append(list(i))
    #print(''.join(i))
print (result.append(i))