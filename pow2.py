def pow2(n):
  if n <= 0:
        return False
  return (n & (n - 1)) == 0

n = int(input("Enter a number: "))

if pow2(n):
    print(n, "is a power of 2")
else: 
    print(n, "is not a power of 2")