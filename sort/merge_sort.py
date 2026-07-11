def merge(list1, list2):
    i = 0
    j = 0
    results = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            results.append(list1[i])
            i += 1
        else:
            results.append(list2[j])
            j += 1

    while i < len(list1):
        results.append(list1[i])
        i += 1

    while j < len(list2):
        results.append(list2[j])
        j += 1

    return results


def merge_sort(lst1):
    if len(lst1) == 1:
        return lst1
    mid_value = int(len(lst1) / 2)
    print(mid_value)
    left = merge_sort(lst1[:mid_value])
    right = merge_sort(lst1[mid_value:])
    return merge(left, right)


liss = [2, 3, 1, 5, 7]

print(merge_sort([2, 3, 1, 5, 7]))



