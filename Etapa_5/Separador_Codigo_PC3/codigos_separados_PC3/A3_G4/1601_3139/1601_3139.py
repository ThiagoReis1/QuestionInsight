from numpy import* 

vet = array(eval(input("tempo dos competidores: ")))

x = min(vet)
cp = 0
cont = 0

while(cp < size(vet)):
	if(vet[cp] == min(vet)):
		cont = cont + 1
		print(cp)
	cp = cp + 1

