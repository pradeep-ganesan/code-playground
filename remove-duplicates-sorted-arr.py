class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, sz = 1, len(nums)
        while i < sz:
            if nums[i] == nums[i-1]:
                x = nums.pop(i)
                nums.append(x)
                sz -= 1
            else:
                i += 1
        return sz

def main():
    sln = Solution()
    print sln.removeDuplicates([0,1,2,2,3,6,6,7])

if __name__ == '__main__':
    main()