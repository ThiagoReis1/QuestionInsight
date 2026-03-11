from numpy import *
tempo = array(float(input("tempo de banho: "))) 
modo = array(input("modo de banho: ").upper())
conta = 0

quente = 90 * 0.005
morno = 45 * 0.005
frio = 0 * 0.005

while(modo != "FRIO"):
	if(modo == "QUENTE" ):
		conta = conta + quente * tempo
	elif(modo == "MORNO"):
		conta = conta + morno * tempo
	conta = conta + frio * tempo
print(round(conta, 2))
	
	