from numpy import*

anel = array (eval (input ("digite um vetor: ")))
pto= 10000

i= 0
while i < size(anel):
	if anel[i] == 1 :
		pto *= 2 
	elif anel[i] == 2:
		pto = pto
	elif anel[i]== 3 :
		pto /= 2
	elif anel[i] == 4:
		pto /= 4
	i = i + 1

print (round (pto, 2))