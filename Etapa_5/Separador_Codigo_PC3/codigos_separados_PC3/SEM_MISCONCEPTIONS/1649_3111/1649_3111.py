from numpy import*

Cabelos = input("olhos:")
ArrayCabelos = array(olhos.split(","))

ListaCabelos = zeros(5, dtype=int)

for i in range(size(Arrayolhos)):
	if((Arrayolhos[i]).upper() == 'P'):
		Listaolhos[0] += 1
	elif((Arrayolhos[i]).upper() == 'C'):
		Listaolhos[1] += 1
	elif((Arrayolhos[i]).upper() == 'M'):
		Listaolhos[2] += 1
	elif((Arrayolhos[i]).upper() == 'V'):
		Listaolhos[3] += 1
	elif((Arrayolhos[i]).upper() == 'A'):
		Listaolhos[4] += 1

MaisComum = 0;
for i in range(5):
	if(Listaolhos[i] > MaisComum):
		MaisComum = Lista[olhos[i]

		
print(MaisComum)
print(Listaolhos)