from numpy import*

n= array(eval(input("")))
i= 0

while i < size(n):
	if n[i] >= 9:
		n[i]= 10
	elif n[i] == 10:
		n[i] = n[i]+ 0
	elif n[i] > 4 and n[i] < 5:
		n[i] = 4
	i= i + 1
print(n)