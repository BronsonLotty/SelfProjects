class Solution:
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        length = len(strs)
        prefix = strs[0]
        for i, letter in enumerate(prefix):
            for string in strs:
                if len(string) > i:
                    if letter != string[i]:
                        if i == 0:
                            result = ""
                            return result
                        else:
                            result = prefix[:i]
                            return result
                else:
                    result = prefix[:i]
                    return result
        if i ==len(prefix)-1 :
            result = prefix
        return result

print(Solution().longestCommonPrefix(["flowe","flower","flowers"]))





A = [[1,2,3],
     [4,5,6]]


B = [[4,5,8],
     [4,6,6]]























