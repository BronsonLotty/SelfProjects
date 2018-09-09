#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:46:38 2018

@author: xutingxi
"""


#根据前序和中序遍历结果，重建二叉树


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution():
    def __init__(self):
        self.newdict={}        
    # 返回构造的TreeNode根节点
    def str_reConstructBinaryTree(self, pre, tin):
        # write code here
        root=pre[0]
        Node=TreeNode(root)
        self.newdict[Node.val]=Node
        tin_rootindex=tin.index(root)
        ltin=tin[:tin_rootindex]
        lnum=len(ltin)
        lpre=pre[1:lnum+1]
        try:
            rtin=tin[tin_rootindex+1:]
            rpre=pre[lnum+1:]
        except:
            rtin=[]
            rpre=[]
        rnum=len(rtin)            
        if lnum*rnum==0:
            if lnum+rnum==0:
                Node.right=None
                Node.left=None
            if rnum==0 and lnum!=0:
                Node.right=None
                Node.left=lpre[0]
                self.str_reConstructBinaryTree( lpre, ltin)
            if lnum==0 and rnum!=0:
                Node.left=None
                Node.right=rpre[0]
                self.str_reConstructBinaryTree( rpre, rtin)          
        else  :
            Node.left=lpre[0]
            self.str_reConstructBinaryTree(lpre, ltin)
            Node.right=rpre[0]
            self.str_reConstructBinaryTree( rpre, rtin)
        return self.newdict
    def reConstructBinaryTree(self,rpre, rtin):
        result=self.str_reConstructBinaryTree( pre, tin)
        key=list(result.keys())
        
        res=[result[key[0]].val]
        n=len(result)
        for i in range(1,n):
            #res.append(result[res[i-1]].val)
            if result[res[i-1]].left!=None:
                res.append(result[res[i-1]].left)
            if result[res[i-1]].right!=None:    
                res.append(result[res[i-1]].right)
        return res
    
        
my=Solution()    
pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6] 
res=my.reConstructBinaryTree(pre,tin)























        