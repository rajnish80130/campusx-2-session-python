# ************ session-2 campusx - python ************
# **********operators in python **********
# 1) Arthimetic operators
print(5+6)

print(5-6)

print(5*6)

print(5/2)

print(5//2)   #after divide return in integer not in float

print(5%2)

print(5**2)   #for square

# 2) Relational Operators
print(4>5)

print(4<5)

print(4>=4)

print(4<=4)

print(4==4)

print(4!=4)

# 3)Logical Operators
print(1 and 0)

print(1 or 0)

print(not 1)

# 4)Bitwise operation ----> in this operator we work on binary number firstly we change in binary and use it
# bitwise and
print(2 & 3)   # here firstly we change 2 and 3 in binary and we solve it if (1&0=0) and (1&1=1)

# bitwise or   # here firstly we change 2 and 3 in binary and we solve it if (1&0=1)
print(2 | 3)

# bitwise xor
print(2 ^ 3)

print(~3)       # here firstly we change 2 and 3 in binary and we solve it if (~1=0,~0=1)

print(4 >> 2)

print(5 << 2)

# 5)Assignment Operators

# =

# a = 2

a = 2

# a = a % 2

a %= 2

# a++ ++a  is not work in python
a += 2

print(a)

# 6)Membership Operators

 # in/not in

 # print('D' not in 'Delhi')

 # print(1 in [2,3,4,5,6])

 # Program - Find the sum of a 3 digit number entered by the user
num = int(input("enter a number "))
sum = 0
while num>0:
    num1 = num%10
    sum = sum + num1
    num = num//10

print(sum)

# ***********if-else statement***********
# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input('enter email')
password = input('enter password')

if email == 'nitish.campusx@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'nitish.campusx@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
  if password == '1234':
    print('Welcome,finally!')
  else:
    print('beta tumse na ho paayega!')
else:
  print('Not correct')

# min of 3 number

a = int(input('first num'))
b = int(input('second num'))
c = int(input('third num'))

if a<b and a<c:
  print('smallest is',a)
elif b<c:
  print('smallest is',b)
else:
  print('smallest is',c)

# menu driven calculator
menu = input("""
Hi! how can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
""")

if menu == '1':
  print('pin change')
elif menu == '2':
  print('balance')
else:
  print('exit')

# ***********modules************
# math
import math

math.sqrt(196)

# keyword
import keyword
print(keyword.kwlist)

# random
import random
print(random.randint(1,100))

# datetime
import datetime
print(datetime.datetime.now())

help('modules')   # for all modules

# ************Loops in Python*******
# while loops
number = int(input('enter the number'))

i = 1

while i<11:
  print(number,'*',i,'=',number * i)
  i += 1

# while loop with else

x = 1

while x < 3:
  print(x)
  x += 1

else:
  print('limit crossed')

# *******************Guessing game*************

# generate a random integer between 1 and 100
import random

jackpot = random.randint(1, 100)

guess = int(input('guess karo'))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print('galat!guess higher')
    else:
        print('galat!guess lower')

    guess = int(input('guess karo'))
    counter += 1

else:
    print('correct guess')
    print('attempts', counter)

# For loop demo

for i in {1,2,3,4,5}:
  print(i)