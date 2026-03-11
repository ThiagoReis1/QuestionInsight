from numpy import*
v =  array(eval(input("Bota os precos ae meu patrao: ")))
if(v[0] > 80):
	v[0] = v[0] - 5
if(v[1] > 80):
	v[1] = v[1] - 5
if(v[2] > 80):	
	v[2] = v[2] - 5
total = v[0] + v[1] + v[2]
print(round(total,2))