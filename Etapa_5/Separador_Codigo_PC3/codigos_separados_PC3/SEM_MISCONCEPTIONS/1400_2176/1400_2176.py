ataque = input("Digite o tipo de ataque: ")
num = int(input("Digite o número de rodadas: "))
val1 = int(input("Primeiro valor sorteado: "))
val2 = int(input("Segundo valor sorteado: "))

pontosconst = num*((val1+val2)+1)
pontospolen = val1 * val2

if(ataque == "constricao"):
	print(pontosconst)
else:
	print(pontospolen)