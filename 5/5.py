def compose1(f, g):
    return lambda x: f(g(x))
def composite_identity(f, g):
    a1 = compose1(f, g)
    a2 = compose1(g, f)
    def youyr(x):
        if a1(x) == a2(x):
            return True
        else: 
            return False
    return lambda x: youyr(x)



add_one = lambda x: x + 1
square = lambda x: x**2
b1 = composite_identity(square, add_one)
print(b1(7))
