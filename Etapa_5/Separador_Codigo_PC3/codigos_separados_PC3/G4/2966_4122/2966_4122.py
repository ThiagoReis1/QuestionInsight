s=input("Voce e mulher?(S/N)")
v=float(input("Qual valor do ingresso?"))
q=float(input("Quantos ingressos?"))
if(s=="S"):
	total=(v*q)-(((v*q)*20)/100)
else:
	total=v*q
print(round(total,2))