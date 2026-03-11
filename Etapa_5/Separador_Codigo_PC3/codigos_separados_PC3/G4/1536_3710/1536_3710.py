x = float(input("Insira o numero real: "))
k = int(input("Insira a quantidade de  termos da serie: "))

cont = 0
a = 0

while(cont < k):
		if(-1 < x <= 1):
			a = a + ((-1)**(cont + 1)) * ((x ** (cont + 1)) / (cont + 1))
			c = a * (-1)
			cont += 1
print(round(c,10))