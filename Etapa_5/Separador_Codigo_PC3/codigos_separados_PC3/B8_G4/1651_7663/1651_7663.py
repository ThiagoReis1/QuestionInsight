from numpy import*
cor = array(input("cor: ").upper().split(','))
v = zeros(6,dtype = int)

for i in range(size(cor)):
	if cor[i] == "MC":
		v[0] = v[0] + 1
	elif cor[i] == "C":
		v[1] = v[1] + 1
	elif cor[i] == "CM":
		v[2] = v[2] + 1
	elif cor[i] == "EM":
		v[3] = v[3] + 1
	elif cor[i] == "E":
		v[4] = v[4] + 1
	elif cor[i] == "ME":
		v[5] = v[5] + 1
print(max(v))
print(v)
