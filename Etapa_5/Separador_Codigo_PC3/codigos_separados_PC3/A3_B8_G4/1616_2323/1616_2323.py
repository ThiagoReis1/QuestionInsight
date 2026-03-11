from numpy import*

GELO = 2
FOGO = 3
CHOQUE = 4
CONJURACAO = 8
ILUSAO = 10
dm = 0
n = array(eval(input()))
v = array(eval(input()))
i = 0
t = []
while i < size(n):
	if n[i] == "GELO":
		dm = dm + 2* v[i]
	elif n[i] == "FOGO":
		dm = dm + 3* v[i]
	elif n[i] == "CHOQUE":
		dm = dm + 4* v[i]
	elif n[i] == "CONJURACAO":
		dm = dm + 8* v[i]
	elif n[i] == "ILUSAO":
		dm = dm + 10* v[i]
	i+=1	
print(round(dm,2))