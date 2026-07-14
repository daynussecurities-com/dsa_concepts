from typing import  List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int("".join(map(str, digits)))
        math = nums + 1
        result = []
        for i in str(math):
            result.append(int(i))
        return result
        