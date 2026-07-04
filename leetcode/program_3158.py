nums = [1,2, 3, 3, 2]
#
# class Solution:
#     def duplicateNumbersXOR(self, nums):
#         unqi = []
#         dub = []
#         for i in nums:
#             if i  not in unqi:
#                 unqi.append(i)
#             elif i not in dub:
#                 dub.append(i)
#
#         if len(dub) == 0:
#             print(0)
#         else:
#             print(sum(dub))
#
# obj = Solution()
# obj.duplicateNumbersXOR(nums=nums)


nums = [1,2]

seen = set()
ans = 0

for i in nums:
    if i in seen:
        ans ^= i
    else:
        seen.add(i)
print(ans)