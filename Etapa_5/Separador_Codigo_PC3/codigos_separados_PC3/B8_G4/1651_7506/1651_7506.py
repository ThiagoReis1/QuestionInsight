from numpy import *

# Contar pessoas com mesmo tom de pele
# Determinar a maior quantidade de clientes com o MESMO tom de pele
# Vetor com a qt. de clientes com o mesmo tom, na ordem: MC, C, CM, EM, E, ME

#x = "c,c,c,mc,me".upper().split(",")
x = input("x: ").upper().split(",")

v = zeros(6, dtype=int)

for i in range(len(x)):
	if x[i] == "MC":
		v[0] += 1
	elif x[i] == "C":
		v[1] += 1
	elif x[i] == "CM":
		v[2] += 1
	elif x[i] == "EM":
		v[3] += 1
	elif x[i] == "E":
		v[4] += 1
	elif x[i] == "ME":
		v[5] += 1

print(max(v))
print(v)
	
	