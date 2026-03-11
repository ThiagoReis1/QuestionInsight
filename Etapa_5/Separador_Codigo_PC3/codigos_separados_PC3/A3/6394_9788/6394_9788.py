from numpy import*

mens = array(eval(input("mensagem:")))
mens_cod = zeros(size(mens), dtype = int)

for i in range(size(mens)):
	if mens[i] == 9:
		mens[i] = 0
	else:
		mens[i] = mens[i] + 1
print(mens)