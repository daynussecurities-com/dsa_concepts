nums1 = [1,2]
nums2 = [3,4, 6, 8, 7, 9]

def median(num1, num2):
    merged = num1 + num2
    sort_array = sorted(merged)
    length = len(sort_array)

    if length % 2 == 0:
        l_med_value = sort_array[length // 2 - 1]
        r_med_value = sort_array[length // 2]
        return r_med_value + l_med_value / 2
    else:
        return sort_array[len(sort_array) // 2]

rep = median(nums1, nums2)
print(rep)