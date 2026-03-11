from numpy import*
n = array(eval(input("pora")))
i = 0
while i < len(n):
	if n[i] == 3:
		n[i]= 0
		i+=1
	else:
		n[i]=n[i]
print(n)

