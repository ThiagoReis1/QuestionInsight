from numpy import *

nota = array(eval(input(": ")))

mf =(nota[0] + nota[1] + nota[2] + nota[3] - max(nota))/ 3.0
print(round(mf,2))
if (mf>=5):
	print("APROVOU")
else:
		print("REPROVOU")
