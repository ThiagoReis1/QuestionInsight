from numpy import*

v = array(eval(input()))

m = zeros(4, dtype=int)
for i in v:
	if(i == "BOTAFOGO"):
		m[0] = m[0] + 1
	if(i == "FLAMENGO"):
		m[1]= m[1] + 1
	if(i == "FLUMINENSE"):
		m[2]= m[2] + 1
	if(i == "VASCO"):
		m[3]= m[3] + 1
print(m)