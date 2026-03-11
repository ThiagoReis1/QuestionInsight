n = int(input())
a = 1
b = 1
c = -1
cont = 0
sd = 0
while(n > cont):
	sd = sd + ((c*(a**2))/(7+b))
	cont = cont + 1
	a = a + 1
	b = b + 2
	c = c*(-1)
	
print(round(sd, 11))