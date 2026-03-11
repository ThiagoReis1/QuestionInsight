from numpy import*
vt = array(eval(input("Insira o vetor com o tempo de chegada dos corredores:")))
me = max(vt)
c = size(vt)
t = 0
while t < c:
	if vt[t] == max(vt):
		print(t)
	t = t + 1
	