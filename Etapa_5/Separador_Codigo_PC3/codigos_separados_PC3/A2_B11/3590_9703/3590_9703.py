from numpy import * 

dado = array(eval(input()))
ganha = 0

i = 0
while i < size(dado):
	if dado[i] == 1:
		ganha = ganha + 10
	if dado [i] == 2:
		ganha = ganha + 5
	if dado[i] == 3:
		ganha = ganha
	if dado[i] == 4:
		ganha = ganha + 5
	if dado[i] == 5:
		ganha = ganha + 20
	if dado[i] == 6:
		ganha = ganha + 10
	i += 1
print(ganha)