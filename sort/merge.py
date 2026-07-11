

def merge(list1, list2):
    merge_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    while i < len(list1):
        merge_list.append(list1[i])
        i +=1

    while j < len(list2):
        merge_list.append(list2[j])
        j += 1

    return merge_list

list1 = [1, 2, 3, 5]
list2 = [6, 8, 9]

# list1 = [1, 2, 5, 3]
# list2 = [6, 9, 8]

print(merge(list1, list2))