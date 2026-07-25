class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = False
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    dupe = True
        return dupe