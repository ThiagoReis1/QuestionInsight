quantidadea = int(input("Quantidade de votos A:"))
quantidaded = int(input("Quantidade de votos D:"))
total = quantidadea + quantidaded
if(quantidadea>quantidaded):
	print("Ambrosio Rutra")
	a = (quantidadea*100)/total
else:
	print("Demelza Olecram")
	a = (quantidaded*100)/total

print(round(a,2))
	


 
   