'''
ENUMERATE () :

lets say that you need a output just like this 

output:

1 : hello
2 : mam
3 : how
4 : are
5 : you

more common way is, this one down here 

'''

# 5 lines of code :

the_list = ['hello','mam','how','are','you']
counter  = 1
for x in the_list:
    
    print(f'{counter} : {x}')
    counter+=1

'''
what if i tell you its easy and takes less lines that the common approach 
'''

# 3 lines of code :
for x,y in enumerate(the_list):
    print(f'{x+1} : {y}')

'''
no counter variable and increment

the x in print has a "+1" because the enumerate() starts with zero !

'''
'''
ZIP():

lets say you need a output like this
OUTPUT:
ashif : aman
al : mohamed 
riyaz : rahmaan
luqmaan : ali

more common way to do this 
'''

list_one = ['ashif','al','riyaz','luqmaan']
list_two = ['aman','mohamed','rahmaan','ali']

for x in range(len(list_one)):
    print(f'{list_one[x]} : {list_two[x]}')
#this works fine only if the len of the lists are same. 
# len is different = list out of index error :(

#instead try this 

for x,y in zip(list_one,list_two):
    print(f'{x} : {y}')
# this works fine even the list has different length. 
# prints output untill one of the lists is out of values.and donot show error :)
