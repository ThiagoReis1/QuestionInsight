from numpy import*

p = input("Informe o paciente: ").upper().split(",")
x = zeros(4, dtype=int)

for i in range(len(p)): 
	if(p[i] == "O"):
		x[0] = x[0] + 1
	elif(p[i] == "D"):
		x[1] = x[1] + 1
	elif(p[i] == "N"):
		x[2] = x[2] + 1
	elif(p[i] == "C"):
		x[3] = x[3] + 1
		
print(x)