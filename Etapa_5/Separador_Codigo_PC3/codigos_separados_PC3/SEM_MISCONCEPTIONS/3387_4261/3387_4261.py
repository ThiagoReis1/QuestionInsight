unidade = input("qual as unidade? KouM: ")
medida = float(input("qual a medida?: "))
if(unidade == "K"):
	mensagem=(2.35215*medida)
else:
	mensagem=(medida/2.35215)
print(round(mensagem,2))	