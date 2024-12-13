import os

if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
    print("File removed successfully")
elif os.path.exists("newfilegen.txt"):
    os.remove("newfilegen.txt")  
else:
    print("The file does not exist")
    new_file = open("newfilegen.txt",'x')
    new_file.close()


f2 = open("new_file.txt",'w')
f2.write("hello world!")
f2.close()


    
    