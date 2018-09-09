#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:52:32 2018

@author: xutingxi
"""

'''
查找算法
1.最简单的方法是顺序查找，逐个比对
2.将数组先排序，使用有序表查找，常用方法是折半查找
3.有序表查找的进一步改良版是 插入查找
4.此外还可以使用块索引等索引查找方法
4.上述查找均为静态查找，动态查找最常用的方法是二叉排序树查找
我们将实现二叉排序树的构建，查找，插入和删除


'''


#============方法一：折半查找==================




def binary_search(mylist,key):
    '''
    输入：
        mylist:被查找的有序数组，构造有序数组，首先需要进行排序，同时记录下初始的index值
        *记录初始的index值可以模仿链表的方法将每一个值记录为一个list，如a=【【2，0】，【1，1】】
        其中【2，0】中2为值，0为该值在a中的位置
        key：被查找的关键字
        
    return：如果查找成功返回index ，否则返回false
    '''
    low=0
    high=len(mylist)-1
#    m=0.5
    m=(key-mylist[low]) /(mylist[high]-mylist[low])
    while low<=high:
        mid=int(low+(high-low)*m)
        if mylist[mid]==key:
            return mid
        elif mylist[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return  False

mylist=[1,4,7,9,13]
key=7
result=binary_search(mylist,key)



#=================方法二：插入查找=========================
'''
只需要修改mid的公式即可，将折半查找中的m修改为（key-mylist【low】）/（mylist【high】-mylist【low】）
'''






#==================方法三：构建二叉排序树===================
'''
构建二叉排序树和二叉排序树的插入操作是相同的
'''
#首先定义节点结构
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.lchild=None
        self.rchild=None   
    

class SortTree:
    def __init__(self,Node):
        self.Node=Node

    def search_BST(self,Node,key):
        '''
        输入：
        Node是本轮被查找的结点；key是要查找的关键字；Trees是字典，其中顺序存储所有结点，p是查找成功时
        返回key在Trees中的index，查找失败时记录最后被查找的结点在Trees结点中的位置
        
        return：查找成功返回 p，否则返回false
        
        '''
        if Node==None:
            return False
        elif key==Node.val:
            
            print('=')
            return True
        elif key<Node.val:
            print('<')
            p=self.search_BST(Node.lchild,key)
        else:
            print('>')
            p=self.search_BST(Node.rchild,key)
        return p

#测试
#Node=TreeNode(2)
#Node.lchild=TreeNode(1)
#Node.rchild=TreeNode(3)
#mysort=SortTree(Node)
#key=3
#mysort.search_BST(Node,key)

#====================将二叉树按照有序存储的方式保存在list中======

    def printTree(self,Node,res,time):
        if Node.lchild!=None:       
            res.append(Node.lchild.val)
        if Node.rchild!=None:
            res.append(Node.rchild.val)
        if time!=0:
            return
        if Node.lchild!=None:
            time+=1
            self.printTree(Node.lchild,res,time)
        if Node.rchild!=None: 
            time+=1
            self.printTree(Node.rchild,res,time)
        return res
    
#mysort=SortTree(Node)
#res=[Node.val]
#time=0
#result=mysort.printTree(Node,res,time)

#====================有序二叉树的插入=========================

    def insert_BST(self,Node,key,time):
        if key<Node.val:
            if Node.lchild==None:
                Node.lchild=TreeNode(key)
                return
            else:
                time+=1
                self.insert_BST(Node.lchild,key,time)
        if key>Node.val:
            if time==0:
                #xuyao  
                newNode=TreeNode(key)
                newNode.lchild=Node
                Node=newNode
                return
            else:
                if Node.rchild==None:
                    Node.rchild=TreeNode(key)
                    return 
                else:
                    time+=1
                    self.insert_BST(Node.rchild,key,time)          
        return  Node


#test
Node=TreeNode(2)
Node.lchild=TreeNode(1)
Node.rchild=TreeNode(3)    

mysort=SortTree(Node)
key=0
time=0
newNode=mysort.insert_BST(Node,key,time)


res=[Node.val]
result=mysort.printTree(newNode,res,time)




