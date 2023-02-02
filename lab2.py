print("Способ 1")
for i in range (1,1001):
    g = len(str(i))
    if i == (i ** 2) % 10 ** g:
        print(i)
print("Способ 2")
for i in range (1,1001):
    if str(i) == str(i**2)[-len(str(i)):]:
        print(i)