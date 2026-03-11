# faça seu código aqui!
tipo = input()
quantidade = int(input())


promocao = 25.90 - (10/100)
total = quantidade*25.90

if tipo.upper() == "B":
   print(round(promocao,2))
else:
	print(total)