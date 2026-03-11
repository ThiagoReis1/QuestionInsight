nom = input("")
c = 12.011
o = 15.9994
n = 14.0067
h = 1.0079
s = 32.066

F = c*9 + h*11 + o*2 + s*1
T = c*9 + h*11 + n*1 + o*3

if (nom == "fenilalanina"):
	print(round(F, 2))
else:
	print(round(T, 2))