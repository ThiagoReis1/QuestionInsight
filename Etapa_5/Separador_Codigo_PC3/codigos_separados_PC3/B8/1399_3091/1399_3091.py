va = int(input("votos para o candidato Ambrosio Rutra: "))
vb = int(input("votos para a candidata Demelza Olecram: ")) 

#a sua soma da 100% , votos totais
total = (va + vb)
porc1 = va/total * 100
porc2 = vb/total * 100

if(va>vb):
	print("Ambrosio Rutra")
	print(round(porc1, 2))
elif(vb>va):
	print("Demelza Olecram")
	print(round(porc2, 2))
