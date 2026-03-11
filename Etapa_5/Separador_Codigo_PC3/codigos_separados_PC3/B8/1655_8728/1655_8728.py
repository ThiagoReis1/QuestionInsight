from numpy import*
x = zeros(5,dtype=int)
estados = input().upper()
estados = estados.split(",")
for estado in estados:
	if estado == "AC":
		x[0]+=1
	elif estado == "AM":
		x[1]+=1
	elif estado == "PA":
		x[2]+=1 
	elif estado == "RO":
		x[3]+=1
	elif estado == "RR":
		x[4]+=1
print(max(x))
print(x)