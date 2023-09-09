# To find how many times the sub string is present in the main string !

x = "ABCDCDC"

y = "CDC"

ms = len(x)

ss = len(y)

count = 0

for a in range(ms-ss+1):
	if (x[a:a+ss]) == y:
		
		count+=1


print(count)
