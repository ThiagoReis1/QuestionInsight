a = float(input("Horas extras: "))
b = float(input("Horas que o fun faltou:"))

print("Entradas:", a,"horas extras e", b, "horas de falta")
H = a-2/3*b

if(a<0) or (b<0):
	print("Dados invalidos")
elif(H>=2400):
	print("Gratificacao: R$", 500.00)
elif(H>=1800) and (H<2400):
	print("Gratificacao: R$", 400.00)
elif(H>=1200) and (H<1800):
	print("Gratificacao: R$", 300.00)
elif(H>=600) and (H<1200):
	print("Gratificacao: R$", 200.00)
elif(H<=600):
	print("Gratificacao: R$", 100.0)
