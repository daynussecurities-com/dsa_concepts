class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ''.join(filter(str.isalnum, s)).lower()
        if words == words[::-1]:
            return True
        return False