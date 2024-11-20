set1={1,2,3,3,4,5}
set2={1,2,3,7}
print("set1=",set1)
print("set2=",set2)
print("adding 9 to set 1")
set1.add(9)
print(set1,"added 9 ")
print("adding 10 to set 2")
set2.add(10)
print(set2,"added 9 ")
print(set1.difference(set2),"differences are given")
print(set1.symmetric_difference(set2),"all diffrences listed")
print("printing union of 2 sets ",set1.union(set2))
print("printing inter section of 2 sets",set1.intersection(set2))