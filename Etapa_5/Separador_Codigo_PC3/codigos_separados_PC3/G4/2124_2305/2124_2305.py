from numpy import*

v = array(eval(input()))
m = sum(v)-max(v)

mf = m / 3

print (round(mf,2))
if mf >= 5:
	print ("APROVOU")
else:
	print("REPROVOU")
	