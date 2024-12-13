with open ('new.txt',"w") as file :
    file.write("Hello World!")
    file.close()

with open ('new.txt',"r") as file :
    data = file.readlines()
    for line in data :
        word = line.split()
        print(word)
    file.close()    
    