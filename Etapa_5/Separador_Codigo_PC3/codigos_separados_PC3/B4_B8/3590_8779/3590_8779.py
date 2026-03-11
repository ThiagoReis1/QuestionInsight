from numpy import*
n=array(eval(input()))

i=0

total=0
while i<size(n):
	if n[i]==1:
		total+=10

	elif n[i]==2:
	
		total+=5
		
	elif n[i]==4:
		
		total+=5
	elif n[i]==5:
		total+=20
	elif n[i]==6:
		total+=10
	i+=1
print(round(total, 2))