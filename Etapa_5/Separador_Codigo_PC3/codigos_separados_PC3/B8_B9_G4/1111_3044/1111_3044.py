x=float(input("horas extras: "))
y=float(input("horas faltas: "))
h=x-(2/3)*y
print("Entradas: ",x,"horas extras e ",y,"horas de falta")
if(x<0 or y<0):
	print("Dados invalidos")
else:
	if(h>2400):
		g=500.0
		print("Gratificacao: R$",round(g,2))
	elif(h>1800 and h<=2400):
		g=400.0
		print("Gratificacao: R$",round(g,2))
	elif(h>1200 and h<=1800):
		g=300.0
		print("Gratificacao: R$",round(g,2))
	elif(h>600 and h<=1200):
		g=200.0
		print("Gratificacao: R$",round(g,2))
	elif(h<=600):
		g=100.0
		print("Gratificacao: R$",round(g,2))