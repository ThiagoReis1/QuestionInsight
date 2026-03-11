valor = float(input("valor investido: "))
mes = int(input("tempo de investimento: "))

tempo = 0

while(tempo < mes): 
	lucro = valor * 0.01
	valor = valor + lucro 
	tempo = tempo + 1 
print(round(valor,2))




	