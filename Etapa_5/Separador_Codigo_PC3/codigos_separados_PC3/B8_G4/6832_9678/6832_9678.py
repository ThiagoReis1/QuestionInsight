from numpy import *

x = (input(":"))

qh = 0
qc = 0
ql = 0
t = 0.0
i = 0

while i < len(x):
	if x[i] == 'H':
		qh = qh + 5.40
		t = t + 1
	elif x[i] == 'C':
		qc = qc + 8.95
		t = t + 1
	elif x[i] == 'L':
		ql = ql + 4.50
		t = t + 1
	i = i + 1
T = qh + qc + ql
	
print(round(T,2))
