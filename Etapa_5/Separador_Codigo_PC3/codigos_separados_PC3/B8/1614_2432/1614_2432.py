from numpy import*
BANANA = 0.97
BIFE = 2.95
FEIJOADA = 1.27
OMELETE = 1.04
TOMATE = 0.2
n = array(eval(input()))
v = array(eval(input()))
i = 0 
w = 0
while i < size(n):
	if n[i] == "BANANA": 
		w= w + BANANA*v[i]
		i += 1
	elif n[i] == "BIFE":
		w= w + BIFE*v[i]
		i += 1
	elif n[i] == "FEIJOADA":
		w= w + FEIJOADA*v[i]
		i += 1
	elif n[i] == "OMELETE":
		w= w + OMELETE*v[i]
		i += 1
	elif n[i] == "TOMATE": 
		w= w + TOMATE*v[i]
		i += 1
print(round(w,2))