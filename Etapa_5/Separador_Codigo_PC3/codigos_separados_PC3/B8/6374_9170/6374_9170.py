from numpy import*

p = input("Especialidade de paciente: ").upper().split(",")
result = zeros(4, dtype=int)

for i in range(len(p)):
	if p[i]=="O":
		result[0]+=1
	elif p[i]== "D":
		result[1]+=1
	elif p[i]=="N":
		result[2]+=1
	elif p[i]=="C":
		result[3]+=1
print(result)

