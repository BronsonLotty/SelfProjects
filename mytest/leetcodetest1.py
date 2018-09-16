class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        nums=sorted(nums)
        results=[]
        if length <3:
            return results
        else:
            inum=0
            for i in range(length-2):
                inum+=1
                if inum>=2 :
                    if nums[i]==nums[i-1]:
                        continue
                jnum=0    
                for j in range(i+1,length-1):
                    jnum+=1
                    if jnum>=2 :
                        if nums[j]==nums[j-1]:
                             continue
                    presum=nums[i]+nums[j]
                    if presum>0:
                        break
                    if presum==0:
                        if nums[j]==nums[j+1]==0:                            
                            results.append([0,0,0])
                            continue
                        else:                          
                            break      
                    knum=0
                    for k in range(length-1,j,-1):
        #                print(k)
                        knum+=1
                        if knum>=2:
                            if nums[k]==nums[k+1]:                                
                                continue
                        mysum=nums[i]+nums[j]+nums[k]
                        if mysum==0:
                            values=sorted([nums[i],nums[j],nums[k]])
                            
 #                           if values not in results:
                            results.append(values)
                            break
                        elif mysum<0:
                            break
                        else:
                            continue
            return results
        
        
        
nums=[-1, 0, 1, 2, -1, -4]
mysolution=Solution()
results=mysolution.threeSum(nums)






