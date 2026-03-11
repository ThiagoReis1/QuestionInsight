idade = int(input("Insira a idade: "))

i = 0

while (idade != -1):
	if (idade < 18):
		i = i + 1
		idade = int(input("Nova idade: "))
		
	else:
		idade = int(input("Nova idade: "))
		
print(i)