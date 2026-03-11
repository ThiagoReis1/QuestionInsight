##Desconto na mensalidade

men = float(input("Mensalidade em R$ "))
cri = int(input("Quantidade de criancas "))

##Condicao

if (cri == 1):
	c = men*0.1
	calculo = men - c
	total= (calculo*cri)
elif (cri == 2):
	c = men*0.3
	calculo = men - c
	total = (calculo*cri)
else:
	c = men*0.4
	calculo = men - c
	total = (calculo*cri)
	
print(round(total,2))