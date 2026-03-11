Vm = float(input("Digite o valor da mensalidade: "))
Nc = int(input("Digite o numero de criancas: "))


if(Nc == 1):
	d = 0.1
	vt = (Vm*Nc)-d*(Vm*Nc)
	print(round(vt,2))
elif(Nc == 2):
	d = 0.3
	vt = (Vm*Nc) - d*(Vm*Nc)
	print(round(vt,2))
else:
	d = 0.4
	vt = (Vm*Nc)-d*(Vm*Nc)
	print(round(vt,2))