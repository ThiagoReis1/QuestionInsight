#
#

from numpy import*
prod = array(["ARROZ","FEIJAO","BIS","MIOJO","FANTA"])
preco = array([1.25, 2.60, 1.80, 0.85, 3.20])


vnp = array(eval(input("Digite os nomes: ").upper()))
vq = array(eval(input("Digite a quantidade: ")))

i = 0
t = 0

while(i < size(vq)):
	if("ARROZ" == vnp[i]):
		t = t + (vq[i]*1.25)
		
	elif("FEIJAO" == vnp[i]):
		t = t + (vq[i]*2.60)
		
	elif("BIS" == vnp[i]):
		t = t + (vq[i]*1.80)
		
	elif("MIOJO" == vnp[i]):
		t = t + (vq[i]*0.85)
		
	else:
		t = t+(vq[i]*3.20)
		
	i = i + 1
print(round(t,2))






