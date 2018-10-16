'''冒泡排序'''

import copy as cy
class BubbleSort(object):
    def __init__(self):
        pass
    def swap(self,L,i,j):
        temp = cy.deepcopy(L[j])
        L[j] = cy.deepcopy(L[i])
        L[i] = cy.deepcopy(temp)
        return L
    def bubblesort(self,L):
        self.length = len(L)
        for j in range(self.length):
            for i in range(self.length-1):
                if L[i] > L[i+1]:
                    L = self.swap(L,i,i+1)
        return L


L = [1, 3, 5, 0, 2, 5, 9, 8]
mybubblesort = BubbleSort()
newL = mybubblesort.bubblesort(L)
print(newL)


'''简单选择排序'''
class SelectSort(object):
    def __init__(self):
        pass
    def swap(self,L,i,j):
        temp = cy.deepcopy(L[j])
        L[j] = cy.deepcopy(L[i])
        L[i] = cy.deepcopy(temp)
        return L
    def selectsort(self,L):
        for i in range(len(L)):
            minvalue = L[i]
            minindex = i
            for j in range(i+1,len(L)):
                if minvalue > L[j]:
                    minvalue = L[j]
                    minindex = j
            if i != minindex :
                L = self.swap(L,i,minindex)
        return L


L = [1, 3, 5, 0, 2, 5, 9, 8]
myselectsort = SelectSort()
newL = myselectsort.selectsort(L)
print(newL)



'''直接插入排序'''
class InsertSort(object):
    def __init__(self):
        pass
    def insertsort(self,L):
        for i in range(len(L)):
            minvalue = cy.deepcopy(L[i])
            for j in range(i-1,-1,-1):
                if minvalue < L[j]:
                    L[j+1] = cy.deepcopy(L[j])
                else:
                    L[j+1] = cy.deepcopy(minvalue)
                    break
                if j == 0:
                    L[0] = cy.deepcopy(minvalue)
        return L
#if __name__ == "__main__":
L = [1, 3, 5, 0, 2, 5, 9, 8]
myinsertsort = InsertSort()
newL = myinsertsort.insertsort(L)
print(newL)

"""快速排序"""
class QuickSort(object):
    def __init__(self):
        pass
    def quicksort(self,L):
        length = len(L)
        if length == 1:
            return L
        elif length == 0:
            return []
        else:
            midvalue = L[length//2]
            right = []
            left = []
            equal =[]
            for i in range(length):
                if L[i] > midvalue:
                    right.append(L[i])
                elif L[i] == midvalue:
                    equal.append(L[i])
                else:
                    left.append(L[i])

            return self.quicksort(left) + equal + self.quicksort(right)

L = [1, 3, 5, 0, 2, 5, 9, 8]
myquicksort = QuickSort()
newL = myquicksort.quicksort(L)
print(newL)


'''堆排序'''

class HeapAdjust(object):
    def __init__(self):
        pass
    def heapadjust(self,L):
        pass









