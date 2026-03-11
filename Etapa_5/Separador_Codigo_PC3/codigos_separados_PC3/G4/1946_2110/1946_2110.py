aminoacido = input()

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.0079

if(aminoacido == "fenilalanina"):
	f1 = c*9 + h*11 + o*2 + s
	print(round(f1,2))
else:
	f2 = c*9 + h*11 + n + o*3
	print(round(f2,2))