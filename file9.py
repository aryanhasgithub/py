with open("hello.txt", "r")as fp:
    data1=fp.read()
with open("input.txt", "r")as fp:
    data2=fp.read()

data1+="\n"+data2
    
with open("out.txt", "w") as fp:
    fp.write(data1)
    
fp.close()    