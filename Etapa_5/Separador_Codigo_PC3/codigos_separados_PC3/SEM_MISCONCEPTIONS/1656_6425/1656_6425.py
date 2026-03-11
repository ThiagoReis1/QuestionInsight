from numpy import*
v=input("paises: ").split(',')

cont = zeros(5, dtype=int) 


for pais in v:
	if pais == "BE":
		cont[0]=cont[0]+1
	if pais == "ES":
		cont[1]=cont[1]+1
	if pais == "FR":
		cont[2]=cont[2]+1
	if pais == "IT":
		cont[3]=cont[3]+1
	if pais == "PT":
		cont[4]=cont[4]+1

maior=0
for valor in cont:
	if valor > maior:
		maior=valor
print(maior)
print(cont)
