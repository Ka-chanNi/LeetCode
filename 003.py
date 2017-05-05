class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]]+1
            else:
                maxLength = max(maxLength, i - start + 1)
            used_char[s[i]] = i
        
        return maxLength
