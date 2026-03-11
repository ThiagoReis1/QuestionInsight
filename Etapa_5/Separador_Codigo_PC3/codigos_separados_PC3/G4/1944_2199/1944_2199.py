NA = input("Nome aminoacido:").lower()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

leucina = 6*C + 13*H + N + 2*O
lisina = 6*C + 15*H + 2*N + 2*O

if(NA == "leucina"):
	soma = leucina
else:
	soma = lisina

print(round(soma,2))
			  