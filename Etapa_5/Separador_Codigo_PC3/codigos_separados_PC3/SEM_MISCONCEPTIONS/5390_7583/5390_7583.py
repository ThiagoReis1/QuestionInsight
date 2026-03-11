from numpy import*

x = input("rotulo da etiqueta: ").upper()

i = 0
v = 0
vn = 0

while(i < len(x)):
	if(x[i] == "A") or (x[i] == "E") or (x[i]=="I") or (x[i]=="O") or (x[i]=="U"):
		v = v + 1
	else:
		vn = vn + 1
	i = i + 1
	vogal = v * 0.19
	vagalnao = vn * 0.23
	total = vogal + vagalnao
print(round(total,2))
	

