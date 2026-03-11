from numpy import*
olhos = input("cor dos olhos: ")
aolhos = array(olhos.split(","))

listaolhos = zeros(5, dtype=int)

for i in range(size(aolhos)):
	if((aolhos[i]).upper() == 'P'):
		listaolhos[0] += 1
	elif((aolhos[i]).upper() == 'C'):
		listaolhos[1] += 1
	elif((aolhos[i]).upper() == 'M'):
		listaolhos[2] += 1
	elif((aolhos[i]).upper() == 'V'):
		listaolhos[3] += 1
	elif((aolhos[i]).upper() == 'A'):
		listaolhos[4] += 1

maiscomum = 0;
for i in range(5):
	if(listaolhos[i] > maiscomum):
		maiscomum = listaolhos[i]
		
print(maiscomum)
print(listaolhos)
		