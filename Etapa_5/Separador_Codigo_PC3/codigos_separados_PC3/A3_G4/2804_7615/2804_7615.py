d= float(input("digite deposito inicial:"))
q= int(input("digite numero de meses:"))
c= 0
a= 0

while (d < 0):
	c= c + 1
	j= d * 0.01
	a= a + 1

print(round(a,2))