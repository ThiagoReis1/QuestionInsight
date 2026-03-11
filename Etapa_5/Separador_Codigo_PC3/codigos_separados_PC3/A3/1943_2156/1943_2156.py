molecula_1 = "Isoleucina"

molecula_2 = "Metionina"

aminoacido = input("Nome da molecula".lower())

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if (aminoacido == "Isoleucina"):
	soma = ((C * 6) + (H * 13) + N + (O * 2))
	
	print(round(soma, 2))
			
else:
		soma = ((C * 5) + (H * 11) + N + (O * 2) + S)
		print(round(soma, 2))