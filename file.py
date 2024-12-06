file1=input("file name 1 ")
file2=input("file name 2 ")
f1=open(file1, "r")
f2=open(file2, "r")
print("this is file 1 before appending- ",f1.read())
print("this is file 2 before appending- ",f2.read())

f1.close()
f2.close()

f1=open(file1, "a")
f2=open(file2, "r")

f1.write(f2.read())

f1.seek(0)
f2.seek(0)
f1.close()
f1=open(file1, "r")
print("appended f1- ",f1.read())

