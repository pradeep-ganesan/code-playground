class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        middle = len(nums) / 2
        i = middle - 1
        j = middle + 1
        while i >= 0 or j < len(nums):
            if nums[i] + nums[middle] + 

def main():
    sln = Solution()

if __name__ == '__main__':
    main()