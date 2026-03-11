from numpy import*
x = array(eval(input("")))
m = sum(x) - max(x)
mf = m / 3
print(round(mf, 2))
if mf >= 5:
	msg = "APROVOU"
	print(msg)
else:
	msg = "REPROVOU"
	print(msg)