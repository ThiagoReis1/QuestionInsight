from numpy import *
it = array(eval(input("hginfgnfinhfnjgjnfgjnfjnbgjfbgj: ")))
i = 0
c = 0
while i < size(it):
	if it[i] > 80:
		it[i] = it[i] * 0.85
	i = i + 1
c= sum(it)
print(round(c ,2 ))