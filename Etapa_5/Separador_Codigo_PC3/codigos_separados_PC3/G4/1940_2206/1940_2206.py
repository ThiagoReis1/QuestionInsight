a = input("nome do aminoacido: ")
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
g = c * 5 + h * 8 + n * 1 + o * 4
t = c * 4 + h * 9 + n + o * 3

if(a == "GLUTAMINA"):
	print(round(g, 2))
else:
	print(round(t, 2))