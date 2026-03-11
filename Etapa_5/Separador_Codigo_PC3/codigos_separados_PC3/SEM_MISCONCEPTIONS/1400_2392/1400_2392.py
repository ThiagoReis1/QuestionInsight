#leitura de informaçoes
ataque = input()
rodadas = int(input())
valor1 = int(input())
valor2 = int(input())

#formula de dano
N = valor1 + valor2

#Resoluçao
if(ataque == "constricao"):
	print((N + 1) * rodadas)
else:
	print(valor1 * valor2)
	