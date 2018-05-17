class Solution:
    def trailingZeros(self, n):
        factor_5 = 0
        factor_2 = 0
        for i in range(n + 1):
            print(i)
            _f_5, _f_2 = self.countFactor5(i), self.countFactor2(i)
            factor_5 += _f_5
            factor_2 += _f_2
            print(">>>")
            print(_f_2)
            print(_f_5)
        return min(factor_5, factor_2)



    def countFactor5(self, n, count = 0):
        if n == 0:
            return count
        n, y = n // 5, n % 5
        if y == 0:
            return self.countFactor5(n, ++count)
        else:
            return count

    def countFactor2(self, n, count = 0):
        if n == 0:
            return count
        n, y = n // 2, n % 2
        if y == 0:
            count += 1
            return self.countFactor2(n, count)
        else:
            return count


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeros(11))

