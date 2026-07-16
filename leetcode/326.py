"""
Example:

Input: n = 27
Output: true
Explanation: 27 = 33
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False

obj = Solution()
print(obj.isPowerOfThree(45))