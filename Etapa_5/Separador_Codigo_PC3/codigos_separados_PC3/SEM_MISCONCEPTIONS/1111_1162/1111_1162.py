a = float(input("qual o numero de horas extras:"))
b = float(input("qual o numero de horas faltadas:"))
h = round((a - (2/3 * b)), 2)
print("Entrada:", str(a), "horas extras e", str(b), "horas de falta")
elif(h > 2400):
	print("gratificacao: R$", 500.0)
elif(1800 < h <= 2400):
	print("Gratificacao: R$", 400.0)
elif(1200 < h <= 1800):
	print("Gratificacao: R$", 300.0)
elif(600 < h <= 1200):
	print("Gratificacao: R$", 200.0)
elif(h < 600):
	print("Gratificacao: R$", 100.0)
else:
	print("dados invalidos")