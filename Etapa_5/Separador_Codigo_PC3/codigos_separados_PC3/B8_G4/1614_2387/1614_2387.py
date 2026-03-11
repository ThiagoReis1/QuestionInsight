from numpy import*
nomes = array(eval(input()))
quant = array(eval(input()))
a = size(nomes)
i = 0
ban = 0.97
bife = 2.95
fei = 1.27
ome = 1.04
tom = 0.2
t = 0 
while(i < a):
	if(nomes[i] == "BANANA"):
		t = t + quant[i]*ban
	elif(nomes[i] == "BIFE"):
		t = t + quant[i]*bife
	elif(nomes[i] == "FEIJOADA"):
		t = t + quant[i]*fei
	elif(nomes[i] == "OMELETE"):
		t = t + quant[i]*ome
	elif(nomes[i] == "TOMATE"):
		t = t +  quant[i]*tom
	i = i + 1	
print(round(t, 2))
	
	