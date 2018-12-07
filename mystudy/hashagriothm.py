def get_count(n):
    mycount = 0
    for i in range(1, n + 1):
        strN = str(i)
        allsums = []
        perallsum = 0
        while perallsum not in allsums:
            perallsum = 0
            for j in strN:
                perallsum += int(j) ** 2
            if perallsum == 1:
                mycount += 1
                break
            else:
                allsums.append(int(strN))
                strN = str(perallsum)
    return mycount

print(get_count(18))