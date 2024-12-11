file1 =open("hello.txt",'r')
file2 = open("bye.txt",'w')
for line in file1.readlines():
    if not line.startswith("hello"):
        print(line)
        file2.write(line)

file2.close()
file1.close()        
        
    
        
        
    