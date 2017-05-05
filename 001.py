class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        middle_map = []
        for num in nums:
            middle_map.append({'value': num, 'index': i})
            i += 1
        # print(middle_map)
        for elem in middle_map:
            surplus_one = target - elem['value']
            if surplus_one in nums:
                first_one_index = elem['index']
                for elem in middle_map:
                    if elem['value'] == surplus_one:
                        return [first_one_index, elem['index']]


if __name__ == '__main__':
    test = Solution()
    get_result = test.twoSum([1, 3, 5, 6], 9)
    print(get_result)
