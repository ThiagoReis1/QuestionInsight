from numpy import *
vn = array(eval(input("Nomes:")))
vq = array(eval(input("Quantidade:")))

i = 0
p1=0
p2=0
p3=0
p4=0
p5=0
while(i<size(vq)):
	if(vn[i]=='ARROZ'):
		p1 = 1.25*vq[i]
	elif(vn[i]=='FEIJAO'):
		p2 = 2.60*vq[i]
	elif(vn[i]=='BIS'):
		p3 = 1.80*vq[i]
	elif(vn[i]=='MIOJO'):
		p4 = 0.85*vq[i]
	elif(vn[i]=='FANTA'):
		p5 = 3.20*vq[i]
	i = i + 1
p = p1+p2+p3+p4+p5
print(round(p, 2))