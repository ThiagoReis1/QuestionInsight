string = input("Digite a quant de letras C:").upper()
i = 0
total = 0
C = 0
while i < len(string):
	if string[i] == "C":
		C = C + 1
		total =total + 1
	i = i + 1
	
print(C)
		