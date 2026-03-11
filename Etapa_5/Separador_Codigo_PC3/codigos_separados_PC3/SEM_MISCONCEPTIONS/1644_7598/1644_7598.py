from numpy import*

mf = array(eval(input("media final")))
cont = zeros(N, dtype=int)

for i in range(size(mf)):
	if (mf >= 5):
		cont[1] = cont[0] + 1
		
	else:
		cont = cont[1] - 1
		
for i in range(size(mf)):
	
