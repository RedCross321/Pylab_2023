def pingpong(n):
    """Возвращает n-ый элемент пинг-понг последовательности.
    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    "*** YOUR CODE HERE ***"
    def pingpong3(n):
        def eight(n):
            while n > 0:
                if n % 10 == 8:
                    return eight(n//10) + 1
                else:
                    return eight(n//10)
            return 0
        while n > 1:
            if n % 8 == 0 or eight(n) > 0:
                return pingpong3(n-1)*(-1) + 1
            return pingpong3(n-1) - 1
        return -1
    return pingpong3(n)

print(pingpong(8), "== 8")
print(pingpong(10), "== 6")
print(pingpong(15), "== 1")
print(pingpong(21), "== -1")
print(pingpong(22), "== -2")
print(pingpong(30), "== -2")
print(pingpong(68), "== 0")
print(pingpong(69), "== -1")
print(pingpong(80), "== 0")
print(pingpong(81), "== 1")
print(pingpong(82), "== 0")
print(pingpong(100), "== -6")

        # def pingpong2(n):
        #     if n > 1:
        #         if (n - 1) % 8 == 0 or eight(n-1) > 0:
        #             return pingpong(n-1)
        #         return pingpong2(n-1) - 1
        #     return 0
        # while n > 1:
        #     if (n - 1) % 8 == 0 or eight(n-1) > 0:
        #         return pingpong2(n-1)
        #     return pingpong(n-1) + 1
        # return 1