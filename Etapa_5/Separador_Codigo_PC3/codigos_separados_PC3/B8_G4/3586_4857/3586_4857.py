from numpy import* 
vt = array(eval(input("Digite os numeros: ")))
t = 0
i = 0
while i < size(vt):
	if vt[i] == 1:
		t = t + 100
	elif vt[i] == 2:
		t = t + 60
	elif vt[i] == 3:
		t = t + 20
	elif vt[i] == 4:
		t = t+0
	i = i +1
print(t)