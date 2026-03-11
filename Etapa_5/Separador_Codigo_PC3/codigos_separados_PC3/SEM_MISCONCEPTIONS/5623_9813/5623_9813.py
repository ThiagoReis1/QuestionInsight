tipo = str(input("Entre com o Bolo(B) ou Salgado(S): "))
qtdbs= int(input())
qtdcap = int(input())

bolo = 5.0
salgado = 4.0
cap = 7.5
if tipo == ("B"):
	total = (qtdcap * cap) + (qtdbs * bolo)
	print(round(total,2))
else:
	total = (qtdcap * cap) + (qtdbs * salgado)
	print(round(total,2))