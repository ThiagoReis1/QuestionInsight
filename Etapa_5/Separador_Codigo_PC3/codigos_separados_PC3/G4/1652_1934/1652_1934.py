from numpy import *

v = input("V: ")
v = v.replace("PA", "k")
v = v.replace("PR", "l")

b = 0
pa = 0
pr = 0
a = 0
i = 0

for j in range(0,len(v),2):
	if(v[j]== "B"):
		b = b + 1
	if(v[j] == "k"):
		pa = pa + 1
	if(v[j] == "l"):
		pr = pr + 1
	if(v[j] == "A"):
		a = a + 1
	if(v[j] == "I"):
		i = i + 1

v_2 = array([b, pa, pr, a, i])
print(max(v_2))
print(v_2)