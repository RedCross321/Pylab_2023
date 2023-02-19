def make_anonymous_factorial():
    """Возвращает выражение, которое вычисляет факториал.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # нельзя использовать связывание, рекурсивные вызовы, создавать свои функции
    >>> check(LAB_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return lambda x: x*make_anonymous_factorial()(x-1) if x>0 else 1
    return (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
print(make_anonymous_factorial()(5))

