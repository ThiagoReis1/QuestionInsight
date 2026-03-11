from numpy import*
v = array(eval(input('')))
l1 = v[0]*0.20 + v[0]
l2 = v[0]*0.50 + v[0]

inf = 0
for i in range(size(v)):
	if(v[i] != v[0]) and (l1 > v[i] < l2):
		inf = inf + 1
		print(i)
		print(inf)