salario = float(input())

if salario < 1212:
	total = salario + (salario * 0.12)
	
elif salario >= 1212 and salario <= 5000:
	total = salario + (salario * 0.08)
	
elif salario > 5000:
	total = salario + (salario * 0.03)

print(round(total,2))