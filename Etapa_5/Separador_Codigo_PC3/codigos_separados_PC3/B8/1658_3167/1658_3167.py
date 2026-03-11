from numpy import*
m = array(input("").split(','))
res = zeros(5, dtype = int)
print(m)
for i in m:
	if(i == "CHN"):
		res[0] += 1
	elif(i == "JPN"):
		res[1] += 1
	elif(i == "KOR"):
		res[2] += 1
	elif(i == "MGL"):
		res[3] += 1
	elif(i == "THA"):
		res[4] += 1
m_max = max(res)
print(m_max)
print(res)