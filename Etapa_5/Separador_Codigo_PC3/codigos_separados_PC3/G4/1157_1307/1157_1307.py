p = int(input("Digite a populacao inicial: "))
tp = float(input("Digite a taxa de crescimento: "))
n = int(input("Digite o numero de tambaquis tirados anualmente: "))

i = 1

while(p > 0):
	p = (p + p * tp) - n
	i = i + 1
print(i)