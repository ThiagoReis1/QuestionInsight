from numpy import *
v = array(eval(input("Vetor registro: ")))
al = 0
ilim = v[0] + (v[0] * (20/100))
flim = v[0] + (v[0] * (50/100))
for i in range(size(v)):
	if (v[i] > ilim) and (v[i] < flim):
		al = al + 1
		print(i)
print(al)