from numpy import*
t = input("Digite A para adm, P para producao, D para desenvolvimento e M para marketing: ").upper().split(",")
x = zeros(4, dtype = int)

for i in range(len(t)):
	if t[i] == "A":
		x[0] += 1
	elif t[i] == "P":
		x[1] += 1
	elif t[i] == "D": 
		x[2] += 1
	elif t[i] == "M":
		x[3] += 1
print(x)