print("Hello, World!")

if 5 > 2:
  print("Five is greater than two!")

#This is a comment.

x = 7

y = "seven"

print(x)
print(y)
print(complex(x))

import datetime

x = datetime.datetime.now()

import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

tup = (2, "Ema", "2020–04–16")
lis = ["Seth", "Ema", "Eli"]
print (type(tup))
print (tup)
print (type(lis))
print (lis)
print (type(arr))
print (arr)

age = 22
name = 'Sharon'
# 1. f strings
print(f'Hello {name}')
# 2. % operator
print('Hey %s %s' % (name, name))
# 3. format
print(
 "My name is {}".format((name))
)
sentence = "My name is {1} and I am {0} years old"
print(sentence.format(age,name))


def logging(func):
  def log_function_called():
    print(f'{func} called.')
    func()
  return log_function_called
  
def my_name():
  print('chris')
def friends_name():
  print('naruto')
my_name()
friends_name()
#=> chris
#=> naruto

@logging
def my_name():
 print('chris')
@logging
def friends_name():
 print('naruto')
my_name()
friends_name()
#=> <function my_name at 0x10fca5a60> called.
#=> chris
#=> <function friends_name at 0x10fca5f28> called.
#=> naruto

for x in range(2,24,3):
    print (x)
    
    
class Car :
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
car = Car('red','100mph')
print(car.speed)
#=> '100mph'


"""
Instance methods : accept self parameter and relate to a specific instance of the class.
Static methods : use @staticmethod decorator, are not related to a specific instance, and are self-contained (don’t modify class or instance attributes)
Class methods : accept cls parameter and can modify the class itself
"""

class CoffeeShop:
    specialty = 'espresso'
    
    def __init__(self, coffee_price):
        self.coffee_price = coffee_price
    
    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for ${self.coffee_price}')
    
    # static method    
    @staticmethod
    def check_weather():
        print('Its sunny')
    # class method
    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')

coffee_shop = CoffeeShop('5')
c_s = CoffeeShop('10')
coffee_shop.make_coffee() #calling instance method
#=> Making espresso for $5
c_s.make_coffee()
coffee_shop.check_weather() #calling static method
#=> Its sunny

coffee_shop.change_specialty('drip coffee') #calling class method

#=> Specialty changed to drip coffee
coffee_shop.make_coffee()
#=> Making drip coffee for $5

c_s.make_coffee()

def func():
    return('Im a function')
    
print(func)
#=> function __main__.func>
print(func() )   
#=> Im a function

x = func
print(x)
print(x())

def add_three(x):
    return x + 3
li = [1,2,3]
print(list(map(add_three, li)))
print(map(add_three, li))
#=> [4, 5, 6]

from functools import reduce
def add_them(x,y):
    return x + y
li = [1,2,3,5]
print(reduce(add_them, li))
#=> 11


def isEven(x):
    if x % 2 == 0:
        return True        
    else:
        return False
li = [1,2,3,4,5,6,7,8]
print([i for i in filter(isEven, li)])
#=> [2, 4, 6, 8]
print(list(filter(isEven, li)))


name = 'text'
def add_chars(str1):
    print( id(str1) ) #=> 4353702856
    print( id(name) ) #=> 4353702856
    
    # new name, same object
    str2 = str1
    
    # creates a new name (with same name as the first) AND object
    str1 += 's' 
    print( id(str1) ) #=> 4387143328
    
    # still the original object
    print( id(str2) ) #=> 4353702856
    
    
add_chars(name)
print(name) #=>text

li = ['a','b','c']
print(li)
li.reverse()
print(li)

print('cat' * 3)

print(len([1,2,3] * 20))

a = [1,2]
b = [3,4,5]
print(a + b)
print(b+a)

a = [0,1,2,3,4,5,6,7,8,9]
print(a[2:8:2])

val = 10
val += 15
print(val)

print(bin(5))

s = 'A string with     white space'
print(''.join(s.split()))
#=> 'Astringwithwhitespace'
s = 'A string with     white space'

#=> 'Astringwithwhitespace'
print (s.replace(' ', ''))

li = ['a','b','c','d','e']
for idx,val in enumerate(li):
    print(idx, val)
