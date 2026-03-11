tipo = input("Digite B para bolo e S para salgado: ")
quantia = int(input("Digite a quantia de bolos ou salgados: "))
bebida = int(input("Digite a quantidade de cappuccinos: "))

if tipo == "B":
	total = quantia * 5 + bebida * 7.50
else: 
	total = quantia * 4 + bebida * 7.50
	
print(round(total,1))