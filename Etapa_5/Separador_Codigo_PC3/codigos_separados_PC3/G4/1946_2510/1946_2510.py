nome = input("Nome do Aminoácido: ")
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.0079

if (nome == "fenilalanina"):
	x = 9 * c + 11 * h + 2 * o + s
	print(round(x, 2))
else :
	x = 9 * c + 11 * h + 3 * o + n
	print(round(x,2))
