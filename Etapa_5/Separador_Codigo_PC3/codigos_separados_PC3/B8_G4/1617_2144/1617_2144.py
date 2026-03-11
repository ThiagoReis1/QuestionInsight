from numpy import*

e = array(eval(input("Tipos de espada: ")))
l = array(eval(input("Nível dos combatentes: ")))

n = size(e)
Te = zeros( n , dtype = int)

t = 0
k = 0

while (t < size(e)):
	if (e[t] == "CENOURA"):
		Te[k] = 2
		k = k + 1
	elif (e[t] == "FERRO"):
		Te[k] = 4
		k = k + 1
	elif(e[t] == "DWARVEN"):
		Te[k] = 8
		k = k + 1
	elif(e[t] == "ELVEN"):
		Te[k] = 11
		k = k + 1
	elif(e[t] == "DAEDRIC"):
		Te[k] = 14
		k = k + 1
	t = t + 1

i = 0
dc = 0

while( i < size(Te)):
	dc = dc + (Te[i] * l[i])
	i = i + 1
	
print(dc)