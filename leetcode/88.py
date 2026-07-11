nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

for i in nums2:
    if i is not nums1:
        if i != 0:
            nums1.append(i)
for j in nums1:
    if j != 0:
        nums1.append(j)

print(sorted(nums1))
