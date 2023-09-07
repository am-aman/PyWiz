'''
what is list comprehension ?

instead of writting several nested loopsand if
statements,we use list comprehension(single line of code).


example : to take a nested list 
and print all the values in the console.

normal method :

'''
s = [[1,2],[3,4],[5,6]]
s1 = []

for x in s :
	for y in x:
		#print(y,end="")
		s1.append(y)
print(s1)

# output : [1, 2, 3, 4, 5, 6]
# output with 5 lines code



# list comprehension method:

y = [y for x in s for y in x]

print(y)

# output : [1, 2, 3, 4, 5, 6] 
#(same output with 2 line of code )



