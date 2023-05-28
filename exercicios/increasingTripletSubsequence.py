class Solution(object):
    def increasingTriplet(self, nums):
        min1 = float('inf')  # Define o primeiro menor valor como infinito
        min2 = float('inf')  # Define o segundo menor valor como infinito

        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True

        return False