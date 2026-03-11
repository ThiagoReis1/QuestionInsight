x = input("Informe B para bolo e S para S salgado: ")
qnt = int(input("informe a quantidade de bolos ou salgados: "))
qntcapuccino = int(input("a quantidade de capuccinos: "))

bolo = 5
salgado = 4
capuccino = 7.50

if x == "B":
	v = bolo * qnt  + qntcapuccino * capuccino
	print(round(v ,2))

else:
	v = salgado * qnt + qntcapuccino * capuccino
	print(round(v ,2 ))
	





