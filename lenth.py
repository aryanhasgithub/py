def bits(n):
    count = 0
    while (n):
        count += 1
        n >>=1
    return count
inp = int(input("number"))
no = bits(inp)
print("no of bits",no)
