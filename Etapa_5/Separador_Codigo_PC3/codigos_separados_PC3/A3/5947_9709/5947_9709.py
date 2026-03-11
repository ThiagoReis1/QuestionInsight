nome = str(input("Digite C ou E: "))
quant = int(input("Digite a quantidade de C ou E: "))
suco = int(input("Digite a quantidade de suco: "))

if(nome.upper()=="C"):
	total = (quant * 2.00) + (suco * 6.00)
	
if(nome.upper()=="E"):
	total = (quant * 4.50) + (suco * 6.00)
print(total)
