# enumerate functions !

things = ['book','bike','clothes']

for(index,value) in enumerate(things):
	print(f'{value} is at index {index}')

# unpacking !

a,b = 20,30
print(b)
print(a,"\n\n")

# functions !

def ashif(s,t): 
# things inside the parathsis is called parameters,if the same functions is called and value is passed inside thats  called arguments (see below). 
	print(s*t)

print(ashif(10,20)) # you get a none in the output bacause , this is a void function.

# the void function donot return values instead print values (function above) , a value return function returns values (check below) 

def ashifaman(x,y):
	return (x*y)**2

aman=ashifaman(2,2) # you should take the value and print it using a extra variable,because you aren't print the value ,you are just returning it .
print(aman)

# dynamic typing in python !
# no values is assigned with a data type , python determines it while running .
def function(x,y):
	return x+y 

var100 = function(100,25)

print("\n\n\n",var100)

var110 = function(2.25,3.75)
print(var110,"\n\n\n")

# the function stub is a incomplete function !

# they donot show error,show none instead . must use pass keyword.

def area(q,w):
	pass


print("what is the height ?")
q = 2

print("what is the width ?")
w = 4

print("the area is :",area(q,w))
area(q,w)

# the locals() will give you the names and values of all local variables!

def check():
	a = 10
	b = 20
	c = 30

	print("\n\n\n",locals())

check()
print(globals(),"\n\n\n")

# *args and **kwargs !

def hello(a,b,*args):
	print(f'{a} is {b} years old')
	for ad in args:
		print(ad)

hello('bob',45,700)

def hi(a,b,**kwargs):
	print(f'{a} is {b} years old')

	for name,values in kwargs.items():
		print(name,":",values)
hi('ashif',21,date=14,month=7,year=2001,cgpa=8.9)

# multiple output function !

def thedu(bil):
	max = bil[0]
	min = bil[0]

	for x in bil:
		if(x > max):
			max = x
	for x in bil:
		if(x<min):
			min=x
	return max,min

bill = [39,78,99,56]
a,b=thedu(bill)

print(f'the maximum value is {a} and the minimum value is {b}')

# Documentation of a function !

def sum(a,b):
	"""
	this function calculates two numbers 
	"""
	print("\n\n\n",a*b)


sum(10,300) # you can get the things written in commentline using help().

print(help(sum))

# string splicing !

x = '0123456789'

grt = x[0::2] # starting index : end+1 th index : increment value

print(grt)

# hey check out this field width,fill charecter and left right align and floating point numbers !

print(f'{"Name":15s}{"Salary":7s}')
print("-"*20)
print(f'{"Ashif":15s}{"700000":7s}')
print(f'{"Noohu Mufeez":15s}{"900000":7s}')

print(f'{"Ashif":<15s}{"700000":7s}')#align
print(f'{"Ashif":>15s}{"700000":7s}')
print(f'{"Ashif":*>15s}{"700000":7s}') # fill
print(f'{"Ashif":*<15s}{"700000":7s}')
print(f'{"Ashif":15s}{700000.428938928392839283:.4}')



# some useful string functions !

aman8 = 'ashif aman'

print(aman8.upper()) # also works for lower .
print(aman8.isalnum()) # checks for only numbers and alphabets only , no spaces.
print(aman8.startswith('ash')) # also works for endswith().
print(aman8.count('a'))
print(aman8.replace('f','i'))
print(aman8.strip()) # removes spaces from the start and the end . 
print(aman8.capitalize(),"\n\n\n")

# split() and join() !

car123 = 'this is a range rover'

thelist= car123.split()
print(thelist) # splits at spaces.
print(car123.split('a')) # splits at the specific charecter.

car321=" ".join(thelist) # joints the lists and strings as well.
print(car321)

# playing with lists !

chess=['queen','king','pawns','bishops','rooks','knights']

del chess[5]
print(chess)
print(len(chess))

chess[len(chess):] = ['knights']
print(chess)

# some lists methods which could be handy !

# using the same list chess .
classroom=['students','teacher','chair']
chess.append('board')
print("\n\n\n")
print(chess)
chess.extend(classroom) # you can do it simply by | newlist = classroom + chess . 
print(chess)
chess.insert(1,'the player') # inserts the element before the specific index.
print(chess)
chess.remove('the player')
print(chess)
chess.pop() # you can specify the index as well.
print(chess)
chess.sort() # in alphabetical order .
print(chess)
chess.reverse()
print(chess)
print(chess.count('king'))

# iterating through the list !

for x in range(len(chess)):
	value = chess[x]
	print(f'{x} : {value}') # printing the index : value | you can do it using enumerate() as well.

print("\n\n")
for x in enumerate(chess) :
	print(x)

# all() , any() , min() ,max(),sum() !

numbers = [2,4,5,9,2,10]
print("\n\n\n")
print(all(numbers)) # checks all are non-zero numbers .
print(any(numbers)) # checks anything is non-zero.
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# no spaces and new line !

print("a","b","c",sep="") # no spaces .
print("a","b","c",end="") # no new line.
print("d",'e','f')

# list inside list | nested list ! 

helloaman = ['1','2',[3,4,5],'6','7','8']
print(helloaman)
print(helloaman[2])

# lists slicing !
print('\n\n')
print(chess[0:])
print(chess[3:5])
print(chess[:5])
print(chess[0::2]) # you can print index values in -1,-2,-? as well.

# list comprehension !

numlist = [12,34,456,672,894]


newlist = [(i+8) for i in numlist if(i%2 == 0)] # does a lot of things in a single line,increments value and then checks even or odd. prints value.

print(newlist)

# lists and the functions !
print("\n\n\n")
vehicle = {"car":"benz","bike":"suzuki","flight":"boeing 747"} # two ways to print a list (1)
books = dict(AT="atomic habits",fiveam="5 am club",tandGR="think and grow rich") # (2)
print(vehicle)
print(books)

del vehicle["car"]
print(vehicle)
print("AT" in books) # only key values work.

books['INTINVSTR'] = "INTELLIGENT INVESTOR" # if it finds a existing value it modifies , if not found it adds one new one.
print(books)

# clear(),get(),pop() for dictionary !

#books.clear()

print(books)

print(vehicle.get("bike","not found"))
print(vehicle.get("boat","not found"))

vehicle.update(books) # if any duplicates found , thet would be eleminated .

print(vehicle)

print(books.pop("fiveam","not book found"))
print(books)

# iteration through a dictionary !

print("\n\n\n")
print(vehicle)
for x in vehicle.values(): #vehicles.values() - for only values, vehicles.items() - for both key and values.
	print(f'{x}')



