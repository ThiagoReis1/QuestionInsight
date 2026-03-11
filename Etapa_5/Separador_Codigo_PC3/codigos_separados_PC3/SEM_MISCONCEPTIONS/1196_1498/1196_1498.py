from numpy import*
temperatura = array(eval(input("digite as temperaturas: ")))
v = 0
l = 0
while( v < size(temperatura)):
	if(temperatura[v] >= -60 and temperatura[v] <= 60):
		l = l + 1
	v = v + 1
temperatura1 = array(zeros(l, dtype = float))
v = 0
l = 0
while( v < size(temperatura)):
	if(temperatura[v] >= -60 and temperatura[v] <= 60):
		temperatura1[l] = temperatura[v]
		l = l + 1
	v = v + 1
print(temperatura1)