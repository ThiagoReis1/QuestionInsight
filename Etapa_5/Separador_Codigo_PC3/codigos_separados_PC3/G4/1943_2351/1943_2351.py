nome_aminoacido= input()

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if (nome_aminoacido == "isoleucina"):
	iso = ((6*c) + (13*h) + n + (2*o))
	print(round(iso,2))
	
else:
	metio = ((5*c) + (11*h) + n + (2*o) + s)
	print(round(metio,2))