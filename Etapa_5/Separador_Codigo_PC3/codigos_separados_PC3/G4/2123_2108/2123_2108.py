from numpy import*
v = array(eval(input("Diga as notas:")))
a = min(v)
b = sum(v)
mf = (b - a)/3
if(mf >= 5.0):
	print(round(mf,2))
	print("APROVOU")
else:
	print(round(mf,2))
	print("REPROVOU")