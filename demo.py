import car
import math

print("this is my car",car.car3,car.car3_year)

val=math.sqrt(100)

# math module has been imported successfully ! 

print(val)
print(math.pow(5,2))
print(math.ceil(25.48))
print(math.floor(25.30))
print(math.pi)
print(math.e)
print(ord("a"))
print(chr(97))

# Escape Sequence is here ! \n \t \\ \' \"
print('ashif aman \nmohamed nafil ashif')
print('hello ashif \\ aman ')

name1='ashif'
name2='aman'

print(name1+' '+name2)
print(len(name1+name2))

# use pop(),append(),remove() in LIST !
# list are mutable but tuples are non-mutable !

products=['googel','microsoft','adobe','wipro','TCS']
marks=[49,59,69,100,59,59]

print(products[3])
print(len(products))
print(products.pop())
print(products)
print(products.remove('googel'))
print(products)
print(products.reverse())
print(products)
print(products.append('oracle'))
print(products)
print(max(marks))
print(sum(marks))
print(marks.count(100))

# tuples are list with immutable values !

devices=('laptop','tab','mobile','pc') #len(devices) and other functions that work in lists also work in here efficiently !

# named tuples !

from collections import namedtuple

MNC=namedtuple('MNC',['name','year','parent'])

google=MNC('google','1980','Alphabet')
oracle=MNC('oracle','1975','oracle')

print(google)
print(oracle)
print(google[2])

# sets ! mutable unordered no index  

apps={'google','youtube','whatsapp','instagram','duolingo'}
apps2={'googles','apps1','apps2','apps3','apps4'}
print(apps2)
print(len(apps2))
apps2.add('apps5')
print(apps2)
print(len(apps2))
print(apps)
print(apps2)
apps.update(apps2)
print(apps)

# Dictionary ! just like  meanings and the actual words in the dictionary !
# has mutable and has index but access it with key value.
# {key value:value}

teams={7:'ronaldo',10:'messi'}
print(teams[7])

teams[101]='imbappe'
print(teams)
 
teams[101]='imbappee'
print(teams)

del teams[101]
print(teams)

#formating datatypes !

num1=12
num2=10

print(num1+num2) # When input is given the type is default as string , so type convert them to int or float

# formating strings !

name36='ashif'
cost=27.48354
print(f'hello this is {name36}')
print(f'the price of the product is {cost:.2f}')

# IF ELSE statement in python !

temperature = 18

if temperature > 26 :
  	print('this day is hot')
else :
  	print('the day is cold\n\n\n')

# relational operator ! == != > < >= <=

age1=12
temp=29

if age1>18: # == != >= <= as well can be done here  
	print('he is able to vote')
else:
	print("he isn\'t able to vote")

# logical operator !

if (age1>18 and temp>25):
	print('both are true')
elif (age1>18 and temp>18) :
	print('they are not true')
else:
	print('half true and half false')

# Comparison of operator !
# this can work in tuple,list,dictionry,set and as well as in expresions .
a=10
b=20

if (a==b):
	print('hello ashif aman')
else:
	print("they are different\n\n")

# membership and identity operator !

grades=[59,67,89,99,100]
print(100 in grades)
print(98 not in grades) # in and not in are the membership operator works in all lists,sets,dictionary and so on.
print('\n\n')

# identity relationship

a1=20
b1=20

print(a1 is b1)
print(id(a1) is (b1)) # this shows false because its memory location are different .

# conditional expresions !

vehicles=1

print('you have',vehicles,('vehicle' if (vehicles==1) else 'vehicles')) # doing the whole if and else statement in a single line .

# Looping !

# While Loop !

var10 = 10

while (var10>5):
	print(var10)
	var10-=1


#print("Are you hungry !")
#ishungry=input()

#while(ishungry == 'yes' ) | (ishungry=='YES'):
#print("take a bite")
#print("Are you hungry !")
#ishungry=input()

# for Loop !

for name in reversed('ashif aman'):# reversed function will print things in reverse. 
	print(name) # you can do tuples,dictionaries,lists and strings in the for loop.

# Range !
print('\n\n\nenter your age ?\n\n')
age123=27## since the input function always takes the value in string,type cast it into int or float if you are entering a number value 

if age123 in range(18):
	print('you are not able to vote')
elif age123 in range(18,60):
	print('you are able to vote and you are not a senior citizen !')
elif age123 in range(18,60,2):
	print('you are not senior citizen and you age is even !')
elif age123 in range(18,100,2):
	print('you are senior citizen and you age is even !')
else:
	print('seriously are you alive !\n\n')

print('finished !')

# Nested Loop !

var114= range(3)
var6666=range(2)

for v in var114:
	print("Surah",v)
	for s in var6666 :
		print("versus",s)

# break and continue ! these things are confusing so be careful , and they are not advisable to use in your python program ..

var100 = 1

while var100<10:


	if(var100==6):
		var100+=1
		continue
 

	print(var100)
	var100+=1


# else part in the looping statement !

brand = ['bata','dell','hp','redmi']

for b in brand:
	print(b)
	if (b == "dell"):
	  break

else:
	print('all the items printed successfully !')

# enumurate function !

brand1 = ['puma','abibas','borito','americane tourister']

for(index,value) in enumerate(brand1):
	print(f'{value} is at {index}')

# unpacking !

(a,b,c)=(100,200,300)
print(c)

#  THIS DOES NOT WORK HERE MAY BE IN JUPYTER.. filepointer = open('simplilern2.py','r')

# how to take a element from the list and make it as variable and rest to another list !

list101=[1,2,3,4,5,6,7,8,9]

ones,*other=list101

print(ones)
print(other)

# a list containing a 100 zeros !

list102 = [100]*50

print(list102)