opcao=input("Lanche ou salgado? (L/S)")
quant1=float(input("Digite um numero: "))
quant2=float(input("Digite um numero: "))
L=5.00
S=3.50
R=4.00
if (opcao=="L"):
	msg=quant1*L+quant2*R
else:
	msg=quant1*S+quant2*R
print(round(msg, 2))