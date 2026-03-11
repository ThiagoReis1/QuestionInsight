idade = int(input("Informe sua idade: "))
maior = 0
menor = 0

while(idade != -1):
	if(idade>0):
		if(idade>=18):
			maior = maior + 1
		else:
			menor = menor + 1
	idade = int(input("Informe sua idade: "))

print(menor)