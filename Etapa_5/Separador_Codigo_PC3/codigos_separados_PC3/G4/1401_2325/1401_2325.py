"""
UNIVERSIDADE FEDERAL DO AMAZONAS
DISCENTE: DAVE MONTEIRO BONATES  MAT: 21601485
TURMA: ENG. DE PRODUÇÃO
"""
at = input("Tipo do ataque: ")
qb = int(input("Quantidade de baforadas: "))

if at == "maritimo":
	D = "Viserion"
	R = qb * 40 
	print(D)
	print(R)
else:
	D = "Drogon"
	R = qb * 150
	print(D)
	print(R)