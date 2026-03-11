from numpy import*
v = array(eval(input()))
n = array(eval(input()))
dano = 0
t = 0
av = zeros(size(n),dtype=int)
while t < size(n):
	if v[t] == "CENOURA":
		av[t] = 2
	elif v[t] == "FERRO":
		av[t] = 4
	elif v[t] == "DWARVEN": 
		av[t] = 8
	elif v[t] == "ELVEN":
		av[t] = 11
	elif v[t] == "DAEDRIC": 
		av[t] = 14
	t = t + 1
y = 0
P = ["DAEDRIC","FERRO","CENOURA","FERRO"]
g = [2,1,5,8]
while y < size(n):
	dano = dano + av[y]*n[y]
	y = y + 1
print(dano)