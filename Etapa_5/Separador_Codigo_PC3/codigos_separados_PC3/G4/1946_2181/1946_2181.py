aminoacido = input("Digite o nome do aminoacido: ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

if	(aminoacido.lower() == 'fenilalanina'):
	a1 = C * 9
	a2 = H * 11
	a3 = O * 2
	a4 = S * 1
	soma = a1 + a2 + a3 + a4
	print(round(soma, 2))
if	(aminoacido.lower() == 'tirosina'):
	b1 = C * 9
	b2 = H * 11
	b3 = N * 1
	b4 = O * 3
	soma = b1 + b2 + b3 + b4
	print(round(soma, 2))