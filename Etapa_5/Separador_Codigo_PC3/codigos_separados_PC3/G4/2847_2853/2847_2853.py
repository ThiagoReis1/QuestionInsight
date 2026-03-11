from numpy import *

msgm = array(eval(input("Leia valor: ")))

v = zeros(size(msgm), dtype=int)

for i in range(0, size(msgm)):
	v[i] = msgm[i] ** 2
print(v)