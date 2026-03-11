## $Curumim Acai$

T = 5.50
S = 4.00
A = 10.0

pedido = input("Voce vai querer tapioca ou salgados?").upper()
ts = int(input("Qual a quantidade de tapiocas ou salgados?"))
acai = int(input("Qual a quantidade de acai?"))

##Condicao 

if (pedido == "S"):
	s = (ts*S) + (acai*A)
else:
	s = (ts*T) + (acai*A)

print(s)