'''
 for loop, range function: start, end , step.
and list function
'''
for i in range(100):
    print("nasa hacking",i,"%")
# more about range function
a= list(range(10))
print(a)
for i in range(10):
    print(i)

b = list(range(10))
c = list(range(3,10))
d = list(range(0,10,2))
e = list(range(0,10,3))
f = list(range(10,0,-2))
g = list(range(10,-2,-2))
print(g)

# more about for loop

a = "hello world "
for latter in a :
    print(latter)

bag = ["alu","payaj","tel", 20, 11.5, 544,22.25]
lst =[12,6554,22,1,2,358,45,254,1,3,8,7,9]
# for i in bag:
#     print(i)
for i in lst:
    if i<=10:
        print(i)

# # 3 and 5 dara divisible ber korbo
for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
# update variable and sum 1 to 10
sum = 0
for i in range(1,11):
    sum = sum + i 
print(sum)

# while loop
a= 0
while a <= 10:
    a= a+1
    print(a)

# break keyword in for and while loop
for i in range(10):
    if i ==5:
        break
    print(i)

a=1
while a<=10:
    a=a+1
    if a ==5:
        break
    print(a)

# continue
for i in range(10):
    if i ==5:
        continue
    print(i)

a=0
while a <=10:
    a = a+1
    if a ==5:
        continue
    print(a)

# infinity loop
while True :
    a = input("your name:")
    if a == "quit" or a == "q":
        break
    print(a)