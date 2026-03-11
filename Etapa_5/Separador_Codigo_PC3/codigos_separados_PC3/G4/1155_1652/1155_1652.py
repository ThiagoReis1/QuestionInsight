num1 = int(input("Digite o numero de leu:"))
num2 = int(input("Digite o numero de vi:"))
taxa1 = float(input("Digite a taxa de crescimento de leu:"))
taxa2 = float(input("Digite a taxa de crescimento de vi"))
i1 = taxa1/100
i2 = taxa2/100
i = 1
while (num1 >= 2*num2):
	num1 = num1 + (num1*i1)
	num2 = num2 + (num2*i2)
	i = i + 1
print (i)