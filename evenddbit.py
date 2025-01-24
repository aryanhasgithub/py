def check(n):  
    if (n^1==n+1):
        return True
    else:
        return False
a = int(input("give no"))

if(check(a)):
    print("even")
else:
    print("odd")    