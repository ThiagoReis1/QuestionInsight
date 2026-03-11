x=float(input())
y=float(input())
h= x-(2/3)*y
print("Entradas:",x, "horas extras e",y,"horas de falta")
if(x>0 and y>0):
	if(h<=600):
		print("Gratificacao: R$ 100.0")
	elif(h>600 and h<=1200):
		print("Gratificacao: R$ 200.0")
	elif(h>1200 and h<=1800):
		print("Gratificacao: R$ 300.0")
	elif(h>1800 and h<=2400):
		print("Gratificacao: R$ R$400.0")
	else:
		print("Gratificacao: R$ 500.0")
else:
	print("Dados invalidos")