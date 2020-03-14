class Solution:
    # 暴力，双重循环 O(m*n)

    # O(m+n) hashtable
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1

        d = dict()
        for i in nums1:
            if i not in d:
                d[i] = 0
            d[i] += 1

        k = 0
        for j in nums2:
            if j in d and d[j] > 0:
                nums1[k] = j
                d[j] -= 1
                k += 1

        return nums1[:k]

    # 当数据是有序，使用此方法
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        nums1.sort()
        nums2.sort()

        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]
