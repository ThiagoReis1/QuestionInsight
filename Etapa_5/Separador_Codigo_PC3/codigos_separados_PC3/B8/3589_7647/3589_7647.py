from numpy import*

vetor = array(eval(input("Vetor de Numeros: ")))

i = 0
pt = 0

while(i < size(vetor)):
	if([vetor] == 1):
		pt = pt + 80
	elif([vetor] == 2):
		pt = pt + 40
	elif([vetor] == 3):
		pt = pt + 20
	elif([vetor] == 4):
		pt = pt + 10
	i = i + 1
	
print(pt)
		