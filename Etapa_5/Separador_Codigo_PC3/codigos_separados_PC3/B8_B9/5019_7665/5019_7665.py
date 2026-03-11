salario = float(input())

if(salario <1212.00):
	print(round(salario + salario*12.0/100.0,2))
elif(salario>5000.0):
	print(round(salario + salario*3.0/100.0,2))
elif(salario>=1200.0 and salario<=5000.0):
	print(round(salario + salario*8.0/100.0,2))