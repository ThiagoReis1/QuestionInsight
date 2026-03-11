from numpy import*
v = array(eval(input("vetor: ")))

i = 0  #contadora
total = 0  #variavel acumuadora para pontuacao

while i < size(v):
	if v[i] == 1:
		total = total + 100
	elif v[i] == 2:
		total = total + 60
	elif v[i] == 3:
		total = total + 20
	elif v[i] == 4:
		total = total
	i += 1
print(total)