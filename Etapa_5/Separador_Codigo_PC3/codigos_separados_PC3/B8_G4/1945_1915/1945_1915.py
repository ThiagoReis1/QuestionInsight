amin = input("")
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if (amin.lower() == "aspartato"):
	peso = 4*c + 6*h + n + 4*o
	print(round(peso,2))
elif (amin.lower() == "cisteina"):
	peso = 3*c + 7*h + n + 2*o + s
	print(round(peso,2))
	