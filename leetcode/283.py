# """
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# """

# nums = [0,1,0,3,12]
# zeo = []
# result = []

# for i in nums:
#     if i == 0:
#         zeo.append(i)
#     else:
#         result.append(i)
# fi = result + zeo
# print(result)
# print(zeo)
# print(fi)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeo = []
        result = []

        for i in nums:
            if i == 0:
                zeo.append(i)
            else:
                result.append(i)
        
        fi = result + zeo
        nums[:] = fi
        return nums

obj = Solution()
nums = [0,1,0,3,12]
print(obj.moveZeroes(nums))