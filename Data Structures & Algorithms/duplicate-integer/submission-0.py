class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index,item in enumerate(nums):            
            curr = item
            currIndex = index

            for z,x in enumerate(nums):
                if(x == item and z != currIndex):
                    return True

        return False
        