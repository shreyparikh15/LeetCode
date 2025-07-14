class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            rev_index = 26-(ord(s[i])-ord('a'))
            position = i+1
            prod = rev_index * position
            total += prod
        return total   