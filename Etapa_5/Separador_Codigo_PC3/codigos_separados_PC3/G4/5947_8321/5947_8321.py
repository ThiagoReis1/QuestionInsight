escolha = input("C OU E?: ")
n = int(input("quantidade?: "))
S = int(input("quantos sucos?: "))

if (escolha == "C"):
	x = 2*n + 6*S
else:
	x = 4.50*n + 6*S
print(x)
	