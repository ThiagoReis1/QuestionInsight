from numpy import*

estado = input("Digite os estados: ").upper()

k = estado.split(',')
m = zeros(5, dtype = int)

for i in range(size(k)):
	if k[i] == "AC":
		m[0] = m[0] + 1
	elif k[i] == "AM":
		m[1] = m[1] + 1
	elif k[i] == "PA":
		m[2] = m[2] + 1
	elif k[i] == "RO":
		m[3] = m[3] + 1
	elif k[i] == "RR":
		m[4] = m[4] + 1

print(max(m))
print(m)