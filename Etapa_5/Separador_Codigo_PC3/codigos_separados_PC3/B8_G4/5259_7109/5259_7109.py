vm = float(input("Valor da mensalidade: "))
nc = int(input("Numero de criancas da familia: "))
c1 = (vm-(vm*0.1))
c2 = (vm-(vm*0.3))*2
c3 = (vm-(vm*0.4))*3
if nc == 1:
	print(round(c1,2))
elif nc == 2:
	print(round(c2,2))
elif nc >=3:
	print(round(c3,2))
	