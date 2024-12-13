f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

lineseen=set()
for line in f1:
    if line not in lineseen:
        lineseen.add(line)
        f2.write(line)
f1.close()
f2.close()
        
        