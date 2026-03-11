from numpy import *
N = array(eval(input(": ")))

mf = (N[0] + N[1] + N[2] + N[3] - max(N)) / 3

print(round(mf,2))
if(mf >= 5):
	print("APROVOU")
else:
	print("REPROVOU")
