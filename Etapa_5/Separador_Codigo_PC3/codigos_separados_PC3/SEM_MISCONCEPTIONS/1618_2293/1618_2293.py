from numpy import*
c = array(eval(input("vetor coeficiente: ")))
f = ""
i=0
while(i<size(c)):
	f= f+str(c[i]) '+' 'x^' '+'+str((size(c) -1 ))
	i += 1
print(f)
	