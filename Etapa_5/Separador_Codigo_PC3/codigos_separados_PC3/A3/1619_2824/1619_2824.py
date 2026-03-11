from numpy import*
tempo = array(eval(input("")))
modo = array(eval(input("")))
n = 0
preco1 = 0
preco3 = 0
valor = size(tempo)
while(n < valor):
	if(modo[n]== "QUENTE"):
		preco = 90*0.005*(tempo[n])
		preco1= preco + preco1
	elif(modo[n]== "MORNO"):
		preco2 = 45 * 0.005*(tempo[n])
		preco3 = preco2 + preco3
	else:
		preco4 = 0
	n = n + 1 
total = round(preco1 + preco2, 2)
print(total)
	
