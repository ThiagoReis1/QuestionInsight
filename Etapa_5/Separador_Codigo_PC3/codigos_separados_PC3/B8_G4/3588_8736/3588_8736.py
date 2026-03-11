from numpy import *

v = array(eval(input("QUE TIRO QUE FOI ESSE ? ")))
acm = 10000
i = 0

while size(v) > i :
	if (v[i] == 1):
		acm = acm * 2
	elif (v[i] == 2):
		acm = acm + 0
	elif (v[i] == 3):
		acm = acm/2
	elif (v[i] == 4):
		acm = acm/4
	i = i + 1
print(round(acm,2))