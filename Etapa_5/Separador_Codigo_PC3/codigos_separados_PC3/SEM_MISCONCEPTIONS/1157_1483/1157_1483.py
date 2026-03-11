tam = int(input("digite a populacao inicial de tambaquis: "))
taxa = float(input("digite a taxa: "))
retir = int(input("tambaquis retirado ao ano: "))
tempo = 0

while tam > 0:
	tam = tam * (taxa / 100) + tam
	tam = tam - retir
	tempo = tempo + 1
print(tempo)