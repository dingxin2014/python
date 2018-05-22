class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        assert m <= n
        a = 0xffffffff
        i = m
        while a != 0 and i < n:
            a &= (i + 1)
            i += 1
        return a
