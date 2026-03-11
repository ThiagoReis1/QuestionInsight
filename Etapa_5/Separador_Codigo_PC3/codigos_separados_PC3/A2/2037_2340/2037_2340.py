idade = int(input("Digite a Idade: "))

qtd = 0 #quantidade de menores

if(idade <18):
	while(idade != -1):
		qtd = qtd + 1
		idade = int(input())
else:
	qtd = qtd
print(qtd)