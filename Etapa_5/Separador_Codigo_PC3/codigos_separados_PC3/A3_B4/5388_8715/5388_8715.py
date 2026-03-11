from numpy import*

string = input().upper()

custo = 0
v1= 25.12
v2 = 40.18

for i in string:
	if i == "A":
		custo += 1 + v1
	elif i == "E":
		custo += 1 + v1
	elif i == "I":
		custo  += 1 + v1
	elif i == "O":
		custo += 1 + v1
	elif i == "U":
		custo += 1 +v1
	else:
		custo += 1 + v2
	
soma = custo

print(round(custo,2))