alt1 = float(input("Qual sua altura? "))
alt2 = float(input("Qual a altura do seu amigo? "))

#impressao de permissao
if(alt1 > 1.37 or alt2 > 1.37):
	print("Sim")
else:
	print("Nao")
	
#impressao de altura mais alta
if(alt1 > alt2):
	print(alt1)
else:
	print(alt2)