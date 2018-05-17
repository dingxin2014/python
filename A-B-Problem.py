class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        while b != 0:
            a, b = (a ^ b) & 0xffffffff, (a & b) << 1
        return a


if __name__ == '__main__':
    s = Solution()
    a = 200
    b = -190
    print(s.aplusb(a,b))
å

