nums = [2,2,1]
a = 0

for i in nums:
    a ^= i

print(a)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0

        for x in nums:
            a ^= x

        return a


