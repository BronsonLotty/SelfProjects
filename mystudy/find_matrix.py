#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:59:22 2018

@author: xutingxi
"""
matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


def searchMatrix( matrix, target):
    m=len(matrix)
    n=len(matrix[0])
    rowlist=list(map(lambda x:x[-1],matrix))
    for i in range(m-1,-1,-1):
        if rowlist[i]==target:
            return True
        elif rowlist[i]<target:
            if i==m-1:
                return False
            else:
                index=i+1
                break
        else:
            if i>0:
                continue
            else:
                index=0
                
    print(index)            
    collist=matrix[index]
    if target<collist[0]:
        return False
    
    for j in range(n):
        if collist[j]==target:
            return True
        elif collist[j]<target:
            continue
        else:
            pass
    return False
    
searchMatrix( matrix, 5)        



class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        j=0
        i=m-1
        while i<m and j<n and i>=0 and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                j+=1
            elif matrix[i][j]>target:
                i-=1
            else:
                return False
        return False
            
            
mysolution=Solution()
mysolution.searchMatrix(matrix,12)



class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        ans=self.sort(nums,n)
        
        return ans[-k]
    def sort(self,nums,n):
        for i in range(n):
            for j in range(n-1,i-1,-1):
                if nums[j]<nums[j-1]:
                    temp=nums[j]
                    nums[j]=nums[j-1]
                    nums[j-1]=temp
        return nums
    


my=Solution()
nums=[3,2,1,5,6,4] 
k = 2
my.findKthLargest(nums,k)















