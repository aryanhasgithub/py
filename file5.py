f1 = open("hello.txt", "r")
f2 = open("bye.txt", "w")
cont = f1.readlines()

# Correcting the loop to use range
for i in range(1, len(cont) + 1):
    if i % 2 != 0:
        f2.write(cont[i - 1])

# Close the first file
f1.close()
f2.close()

f2 = open("bye.txt", "r")
print(f2.read())
f2.close()