#Wagner William Amorim - 21552149
#Terceira avaliação
#Questão 1
#14/07/2016

preco = float(input("Informe o valor da entrada: "))
dia = int(input("Informe o dia da semana: "))
musica = str(input("Dia de musica ao vivo ? "))
S = str
N = str

if (preco >= 0.0):
	if(musica == S):
		valor = preco + 20.00
	else:
		valor = preco
	if(dia == 2 or dia == 3 or dia == 5):
		valor = preco * 0.25
		print(round(valor, 2))
	else:
		valor = preco
		print(valor)

else:
	print("Entradas:", preco , dia, musica)
	print("Dados invalidos")
	
	

