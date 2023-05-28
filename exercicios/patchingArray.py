class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0  
        missing = 1  
        i = 0    
        tam = len(nums)

        while missing <= n:
            if i < tam and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing = missing * 2
                patches += 1

        return patches