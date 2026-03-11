s=input("Molier: (S/N)")
v=float(input("Digite o valor do ingresso: "))
q=int(input("Digite a quantidade de ingressos: "))
var=v*q
if(s=="S"):
	var2=var-(0.2*var)
	print(round(var2,2))
else:
	print(round(var,2))