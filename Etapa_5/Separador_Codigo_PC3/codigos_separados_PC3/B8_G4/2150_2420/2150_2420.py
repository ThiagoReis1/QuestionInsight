from numpy import*
vet = array(eval(input("times: ")))
m = zeros(4, dtype=int)
for i in vet:
	if i == 'BOTAFOGO':
		m[0] += 1
	elif i == 'FLAMENGO':
		m[1] += 1
	elif i == 'FLUMINENSE':
		m[2] += 1
	elif i == 'VASCO':
		m[3] += 1
print(m)
