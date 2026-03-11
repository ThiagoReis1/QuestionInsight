from numpy import*
v = array(eval(input("")))

i = 0
t = []

while(i < size(v)):
	if(v[i] > min(v)):
		t.append(v[i])
	i += 1
		
mf = (v[0] * 5.0 + v[1] * 2.5 + v[2] * 2.5) / 10.0	
print(round(mf,2))

if(mf >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")