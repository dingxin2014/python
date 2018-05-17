class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    count += 1
                j /= 10
                if j == 0:
                    break
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.digitCounts(1, 12))