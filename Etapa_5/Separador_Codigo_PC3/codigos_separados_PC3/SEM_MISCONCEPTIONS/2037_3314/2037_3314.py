idade=int(input("Digite a idade do participante: "))
i = 1
soma=0
while (idade != -1):
	if(idade < 18):
		soma = soma + i
	idade = int(input("Digite a idade do participante: "))
print(soma)
