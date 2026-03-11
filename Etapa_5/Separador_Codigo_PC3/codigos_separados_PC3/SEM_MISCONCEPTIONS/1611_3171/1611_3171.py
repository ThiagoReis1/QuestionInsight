stringer = input("Informe a string: ")

soma = 0

i = 0

while(i < len(stringer)):
	if(stringer[i] == "A" or stringer[i] == "E" or stringer[i] == "I" or stringer[i] == "O" or stringer[i] == "U"):
		soma = soma + 0.15
	else:
		soma = soma + 0.17
		
	i = i + 1
		
print(round(soma, 2))