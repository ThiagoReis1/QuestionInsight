from numpy import*

v = str(input("Diga o tom de pele das pessoas: ")).split(',')
cont = zeros(6,dtype=int)

for i in v:
	
   mc = cont[0]
	
   c = cont[1]
	
   cm = cont[2]
	
   em = cont[3]
	
   e = cont[4]
	
   me = cont[5]
	
   cont[i] = cont[i] + 1

print(cont)