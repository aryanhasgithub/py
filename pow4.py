def pow4(n):
    return n>0 and n&(n-1)==0 and (n-1)%3==0
num = int(input("Number:"))
if pow4(num):
    print(num, "is a power of 4")
else:
    print(num, "is not a power of 4")