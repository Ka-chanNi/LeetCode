'''
this version is not so efficient
should optimize later
'''
def solution(nums1, nums2):
    all_list = nums1+nums2
    sorted_list = quick_sort(all_list)
    middle_index = len(sorted_list) // 2
    if middle_index * 2 != len(sorted_list):
        return sorted_list[middle_index]
    else:
        return (sorted_list[middle_index-1] + sorted_list[middle_index])/2.0

def quick_sort(all_list):
    if len(all_list) == 0:
        return []
    left_list =[]
    right_list = []
    middle = all_list[0]
    for item in all_list[1:]:
        if item <= middle:
            left_list.append(item)
        else:
            right_list.append(item)
    return quick_sort(left_list)+[middle]+quick_sort(right_list)


print(solution([1,3],[2]))