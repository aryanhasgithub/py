students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
def convert(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result
print("\n printing name of students in list form")
print(students)
print("\n printing name of students in dictonary form")
print(convert(students))