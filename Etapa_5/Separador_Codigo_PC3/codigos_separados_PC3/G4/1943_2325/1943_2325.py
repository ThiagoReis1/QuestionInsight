"""
UNIVERSIDADE FEDERAL DO AMAZONAS
DISCENTE: DAVE MONTEIRO BONATES  MAT: 21601485
TURMA: ENG. DE PRODUÇÃO
"""
na = input("Nome do aminoácido: ")
na = na.lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if na == "isoleucina":
	R = C*6 + H*13 + N*1 + O*2
	print(round(R,2))
else:
	R = C*5 + H*11 + N*1 + O*2 + S*1
	print(round(R,2))
