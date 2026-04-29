class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = list(set(nums))
        if len(nums) == len(uniq):
            return False
        return True
        