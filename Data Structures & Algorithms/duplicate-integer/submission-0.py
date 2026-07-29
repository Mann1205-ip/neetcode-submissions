class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aMap = {}

        for i, n in enumerate(nums):
            if n in aMap:
                return True
            else:
                aMap[n] = i
        return False
