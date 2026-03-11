from numpy import *

v = array(eval(input('pontos:')))
x = 100
S = 0

for i in range(size(v)):
	if v[i] == 2:
		s = x * 2
		
	elif v[i] == 3:
		s = (x/3)
		
	elif v[i] == 4:
		s = x * 4
		
	elif v[i] == 5:
		s = x/5
		
	elif v[i] == 6:
		s = x * 6
		
print(round(s,2))
		
		