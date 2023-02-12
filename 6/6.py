from operator import sub, mul
def make_anonymous_factorial():
    """Возвращает выражение, которое вычисляет факториал.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # нельзя использовать связывание, рекурсивные вызовы, создавать свои функции
    >>> check(LAB_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda y: mul(y, sub(y, 1))
print(make_anonymous_factorial()(5))
