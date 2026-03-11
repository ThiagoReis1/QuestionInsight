n = int(input("Informe um numero: "))
p = 0
t = 0

while(n!=0):
	t += 1
	if(n%2==0):
		p += 1
	n = int(input("Informe outro numero: "))
	
r = (p/t) * 100
print(t)
print(round(r,2))



