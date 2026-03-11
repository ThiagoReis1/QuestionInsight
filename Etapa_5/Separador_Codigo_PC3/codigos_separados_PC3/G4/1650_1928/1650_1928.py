from numpy import *

v = input("V: ")


b = 0
pa = 0
pr = 0
a = 0
i = 0

for j in range(0,len(v),2):
	if(v[j]== "P"):
		b = b + 1
	if(v[j] == "C"):
		pa = pa + 1
	if(v[j] == "R"):
		pr = pr + 1
	if(v[j] == "L"):
		a = a + 1
	if(v[j] == "B"):
		i = i + 1

v_2 = array([b, pa, pr, a, i])
print(max(v_2))
print(v_2)