tup1 = ('cat','dog','mouse','bird')
dttup = ('mouse',1,'hello')
nesttup = ('mouse',[1,2,3],(9,8,7))
print(tup1,"all following are for tup1")
print("2nd index is:",tup1[2])
print("slicing 1st 2 element",tup1[0:3])
for i in tup1:
    print("hello",i)
print(dttup,"all following are for dttup")
print("2nd index is:",dttup[2])
print("slicing 1st 2 element",dttup[0:3])
print(nesttup,"all following are for nesttup")
print("2nd index is:",nesttup[2])
print("last tupp 2 index index is:",nesttup[2][2])
print("slicing 1st 2 data types",nesttup[0:1])


