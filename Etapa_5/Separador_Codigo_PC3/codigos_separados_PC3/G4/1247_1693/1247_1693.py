from numpy import*
x=array(eval(input("qual vetor: ")))
x1= array(zeros(2, dtype=int))
cont = 0
cont1 = 0
for i in range(0, size(x)):
	a = min(x)
	b = max(x)
c = (0.75 * a) + (0.25 * b)
d = (0.25 * a) + (0.75 * b)
for j in range(0, size(x)):
	if x[j] >= a and x[j] < c:
		cont = cont + 1
for k in range(0, size(x)):	
	if x[k] >= d and x[k] < b:
		cont1 = cont1 + 1
x1[0] = cont
x1[1] = cont1
print(x1)