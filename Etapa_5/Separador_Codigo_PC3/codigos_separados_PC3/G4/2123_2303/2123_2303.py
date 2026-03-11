from numpy import*
x = array(eval(input("vetor: ")))
m = sum(x) - min(x)
mf = m/3
print(round(mf, 2))
if mf >= 5:
	print("APROVOU")
else:
	print("REPROVOU")