x= int(input('inserir numeros:'))
c=0

while (x!=-1):
	if ((x>=26) and (x<=85)):
		c += 1
	x= int(input("inserir numeros:"))
print(c)