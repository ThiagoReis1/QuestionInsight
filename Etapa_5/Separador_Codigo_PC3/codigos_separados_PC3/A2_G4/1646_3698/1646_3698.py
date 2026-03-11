from numpy import * 
x = array(eval(input("Saques: ")))
i = 0
for r in range(size(x)):
	if x[r]<=50:
		i = i +1
	else:
		i = i
print(i)
z= zeros(i, dtype = int)
q = 0
for w in range(size(x)):
	if (x[w] <=50):
		z[q] = z[q] + w
		q = q+1
print(z)