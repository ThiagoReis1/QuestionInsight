val = int(input("Valor do dado: "))
qtd = 0

while(val!=-1):
	if(val == 6):
		qtd = qtd+1
	val = int(input("Valor do dado: "))

print(qtd)