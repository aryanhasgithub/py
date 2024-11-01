height=float(input("write your height"))#pls input 140
weight=float(input("write your weight in kg"))
bmi=weight/height**2
if bmi>=18.5:
    print("underweight")
elif bmi<=18.5:
    print("healthy")
elif bmi<=25:
    print("overweight")
elif bmi<=30:
    print("obese class 1")
elif bmi<=35:
    print("obese class 2")
elif bmi<=40:
    print("severly obese")
else:
    print("data is wrong")

num=int(input("enter no for checking if input is od or even"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")
    
import datetime

dateandtime=datetime.datetime.now()
print(dateandtime)
import calendar
calender=calendar.calendar(2024)
print(calender)





 