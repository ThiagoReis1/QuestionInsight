v=float(input("Informe o valor premio: "))
m=float(input("Informe o valor saque mensal: "))
x=float(input("informe a taxa de juros mensal: "))
x=x/100
soma=v
i=0
if (v<=0)or(m<=0)or(x<=0) :
	print("Dados incorretos")
else:
	while(v>=(v+(v*0.20))):
		soma=soma*x
		soma=soma-m
		i=i+1
	print(i)	