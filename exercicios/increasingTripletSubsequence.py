class Solution(object):
    def increasingTriplet(self, nums):
        min1 = float()
        min2 = float()  

        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True

        return False