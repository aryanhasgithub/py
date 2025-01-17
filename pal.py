num = int(input("enter number: "))
org_num = num
rev_num = 0
while num > 0 :
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

if org_num == rev_num :
    print(org_num, "is a palindrome")
else:
    print(org_num, "is not a palindrome")        