def func(a):
    roman = {'I': 1, 'V': 5 , 'X': 10 ,'L': 50,'C': 100, 'D': 500 , 'M' : 1000}
    int1 = 0
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]] < roman[a[i+1]]:
            int1 -= roman[a[i]]
        else:
            int1 += roman[a[i]]
    return int1
a = input("ener roman numeral : ")      

print(func(a))              
                
            