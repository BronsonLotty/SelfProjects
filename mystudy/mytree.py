#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:55:25 2018

@author: xutingxi
"""
#学习树和图
'''
跟据前序遍历创建二叉树链表。
输入为list，表示从list中的i点为根结点，访问visit点，并创建where树
eg list=['A','B','#','D','#','#','C','#','#']  
'''
Trees={}
visit=0
global Trees
global visit

def CreateTree(l,index=0,visit=0,where='left'):
    print('index=%s,visit=%s'%(index,visit))
    if l[visit]=='#':
       newval={'LeftTree':'#','data':'#','RightTree':'#'}
       print('创建第%d结点,结点为空'%visit)
       Trees[visit]=newval
       if visit>=1 and where =='left':Trees[index]['LeftTree']=visit 
       if visit>=3 and where =='right':Trees[index]['RightTree']=visit        
       return visit
    else: 
        if visit>=1 and where =='left':Trees[index]['LeftTree']=visit 
        if visit>=3 and where =='right':Trees[index]['RightTree']=visit 
        newval={'LeftTree':0,'data':l[visit],'RightTree':0}
        print('创建第%d结点'%visit)
        Trees[visit]=newval
        index=visit
        visit+=1
        print('递归调用，创建左树')
        visit=CreateTree(l,index,visit,'left')#创建左树
        visit+=1
        #index=visit-1
        print('递归调用，创建右树')
        visit=CreateTree(l,index,visit,'right')#创建右树
        return visit
        
    
mysort=['A','B','#','D','#','#','C','#','#']        
CreateTree(mysort)    



'''
根据中序遍历创建二叉树链表。
'''
newval={'LeftTree':'#','data':'#','RightTree':'#'}
Tree={0:newval}
global Trees
def midsortTree(l,index=1,visit=1,where='left'):
    if l[visit]=='#':
        newval={'LeftTree':'#','data':'#','RightTree':'#'}
        Trees[visit]=newval
       # index+=1
        visit+=1   
        midsortTree(l,index,visit,'parent')
        midsortTree(l,index,visit,'right')        

        
    else:
        newval={'LeftTree':0,'data':l[visit],'RightTree':0}
        Trees[visit]=newval
        if visit>=1 and where =='parent':
            Trees[visit]['LeftTree']=index
            if l[visit]=='#':
               return
            index=visit
            visit+=1
            midsortTree(l,index,visit,'right')  
            
        if visit>=2 and where =='left':
            Trees[visit]['LeftTree']=index
            index=visit
            visit+=1            
            midsortTree(l,index,visit,'right')
        if visit>=2 and where =='right':Trees[index]['RightTree']=visit
              
    return












