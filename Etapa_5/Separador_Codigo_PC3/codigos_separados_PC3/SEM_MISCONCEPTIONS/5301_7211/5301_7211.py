valor = int(input("valor: "))
t = 0 
while(valor >= 40):
	t = t + 1 
	valor = valor - (valor*2/100)
print(t)