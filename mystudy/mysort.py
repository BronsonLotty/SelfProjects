#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 07:51:39 2018

@author: xutingxi
"""

周三下午/晚上：树和图的遍历，插入删除
周四：数据库/查找
周五+周末：深度学习：自然语音处理/推荐算法/图像处理
18，19，20:深度学习/机器学习
21:30:论文写作




#冒泡排序初级-交换排序
#class struct():
#    def __intial__(self,l):
#        self.length=len(l)
#        
#    def swap(self,l,i,j):
#        import copy
#        temp=copy.deepcopy(l[i])
#        l[i]=copy.deepcopy(l[j])
#        l[i]=copy.deepcopy(temp)
#            return l
l=[12,20]
def swap(l,i,j):
        import copy
        temp=copy.deepcopy(l[i])
        l[i]=copy.deepcopy(l[j])
        l[j]=copy.deepcopy(temp)
        return l
swap(l,0,1)

def sort1(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l=swap(l,i,j)
    return l

a=[2,4,7,2,1,3,0,9,5]

sort1(a)


#冒泡排序
def sort2(l):
    for i in range(len(l)-1):
        for j in range(len(l)-2,i-1,-1):
            if l[j]>l[j+1]:
                l=swap(l,j,j+1)
                
    return l


sort2(a)


#冒泡排序-升级版
def sort3(l):
    flag=True
    for i in range(len(l)-1):
        if flag:
            flag=False
            for j in range(len(l)-2,i-1,-1):
                if l[j]>l[j+1]:
                    l=swap(l,j,j+1)
                    flag=True
    return l

sort3(a)
    
    
    
#简单选择排序
'''
简单选择排序类似于交换排序，不过交换排序总是进行交换，而简单选择排序每次是交换n-i中最小的一个，时间复杂度为n2，性能略优于冒泡排序
 
'''
import copy
def sort4(l):
    for i in range(len(l)):
        min_index=copy.deepcopy(i)
        for j in range(i+1,len(l)):
            if l[min_index]>l[j]:
                min_index=copy.deepcopy(j)
        if min_index!=i:
            l=swap(l,i,min_index)

    return #即使什么都不返回，变量本身也会发生变化，不会返回新的变量
a=[2,4,7,2,1,3,0,9,5]

sort4(a)


#直接插入排序
'''
直接插入排序，是通过设置哨兵（哨兵起到存储临时值的作用），将较大的值一次插入到已经有序的序列中，时间负责度为n2/4，性能由于简单选择排序
如果数据量比较少，或基本有序，则适用于直接插入排序
'''
def sort5(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            temp=copy.deepcopy(l[i])
            for j in range(i-1,-2,-1):
                if l[j]>temp:
                    l[j+1]=l[j]
                else:
                    break
            l[j+1]=temp
    return l
sort5(a)


#希尔排序
'''
直接插入排序，是反复比较相邻两个变量的值的大小，如果序列较长，则效率较慢，而希尔排序是将一个序列
先通过分组排序，将序列一步步变得整体有序，直至最终有序,时间复杂度为n^1.5
'''
def sort6(l):
    increment=copy.deepcopy(len(l))
    while increment>1:
        increment=int(increment/3+1)
        for i in range(increment+1,len(l)):
            if l[i]<l[i-increment]:
                temp=copy.deepcopy(l[i])
                for j in range(i-increment,-increment-1,-increment):
                    if l[j]>temp:
                        l[j+increment]=l[j]
                    else:
                        break
                l[j+increment]=temp
    return l


sort6(a)

#堆排序

'''
堆排序类似于比赛制，先两两比赛，赢的再和赢得比赛，直至选到最大值。
有两个问题需要解决：第一，如何将一个无序数组构造成大顶堆。第二，顶堆元素输出元素后，剩下的n-1个元素
如何构建新的堆.适合数目较多的排序，为不稳定排序，跳跃式排序，时间复杂度为nlogn
'''
#建堆函数
def HeapList(l,s):
    
    l[0]=copy.deepcopy(l[s])
    i=2*s
    while i <len(l)-1:
        if l[i]<l[i+1]:
            i+=1
        if l[0]>l[i]:
            break
        l[s]=l[i]
        s=i
        i=2*s 
    l[s]=l[0]
    return l
test=a
test=l=[50,10,90,30,70,40,80,60,20]
HeapList(test,4)

#构建堆排序函数
def HeapSort(l):
    start=[0]
    start.extend(l)
    l=start
    length=len(l)
    for s in range(int(length/2),0,-1):
        l=HeapList(l,s)
    #至此，构建堆排序结束
    #print(l[1:])
    result=[]
    while len(l)>3:
        swap(l,1,-1)
        result.append(l[-1])
        l=HeapList(l[:-1],1)
    if l[2]>l[1]:
        result.append(l[2])
        result.append(l[1])
    else:
        result.append(l[1])
        result.append(l[2])
    return result

test=l=[50,10,90,30,70,40,80,60,12,23,56,75,122,20]

HeapSort(test)






#归并排序
#首先定义merge函数
'''
merge(l,i,m，n)其中l为有序的数列l（i，，，m，，，，n）其中i-m是有序的，m+1-n是有序的，
返回result,也相当于对一个list中位置在i，n之间的数进行排序
'''
def merge(l,i,m,n):
    j=m+1
    result=[]
    if i!=0:
        strresult=l[:i]
        strresult.extend(result)
        result=strresult
    while i<=m and j<=n:
        if l[i]<l[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(l[j])
            j+=1
    if i<=m:
        result.extend(l[i:m+1])
    if j<=n:
        result.extend(l[j:n+1])
    
    if n!=len(l)-1:
       result.extend(l[n+1:]) 
    
    return result
        
l=[10,0,6,2,6,3,1]        
            
merge(l,0,0,1)#对前n个数进行排序

#定义归并函数
'''
mergepass(l,s,n)：将序列l相邻s的子序列两两归并,n为序列长度，返回result,时间复杂度为nlogn
'''


def mergepass(l,s,n):
    result=l
    i=0
    while i<n-2*s+1:
        print(i)        
        result=merge(result,i,i+s-1,i+2*s-1)
        print(result)
        i=i+2*s
    if i<n-s:
        result=merge(result,i,i+s-1,n-1)

    return result
l=mergepass(l,1,7)

#定义归并排序函数
def MergeSort(l):
    k=1
    result=l
    while k<len(l):
        result=mergepass(result,k,len(l))
        k=2*k
        result=mergepass(result,k,len(l))
        k=2*k
    
    return  result


l=[23,7,8]
MergeSort(l)




#快速排序

def quicksort(l):
    if len(l)==0:
        return []
    elif len(l)==1:
        return l
    else:
        index=int(len(l)/2)
        midval=l[index]
        lvals=[ival for ival in l if ival<midval]
        rvals=[ival for ival in l if ival>midval]
        midvals=[ival for ival in l if ival==midval]
    return quicksort(lvals) + midvals + quicksort(rvals)
    
l=[12,45,63,2,4,3,87,3]

quicksort(l)






    
        
searchMatrix( matrix, 5)        




