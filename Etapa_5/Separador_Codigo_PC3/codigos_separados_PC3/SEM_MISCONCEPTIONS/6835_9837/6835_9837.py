def calcular_compra(produtos):
	preco_biscoito = 3.75
	preco_cereal = 7.90
	preco_enlatados = 9.85
	
	valor_total = 0.0
for produtos in produtos:
	if produto == "B":
		valor_total += preco_biscoito
   else produto == "C":
				valor_total+= preco_cereal
				elif produto == "E":
					valor_total += preco_enlatados
					return valor_total
				def main():
					produtos = input("digite uma string:")
					valor_total= calcular_compra(produtos)
					print(round(valortotal, 2))
					
					if __name__ == "__main__"
					main()