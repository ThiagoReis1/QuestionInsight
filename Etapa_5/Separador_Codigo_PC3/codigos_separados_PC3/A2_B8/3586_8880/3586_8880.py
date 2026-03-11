from numpy import*
nanel= array(eval(input("numeros: ")))
p=0
i=0

while i<size(nanel):
	if nanel[i] == 1 :
		p= p + 100
	elif nanel[i]==2 :
		p= p+60
	elif nanel[i]== 3 :
		p=p+20
	if nanel[i]== 4:
		p=p
	i= i+1	
print(p)		