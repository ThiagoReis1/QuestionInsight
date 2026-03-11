cand_1 = int(input())
cand_2 = int(input())
cand_3 = int(input())
brancos = int(input())
nulos = int(input())
votos_validos1 = cand_3 + cand_2 + cand_1

if(cand_1 > (votos_validos1)/2):
	mensagem = "NAO"
	print(mensagem.upper())
else:
	mensagem = "SIM"
	print(mensagem.upper())