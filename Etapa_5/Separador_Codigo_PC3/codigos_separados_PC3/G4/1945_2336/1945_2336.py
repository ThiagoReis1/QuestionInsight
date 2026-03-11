Nome = input("Digite o nome do Aminoacido: ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if (Nome.lower() == 'aspartato'):
	conta1 = (C*4 + H*6 + N + O*4)
	print(round(conta1,2))
if (Nome.lower() == 'cisteina'):
	conta2 = (C*3 + H*7+ N + O*2 +S)
	print(round(conta2,2))