class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] < target:
                continue;
            else:
                return i
        return i+1

def main():
    sln = Solution()
    print sln.searchInsert([1,3,5,6], 0)

if __name__ == '__main__':
    main()