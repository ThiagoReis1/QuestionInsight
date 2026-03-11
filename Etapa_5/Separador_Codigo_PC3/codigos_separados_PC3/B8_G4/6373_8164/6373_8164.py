from numpy import*
t = input("digite o codigo da tarefa: ").upper().split(',')

v = zeros(4, dtype=int)
for i in range(len(t)):
	if t[i] == "A":
		v[0] = v[0] + 1
		
	elif t[i] == "P":
		v[1] = v[1] + 1
	elif t[i] == "D":
		v[2] = v[2] + 1
	elif t[i] == "M":
		v[3] = v[3] + 1
print(v)
	