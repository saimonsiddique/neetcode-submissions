class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)
        current = 1
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                max_count = max(max_count, current)
                current = 1
        return max(max_count, current)
