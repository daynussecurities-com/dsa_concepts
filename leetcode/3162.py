
nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3
ans = 0

for i in nums1:
    for j in nums2:
        if i % (j * k) == 0:
            ans += 1

print(ans)