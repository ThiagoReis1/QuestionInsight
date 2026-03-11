idade = int(input("idade: "))

soma = 0


while idade != -1:
	if idade < 18:
		soma = soma + 1
		idade = int(input("idade: "))
	else:
		idade = int(input("idade: "))
		
print(soma)