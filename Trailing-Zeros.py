class Solution:
    def trailingZeros(self, n):
        sum = 0
        while n != 0:
            n /= 5
            sum += n
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeros(11))
