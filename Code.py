class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for x in range(len(arr)-2):
            if all(num % 2 == 1 for num in arr[x:x+3]):
                return True
        return False
