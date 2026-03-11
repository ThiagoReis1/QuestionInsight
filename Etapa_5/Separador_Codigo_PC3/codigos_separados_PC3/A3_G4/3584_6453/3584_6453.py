from numpy import*
v = array(eval(input("Digite o valor: ")))

i = 0
t = 0
d = 0
while(i < size(v)):
	if(v[i] > 200):
		d = v[i] - v[i]*0.15
		t = d + t
	else:
		t = v[i] + t
	i = i + 1
print(round(t, 2))
		
		
