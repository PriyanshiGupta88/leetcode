class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            v=target-nums[i]
            if ((v in nums)and (nums.index(v)!=i)):
                l.append(i)
                l.append(nums.index(v))
                break
        return l
