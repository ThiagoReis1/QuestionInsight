from numpy import*

vd = array(eval(input("Vetor de dano: ")))

#Variacel acumuladoras
i = 0
vc2 = 1
vc3 = 0
					 			 
while (i < size(vd)):
	dano = vd[i] * vc2 #vetor * peso	
	vc2 = vc2 + 1 #acumuladora do peso de atk
	vc3 = vc3 + dano #acumuladora do atk
	i = i + 1
print(vc3)