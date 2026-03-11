from numpy import*

soros = array(eval(input("Informe a ocorrencia dos soros: ")))
o = zeros(4, dtype = int)


for i in range(size(soros)):
	if(soros[i] == 1):
		o[0] += 1
	elif(soros[i] == 2):
		o[1] += 1
	elif(soros[i] == 3):
		o[2] += 1
	elif(soros[i] == 4):
		o[3] += 1
		
print(o)
		
	
	