cabeca = input()
e1 = int(input())
e2 = int(input())
saida = "Entrada invalida"

if( e1>0 and e2>0 and e1<11 and e2 < 11):
	if(cabeca == "AAMEUL"):
		saida = 8+e1+e2
	elif(cabeca == "HETHRADIAH"):
		saida = 2*(e1+e2)
	elif(cabeca == "RAKSHASA"):
		saida = 10+(e1+e2)

print(saida)
	
	