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

class HeapSort(object):
    def __init__(self):
        pass
    def heapadjust(self,L,s,m):
        temp = L[s]
        j = s*2
        while j < m-1:
            if L[j] < L[j+1]:
                j+=1
            if temp >= L[j]:
                break
            else:
                L[s] = cy.deepcopy(L[j])
                s = cy.deepcopy(j)
                j = s*2
        L[s] = cy.deepcopy(temp)
        return L
    def swap(self,L,i,j):
        temp = cy.deepcopy(L[j])
        L[j] = cy.deepcopy(L[i])
        L[i] = cy.deepcopy(temp)
        return L
    def heapsort(self,L):
        for i in range(len(L)//2,0,-1):
            L = self.heapadjust(L,i,len(L))
        for i in range(1,len(L)):
            L = self.swap(L,1,len(L)-i)
            L = self.heapadjust(L,1,len(L)-i)
        return L

L = [1, 3, 5, 0, 2, 5, 9, 8]  #第一个数不参与排序，仅用来占位，保证二叉树 parent *2 = child
myheapsort = HeapSort()
newL = myheapsort.heapsort(L)
print(newL)

'''归并排序'''
class MergeSort(object):
    def __init__(self):
        pass
    def merge(self,L1,L2):
        L = []
        i = j = 0
        while i < len(L1) and j < len(L2):
            if L1[i] >= L2[j]:
                L.append(L2[j])
                j+=1
            else:
                L.append(L1[i])
                i += 1
        if i == len(L1):
            L.extend(L2[j:len(L2)])
        if j == len(L2):
            L.extend(L1[i: len(L2)])
        return L
    def mergesort(self,L):
        if len(L):
            st = 0
            ed = len(L)
            if st == ed - 1:
                return L
            else:
                mid = (st + ed)//2
                L1 = self.mergesort(list(L[st:mid]))
                L2 = self.mergesort(list(L[mid:ed]))
                return self.merge(L1,L2)

L = [1, 3, 5, 0, 2, 5, 9, 8]
mymergesort = MergeSort()
newL = mymergesort.mergesort(L)
print(newL)