# faça seu código aqui!

a = int(input("Informe a quantidade de dias: "))

if a < 15: 
	total = a * 175 + 20
elif a == 15:
	total = a * 175 + 16
else:
	total = a * 175 + 10
print(round(total, 2))