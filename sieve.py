def sieveofe(n):
    prime =[True for i in range(n+1)]
    currnetno =2
    while(currnetno*currnetno <= n):
        if (prime[currnetno] == True):
            for i in range(currnetno*currnetno, n+1, currnetno):
                prime[i] = False
        currnetno += 1
    for p in range(2, n):
        if prime[p]:
            print(p, end = " ")
n = int(input("Enter the number: "))

sieveofe(n)
print("prime numbbers less than ", n )