A_r = int(input("A_r: "))
D_o = int(input("D_o: "))

total_votos = A_r + D_o

porcentagem1 = 600000 * 100
total_porcentagem = porcentagem1 / total_votos



if(A_r > D_o):
	mensagem = "Ambrosio Rutra"
else:
	mensagem = "Demelza Olecram"
print(mensagem)
print(round(total_porcentagem, 2))