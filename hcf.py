largnum = int(input("give largest number :"))
smanum = int(input("give smallest number :"))

while smanum:
    numstore = smanum 
    smanum = largnum % smanum
    largnum = numstore
print(largnum , "is the hcf ")    