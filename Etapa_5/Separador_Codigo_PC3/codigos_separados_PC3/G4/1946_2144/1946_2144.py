a = input("nome do aminoácido:")
a = a.lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.0079

if (a == "fenilalanina"):
	Pm = ((c * 9) + (h * 11) + (o * 2) + s)
	print(round( Pm , 2))
else:
	Pm = ((c * 9) + (h * 11) + n + (o *3))
	print(round( Pm , 2))