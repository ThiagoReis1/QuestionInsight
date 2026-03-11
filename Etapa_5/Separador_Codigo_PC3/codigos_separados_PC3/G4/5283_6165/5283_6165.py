n = int(input(""))

soma = 0
i = 0
j = 0
while(n != 0):
	if(n > 0):
		i = i+1
		soma = soma +1
	else:
		j = j+1
	n = int(input(""))
s = i + j 
p1 = (i/s)*100
#n = int(input(""))
print(s)
print(round(p1,2))
