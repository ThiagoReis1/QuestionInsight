from numpy import*
acertos = array(eval(input("Acertos: ")))
i = 0
p = 0
while i < size(acertos):
	if acertos[i] == 1:
		p = p + 80
	if acertos[i] == 2:
		p = p + 40
	if acertos[i] == 3:
		p = p + 20
	if acertos[i] == 4:
		p = p + 10
	i = i + 1
print(p)