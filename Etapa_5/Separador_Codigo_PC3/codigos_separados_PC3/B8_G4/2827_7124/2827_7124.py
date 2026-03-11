from numpy import*

n= array(eval(input("notas:")))
i= 0

while i< size(n):
	if n[i]>4 and n[i]<5:
		n[i]=4
	elif n[i]>9:
		n[i]=10
	i= i+1
print (n)