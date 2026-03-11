tipo=input("C ou E").upper()
quant=int(input("quantidade de coxinha ou salgado"))
quantS=int(input("quantidade de suco"))
if tipo== 'C' :
	conta=(quant*2)+(quantS*6)
	print(conta)
else:
	conta=(quant*4.50)+(quantS*6)
	print(conta)