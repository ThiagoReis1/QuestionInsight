x = float(input("Numero real: "))
k = int(input("Quantidade de termos: "))

s = 1 #Parte Superior
v = 2 #Parte Inferior
a = 0 #Soma
cont = 0

while (cont < k):
	a = a + s/(v*x)
	cont = cont + 1
	s = s + 1
	v = v + 2	

print(round(a,10))
	
	
	