class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_list = []
        for num in nums:
            if num != val:
                nums_list.append(num)
        for i in range(len(nums_list)):
            nums[i] = nums_list[i]
        
        return len(nums_list)
        