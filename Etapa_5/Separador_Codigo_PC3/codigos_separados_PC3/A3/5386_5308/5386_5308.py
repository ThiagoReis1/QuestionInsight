senha = input("senha: ").upper()

i = 0

vogal = 0

n_vogal = 0

soma = 0

while  i < len(senha):
	if senha[i] == "A" or senha[i] == "E" or senha[i] == "I" or senha[i] == "O" or senha[i] == "U":
		vogal = vogal + 1.12
		
	else:
		n_vogal = n_vogal + 1.18
		
	soma = vogal + n_vogal
	
	i = i + 1
print(round(soma, 2))