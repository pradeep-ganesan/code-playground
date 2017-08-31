class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(j, i) for i, j in enumerate(nums)]
        nums.sort(reverse=True)
        print nums
        i, j = 0, len(nums) - 1

        while True:
            sumnum = nums[i][0] + nums[j][0]
            print nums[i][0], nums[j][0]
            if sumnum > target:
                i += 1
                continue
            elif sumnum < target:
                j -= 1
                continue
            return sorted([nums[i][1], nums[j][1]])

def main():
    tsum = Solution()
    nums = [-1, -2, -3, -4 , -5]
    print tsum.twoSum(nums, -8)

if __name__ == '__main__':
    main()