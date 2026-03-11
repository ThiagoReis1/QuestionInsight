ataque = input("Tipo de ataque: ").lower()
d1 = int(input("Resultado do dado 1: "))
d2 = int(input("Resultado do dado 2: "))
d3 = int(input("Resultado do dado 3: "))
d4 = int(input("Resultado do dado 4: "))
di = d1 + d2 + d3 +d4

espada = di+6
cauda = (d1 + d2 + d3) * d4
if(ataque == "espada"):
		mensagem = espada
else:
	mensagem = cauda
	
print(mensagem)