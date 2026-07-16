"""
Input: nums = [3,30,34,5,9]
Output: "9534330"
Wrong Answer
232 / 236 testcases passed


Input
nums =
[0,0]

Use Testcase
Output
"00"
Expected
"0"
"""

# Multiple 0 return 0 not 00

nums = [0, 0]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):

            
                
                nums[i], nums[j] = nums[j], nums[i]
        

# print("".join(str(i) for i in nums))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
            nums[i], nums[j] = nums[j], nums[i]

print(str(int("".join(map(str, nums)))))