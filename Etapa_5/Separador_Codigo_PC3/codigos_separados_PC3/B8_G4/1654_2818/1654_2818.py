from numpy import *
vet = input("Estados: ")
vet = vet.split(',')
vet2 = zeros(5, dtype = int)
i = 0
am = 0
pe = 0
mg = 0
sp = 0
rs = 0
tamanho = size(vet)
while (i < tamanho):
	if (vet[i] == 'AM'):
		vet2[0] = vet2[0] + 1
		am = am + 1
		i = i + 1
	elif (vet[i] == 'PE'):
		vet2[1] = vet2[1] + 1
		pe = pe + 1
		i = i + 1
	elif (vet[i] == 'MG'):
		vet2[2] = vet2[2] + 1
		mg = mg + 1
		i = i + 1
	elif (vet[i] == 'SP'):
		vet2[3] = vet2[3] + 1
		sp = sp + 1
		i = i + 1
	elif (vet[i] == 'RS'):
		vet2[4] = vet2[4] + 1
		rs = rs + 1
		i = i + 1
	
if (am > pe and am > mg and am > sp and am > rs):
	print (am)
elif (pe > am and pe > mg and pe > sp and pe > rs):
	print (pe)
elif (mg > pe and mg > am and mg > sp and mg > rs):
	print (mg)
elif (sp > am and sp > pe and sp > mg and sp > rs):
	print (sp)
elif (rs > am and rs > pe and rs > mg and rs > sp):
	print (rs)
	
	
print (vet2)
