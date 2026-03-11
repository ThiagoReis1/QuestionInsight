num1 = int(input("Digite o numero de habitantes em bravo: "))
num2 = int(input("Digite o numero de habitantes em pentos: "))
num3 = int(input("Digite o numero de habitantes em porto real: "))
taxa1 = float(input("Digite a taxa de crescimento de habitantes em bravos: "))
taxa2 = float(input("Digite a taxa de crescimento de habitantes em pentos: "))
taxa3 = float(input("Digite a taxa de crescimento de habitantes em porto real: "))
i1 = taxa1/100
i2 = taxa2/100
i3 = taxa3/100
x = 1
while (num1 + num2 <= num3):
	num1 = num1 + (num1 * i1)
	num2 = num2 + (num2 * i2)
	num3 = num3 + (num3 * i3)
	x = x + 1
print (x) 