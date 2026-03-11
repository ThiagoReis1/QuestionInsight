from numpy import*
saques = array(eval(input("")))

d = 0
cont = zeros(5,dtype=int)
for i in range(size(saques)):	
	
	if(saques[i] >= 2000):
		d = d + 1
		cont = i	
		cont[0] =  cont[0] + 1
vetor= array([cont])		
print(d)
print(vetor)
	


