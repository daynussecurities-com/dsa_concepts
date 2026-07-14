from typing import List

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        mergerd_list = []
        output = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
               mergerd_list.append(nums1[i])
               i += 1
            else:
                mergerd_list.append(nums2[j])
                j += 1

        while i < len(nums1):
            mergerd_list.append(nums1[i])
            i += 1

        while j < len(nums2):
            mergerd_list.append(nums2[j])
            j += 1

        for i in mergerd_list:
            if i != 0:
                output.append(i)

        return output

               


re = Solution()
print(re.merge(nums1=nums1, nums2=nums2))




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mergerd_list = []
        output = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
               mergerd_list.append(nums1[i])
               i += 1
            else:
                mergerd_list.append(nums2[j])
                j += 1

        while i < len(nums1):
            mergerd_list.append(nums1[i])
            i += 1

        while j < len(nums2):
            mergerd_list.append(nums2[j])
            j += 1

        for i in mergerd_list:
            if i != 0:
                output.append(i)

        return output