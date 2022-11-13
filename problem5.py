# 5. Write a function where I pass a sorted integer array and another array of integers
# and the function returns me start indexes of those values in second array.

# My solution's time complexity is O(K * log N), where K is the length of second array, and N is the length of the first array.

class Solution:
    def getStartIndexes(self, nums1, nums2):
        result = []
        for x in nums2:
            result.append(self.getStartIndex(nums1, x))
        return result

    def getStartIndex(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                right = mid
                if left == right:
                    return left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# TEST
print(Solution().getStartIndexes([0,0,1,1,1,3,3,3,9,9,9,9,20,20], [0,2,8,20]))
print(Solution().getStartIndexes([0,0,1,1,1,2,3,7,7,7,8,9,20,26], [0,2,8,20]))
print(Solution().getStartIndexes([0,0,1,1,1,3,3,3,9,9,9,9,20,20], [2,8,20]))
print(Solution().getStartIndexes([0,0,1,1,1,3,3,3,9,9,9,9,20,20], [2,10,22]))