from numpy import*

v=array(eval(input("n")))

a = 0

for i in range(0, size(v)):
	if (v[i-1]<5):
		a = a + 1

b=0
j=0
w =zeros(a, dtype=int)

for i in range(0, size(v)):
	if (v[i]<5):
		w[j]=b
		j=j+1
		b=b+1
	else:
		b=b+1
	
		
print(a)
print(w)
		