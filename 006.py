'''
将字符串写成一个紧凑的矩阵，将每两列形成的「V」型作为模型
第一行和最后一行每个元素之间的距离是2*(numRows-1)
其他行中，设行号为i，每个模型中同一行的元素之间距离为2*(numRows-(i+1))
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        new_s = ''
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = i
                while j <= len(s)-1:
                    new_s += s[j]
                    j += 2*(numRows-1)
            else:
                j = i
                while j <= len(s)-1:
                    if j+(2*(numRows-(i+1))) <= len(s)-1:
                        new_string = s[j]+s[j+(2*(numRows-(i+1)))]
                    else:
                        new_string = s[j]
                    new_s += new_string
                    j += 2*(numRows-1)

        return new_s
