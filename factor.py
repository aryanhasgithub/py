def func1(n):
    for i in range(1,n+1):
      if  n % i == 0 :
          print(i)
num = int(input("give number :"))          
func1(num)        