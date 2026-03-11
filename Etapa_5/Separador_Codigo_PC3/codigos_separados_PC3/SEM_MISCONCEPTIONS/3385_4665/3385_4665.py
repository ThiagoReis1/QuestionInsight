unidade = input("Qual a unidade?")
valor = float(input("Qual o valor?"))
acre = valor/2.47105
ha = valor*2.47105
if(unidade.upper()=="A" ):
	mensagem = acre
	print(round(mensagem,2))
else:
	mensagem = ha
	print(round(mensagem,2))
