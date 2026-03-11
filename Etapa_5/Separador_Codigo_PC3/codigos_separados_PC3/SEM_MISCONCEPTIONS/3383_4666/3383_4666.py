unid_medida = input("qual a medida?")
valor = float(input("qual o valor?"))
Lb = valor/2.20462
Kg = valor*2.20462
if(unid_medida.upper()=="L" ):
	mensagem = Lb
	print(round(mensagem,2))
else: 
	mensagem = Kg
	print(round(mensagem,2))
