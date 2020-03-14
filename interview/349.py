class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) > len(set2):
            set1, set2 = set2, set1
        return [x for x in set1 if x in set2]
