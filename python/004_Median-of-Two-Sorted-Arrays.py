nums1 = [2, 3, 4]
nums2 = [1]


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def kthSmall(nums1, nums2, i, j, k):
            len1, len2 = len(nums1), len(nums2)
            if i >= len1:
                return nums2[k-1]
            if j >= len2:
                return nums1[k-1]
            if k == 1:
                return min(nums1[i], nums2[j])
            if len1 - i > len2 - j:
                return kthSmall(nums2, nums1, j, i, k)
            pa = min(len1 - i, (k // 2))
            pb = k - pa
            return kthSmall(nums1, nums2, i + pa, j, pb) if nums1[i + pa - 1] < nums2[j + pb - 1] else kthSmall(nums1, nums2, i, j + pb, pa)

        len_nums = len(nums1) + len(nums2)
        if len_nums % 2:
            return kthSmall(nums1, nums2, 0, 0, len_nums // 2 + 1)
        else:
            return 0.5 * (kthSmall(nums1, nums2, 0, 0, len_nums // 2) + kthSmall(nums1, nums2, 0, 0, len_nums // 2 + 1))


sol = Solution()
b = sol.findMedianSortedArrays(nums1, nums2)
print(b)
