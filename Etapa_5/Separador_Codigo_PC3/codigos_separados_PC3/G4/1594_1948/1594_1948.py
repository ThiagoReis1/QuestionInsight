from numpy import*

vd= array(eval(input("Vetor de danos: ")))
i = 1
h = 0
while i <= size(vd) + 1:
	h = h + (vd[i] * i)
	print(h)
	