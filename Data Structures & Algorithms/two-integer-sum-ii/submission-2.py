class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        i = 0
        j = len(numbers) - 1

        while i < j:
            while j > i:
                if numbers[i] + numbers[j] > target:
                    j -= 1
                if numbers[i] + numbers[j] < target:
                    i += 1
                if numbers[i] + numbers[j] == target:
                    res.append(i + 1)
                    res.append(j + 1)
                    return res