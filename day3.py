
''' Problem 1:
 Take values of length and 
 breadth of a rectangle from user 
 and check if it is square or not
 '''
input_one = int(input('enter the rectangle length: '))
input_tow = int(input('enter the breadth length: '))
if input_one == input_tow:
    print("this is a square")
else:
    print("this a not square")

'''Problem 2 :
Take three integer input from user and 
find the largest number between 
using if-elif-else statement
'''
a = int(input())
b = int(input())
c = int(input())
# method 1
if a >= b:
    if a >= c:
        print(a,'is the largest')
    else :
        print(c,'is largest')

else:
    if b>= c:
        print(b,"is the largest")
    else:
        print(c,"is the largest")

# method 2:
if a>= b and a>= c:
    print(a, 'is the largest')
elif b>= c and b >= a:
    print(b, 'is the largest')
else:
    print(c, 'is the largest')


'''Problem 3:
Write a program using conditional 
Statement whether a number is even or odd.
'''
a = int(input())
if a % 2 == 0:
    print(a,"is even number")
else:
    print(a, "is odd number")

'''Problem 4:
Write a Program to take integer input from user 
and display the grade according to the following criteria.
'''
marks= int(input("enter your marks: "))

if marks > 90  :
    print("grade: A")
elif marks > 80 and marks <=90:
    print("grade: B")
elif marks >= 60 and marks <=80:
    print("grade: C")
else:
    print("grade: D") 


'''Problem 5:
Write a Program to check whether a year is leap year or not.
'''
year = int(input())

# method 1:
if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not leap year")
elif year % 4 == 0:
    print("leap year")
else : print("not leap year")

# method 2 :
if year % 400 == 0 and year % 100 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:  print("not leap year")

# method 3 :
if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("leap year")
else : print("not leap year")
