'''
copy from @chomolungma
'''


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in xrange(len(s)):
            # add the character at the begin and the end
            if i-maxLen >= 1
            and s[i-maxLen-1: i+1] == s[i-maxLen-1: i+1][::-1]:
                start = i-maxLen-1
                maxLen += 2
                continue

            # add the same character at the end
            if i-maxLen >= 0 and s[i-maxLen: i+1] == s[i-maxLen: i+1][:: -1]:
                start = i-maxLen
                maxLen += 1
        return s[start:start+maxLen]
