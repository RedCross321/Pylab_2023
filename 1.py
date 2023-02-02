n = 18808848283
k = 9
d = 88
while n > 0:
    if str(d) == str(n)[-len(str(d)):]:
        k = 8
        print ("True")
        break
    n //= 10
if k == 9:
    print("False")
    

