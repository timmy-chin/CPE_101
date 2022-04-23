#Question A
str1 = "Hello"
str2 = input("enter name of class-mate")
birthYear = int(input("enter birth year of team member"))
age = 2022 - birthYear
print(str2, "will be", age, "years old in 2022")

#Question B
'''
100
1024
2.0
2.333333
2
1
30
'''

print((20+5)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(20+5*2)

# Question C
from datetime import datetime

now = datetime.now()
dtstring = now.strftime("%d/%m/%Y%H:%M:%S")
Day = dtstring[0:2]
Month = dtstring[3:5]
Year = dtstring[6:10]
Hour = dtstring[10:12]
Minute = dtstring[13:15]
Second = dtstring[16:18]

print('Day:',Day,'\nMonth:', Month,'\nYear:', Year,'\nHour:', Hour, '\nMinute:', Minute, '\nSecond:', Second)

