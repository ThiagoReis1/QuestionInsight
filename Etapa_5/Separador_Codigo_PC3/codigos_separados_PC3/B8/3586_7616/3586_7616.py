from numpy import*

acertos = array(eval(input("Acertos: ")))

i = 0
p = 0

while i < size(acertos):
	if acertos[i] == 1:
		p = p + 100
	elif acertos[i] == 2:
		p = p + 60
	elif acertos[i] == 3:
		p = p + 20
	elif acertos[i] == 4:
		p = p + 0
	
	i += 1
	
print(p)