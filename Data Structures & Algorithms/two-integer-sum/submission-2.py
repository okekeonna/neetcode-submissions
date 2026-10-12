class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []

        for i, item  in enumerate(nums):
            for j, item1 in enumerate(nums):
                total = item + item1

                if(total == target and i != j):
                    answer.append(i)
                    answer.append(j)
                    return answer
                