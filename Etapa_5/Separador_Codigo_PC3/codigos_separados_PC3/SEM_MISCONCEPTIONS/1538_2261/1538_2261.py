x = float(input("numero real: "))
n = int(input("numero de termos: "))
i = 2
serie = 1
s = -1
t = 2
while(i<n):
	serie = serie + (- x ** i + x ** (2 * i))
	s = - s 
	i = i + 1
	t = t + 2
resultado = 1 - serie
valor = (1+x**2) * resultado
print(round(valor, 8))
	
	
	
	