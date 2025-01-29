def setbit(number,bit):
    mask = 1
    if bit&mask == 0 or bit&mask == 1:
        if number&(1<<(bit-1)):
            print("Bit is set")
        else:
            print("Bit is not set")
            
number = int(input("Number: "))
bit = int(input("Bit: "))
setbit(number,bit)
            
                