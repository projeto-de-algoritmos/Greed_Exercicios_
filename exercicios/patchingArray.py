class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0  # Contador para o número de patches adicionados
        missing = 1  # O menor número ausente no array
        index = 0    # Índice para percorrer o array
        length = len(nums)

        while missing <= n:
            if index < length and nums[index] <= missing:
                missing += nums[index]
                index += 1
            else:
                missing *= 2
                patches += 1

        return patches