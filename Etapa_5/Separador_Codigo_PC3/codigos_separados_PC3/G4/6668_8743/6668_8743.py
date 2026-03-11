from numpy import *
m = array(eval(input("Digite : ")))
s = 0
q = 0
for i in range(size(m)):
	if (m[i] > 170):
		s = s + m[i]
		q = q + 1
if (q == 0):
	print("0.0")
else:
	me = s/q
	print(round(me,2))

		