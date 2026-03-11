from numpy import*

v = array(eval(input()))

i = 0
des = 0
soma = 0
for i in range(size(v)):
	if(v[i] > 200):
		des = v[i] * (15/100)
		v[i] = v[i] - des

	elif(v[i] < 200):
		v[i] = v[i]


print(round(sum(v),2))
