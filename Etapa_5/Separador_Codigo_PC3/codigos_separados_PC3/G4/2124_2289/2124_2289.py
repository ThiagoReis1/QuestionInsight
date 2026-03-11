from numpy import *
v = array(eval(input()))

m = sum(v) - max(v)

mf = m / 3

if mf >= 5:
	print(round(mf, 2))
	msg = "aprovou".upper()
	print(msg)
else:
	print(round(mf, 2))
	msg = "reprovou".upper()
	print(msg)