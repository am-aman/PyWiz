# find S algorithm :) 
import csv 

attribute = 6
a = []

with open('book1.csv','r') as r :
	dataset = csv.reader(r)
	for row in dataset:
		a.append(row)
		#print(row)
a[0][0] = "sunny"
#print(a)

hypothesis = ['X']*attribute

for j in range(0,attribute):
	hypothesis[j]=a[0][j]
print(hypothesis)

for i in range(0,len(a)):
	if a[i][attribute]=="yes":
		for j in range(0,attribute):
			if a[i][j]!=hypothesis[j]:
				hypothesis[j]="?"
			else:
				hypothesis[j]=a[i][j]

	print(f"Iteration number {i} the hypothesis is : ",hypothesis)

print(hypothesis)

