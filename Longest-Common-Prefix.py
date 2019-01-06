class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        stop = False
        if len(strs) == 0:
            return prefix
        for x in range(len(strs[0])):
            char = strs[0][x]
            prefix += str(char)
            for candidate in strs:
                if len(candidate) == 0:
                    prefix = ''
                    stop = True
                    break
                if x > len(candidate)-1 or char != candidate[x]:
                    stop = True
                    prefix = prefix[:len(prefix)-1]
                    break
            if stop:
                break
        return prefix


if __name__ == '__main__':
    soln = Solution()
    print(soln.longestCommonPrefix(['aca', 'cba']))
