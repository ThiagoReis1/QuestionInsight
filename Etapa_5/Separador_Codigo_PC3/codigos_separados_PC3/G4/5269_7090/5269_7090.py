num = int(input("Valor: "))
aux1 = 0
aux2 = 0

while(num!=0):
	aux1 = aux1 + 1.0
	if(num%3==0):
		aux2 = aux2 +1.0
	num = int(input("Valor: "))
	
print(int(aux1))
tot = aux2 / aux1
print(round(tot*100,2))