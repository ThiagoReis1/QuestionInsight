from numpy import *
v = input("digite o time: ")
saida = zeros(4, dtype = int)
times = ["BOTAFOGO", "FLAMENGO", "FLUMINENSE", "VASCO"]
for i in range(size(v)):
	if(times[i]== "BOTAFOGO" ):
		saida[0] = saida[0] + 1

	elif(times[i]== "FLAMENGO"):
		saida[1] = saida[1] + 1
	
	elif(times[i]== "FLUMINENSE"):
		saida[2] = saida[2] + 1
	
	elif(times[i]== "VASCO"):
		saida[3] = saida[3] + 1
print(saida)
