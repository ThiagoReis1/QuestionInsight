aminoacido = input("qual o nome do aminoacido?")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.0079

if (aminoacido == "fenilalanina"):
	print (round ((c * 9) + (h * 11) + (o * 2) + s , 2))
else:
	print (round ((c * 9) + (h * 11) + ( o * 3) + n ,2))
	


