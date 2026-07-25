class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We want to use hashmap to
        numMap = {}

        for i in range(0,len(nums)):
            value = target - nums[i]
            if value in numMap:
                return [numMap[value], i]
            numMap[nums[i]] = i