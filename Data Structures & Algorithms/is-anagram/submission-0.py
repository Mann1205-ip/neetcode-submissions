class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aMap = {} # string , counts
        bMap = {}

        for i in s:
            if i in aMap:
                aMap[i] = aMap.get(i ,0) + 1
            else:
                aMap[i] = aMap.get(i, 0) + 1
        
        for j in t:
            if j in bMap:
                bMap[j] = bMap.get(j ,0) + 1
            else:
                bMap[j] = bMap.get(j, 0) + 1

        for x in aMap:
            for y in bMap:
                if bMap != aMap:
                    return False
                return True