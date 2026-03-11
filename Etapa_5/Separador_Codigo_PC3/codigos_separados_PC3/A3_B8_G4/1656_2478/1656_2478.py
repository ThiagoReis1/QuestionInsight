from numpy import *
s = input("Informe os paises: ").split(',')
a = size(s)
x = zeros(5, dtype=int)
be = 0
es = 0
fr = 0
it = 0
pt = 0
for i in range(a):
	if(s[i] == "BE"):
		x[0] += 1
	elif(s[i] == "ES"):
		x[1] += 1
	elif(s[i] == "FR"):
		x[2] += 1
	elif(s[i] == "IT"):
		x[3] += 1
	elif(s[i] == "PT"):
		x[4] += 1
print(max(x))
print(x)
