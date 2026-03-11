v = float(input("Valor recebido da indenizacao: "))
c = float(input("Saque mensal fixo: "))
j = float(input("A taxa de juros: "))
vm = (v * j) / 100
v = vm + v
vfm = v - c
v2 = v / 2
cont = 0
if(v>0) and (c>0) and (j>0):
	while(vfm >= v2):
		vm = (v * j) / 100
		v = vm + v
		vfm = v - c
		v2 = v / 2
		cont = cont + 1
	print(cont)
		
else:
	print("Dados incorretos")