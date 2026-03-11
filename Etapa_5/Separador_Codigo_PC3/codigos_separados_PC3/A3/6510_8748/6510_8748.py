# faça seu código aqui!
dia = input("qual dia da semana: ")
quantidade = float(input("quantidade de pratos consumidas: "))

prato = 22
pratoqvaicomer = 22 * quantidade
descontoQUA = pratoqvaicomer - (0.15 * pratoqvaicomer) 
prato_normal = quantidade * 22

if dia == "qua":
	print(descontoQUA)
	
else: 
	print(prato_normal)