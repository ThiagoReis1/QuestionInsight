from numpy import*
v = array(eval(input("temperaturas registradas:")))
i = 0
t = 0
l = (-100)
while i < size(v):
	if v[i] > l:
		t = t + 1
	i = i + 1
	
vn = array(zeros(t, dtype = float))
i = 0
t = 0
while i < size(v):
	if v[i] > l:
		vn[t] = v[i]
		t = t + 1
	i = i + 1
print(vn)