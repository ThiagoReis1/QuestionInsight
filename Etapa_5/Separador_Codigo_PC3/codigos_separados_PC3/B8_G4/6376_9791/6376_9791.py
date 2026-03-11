from numpy import *
j = input("jogador (A) jogador (B) jogador (C) Jogador (E):").upper().split(",")
p = zeros(4,dtype=int)
for v in j:
	if v == "A":
		p[0] += 1
	elif v == "B":
		p[1] += 1
	elif v == "C":
		p[2] += 1
	elif v == "D":
		p[3] += 1
		
print(p)
		