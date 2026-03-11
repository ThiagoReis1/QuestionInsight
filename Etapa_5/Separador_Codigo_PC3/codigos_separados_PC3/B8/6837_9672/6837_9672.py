secao= input("Insira a inicial da secao que voce pegou o item: ") .upper()

i= 0 
valor= 0 

while (i < len(secao)):
	if secao[i] == "I":
		valor= valor + 3.75
	elif secao[i] == "M":
		valor= valor + 4.50
	elif secao[i] == "S":
		valor= valor + 2.90
		
	i= i + 1
	
print(round(valor,2))