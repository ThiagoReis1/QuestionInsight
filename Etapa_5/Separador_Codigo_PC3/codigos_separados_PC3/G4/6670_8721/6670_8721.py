from numpy import *
n = array(eval(input("Digite os precos: ")))
s = 0
q = 0

for x in range(size(n)):
	if n[x] > 20:
		s = s + n[x]
		q = q + 1
if q > 0:
	print(round((sum(s)/q),2))
else:
	print(0.0)