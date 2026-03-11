amin = input("Aspartato ou Cisteina?: ")
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
ma = c*4 + h*6 + n*1 + o*4
mc = c*3 + h*7 + n*1 + o*2 + s*1
if (amin.lower() == "aspartato"):
	print(round(ma, 2))
if (amin.lower() == "cisteina"):
	print(round(mc, 2))		