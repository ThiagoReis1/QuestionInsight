from numpy import*
from numpy.linalg import*
from math import*

qi = int(input("Quantidade de Infantaria:"))
qc = int(input("Quantidade de Cavalaria:"))
qp = int(input("Percentual de Infantaria:"))
qpi = int(input("Percentual de Cavalaria:"))

lot = float(qp/100)
put = float(qpi/100)
t = qi + qc
n = 0
m=0
o=0
while (t < 50000):
	m = m + (qi*lot) 
	o = o + (qc*put)
	t = m + o
	n = n + 1
print(n)