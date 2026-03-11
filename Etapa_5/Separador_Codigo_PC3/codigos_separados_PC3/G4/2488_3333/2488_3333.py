s=float(input("Leia o valor do salario: "))
print("Entrada:","R$",s)
if(0<s and s<=800):
	ns=((s*0.5)+s)
	print("Novo salario:", "R$",round(ns,2))
elif(800<s and s<=1000):
	ns=((s*0.4)+s)
	print("Novo salario:", "R$",round(ns,2))
elif(1000<s and s<=1200):
	ns=((s*0.3)+s)
	print("Novo salario:", "R$",round(ns,2))
elif(1200<s and s<=1400):
	ns=((s*0.2)+s)
	print("Novo salario:", "R$",round(ns,2))
elif(1400<s and s<=1600):
	ns=((s*0.1)+s)
	print("Novo salario:", "R$",round(ns,2))
elif(0<s and 1000<s):
	ns=((s*0.05)+s)
	print("Novo salario: R$",round(ns,2))
else:
	#print("Entrada: R$",s)
	print("Dado invalido")