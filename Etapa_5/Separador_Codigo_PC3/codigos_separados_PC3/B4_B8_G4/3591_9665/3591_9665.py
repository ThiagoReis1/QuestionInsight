from numpy import * 

Vn = array(eval(input("digite o vetor de numeros: ")))

f = 0 
pt = 0 
while f < size(Vn):
	if Vn[f] == 1:
		pt = pt + 10
	elif Vn[f] == 2: 
		pt = pt + 5
	elif Vn[f] == 3: 
		pt = pt + 10
	elif Vn[f] == 4:
		pt = pt + 5 
	elif Vn[f] == 5:
		pt = pt + 10
	elif Vn[f] == 6:
		pt = pt + 5

	f = f + 1
print(pt)