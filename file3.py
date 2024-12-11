file =open("hello.txt",'r')
print(file.readline())
file.close()

file = open("hello.txt",'r') 
print("this is only 3")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file = open("hello.txt",'r')
print("this is all lines")
for line in file:
    print(line)
    
file.close()    
    
