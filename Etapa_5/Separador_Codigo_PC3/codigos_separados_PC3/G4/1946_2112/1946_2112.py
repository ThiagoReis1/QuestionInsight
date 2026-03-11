nome = input()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

resultado = (9*C)+(11*H)+(2*O)+ S 
resultado2 = (9*C)+(11*H)+ N +(3*O)


if(nome == "fenilalanina".lower()):
	print(round(resultado,2))
else:
	print(round(resultado2,2))

