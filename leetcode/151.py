class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

print(Solution().reverseWords("the sky is blue"))  # Output: "blue is sky the"