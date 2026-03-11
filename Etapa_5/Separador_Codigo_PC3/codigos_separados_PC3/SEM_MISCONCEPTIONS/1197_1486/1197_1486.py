from numpy import *

vtemper = array(eval(input("Vetor:")))
vvalido = 0
i = 0

while(i < size(vtemper)):
	if(vtemper[i] < 50):
		vvalido = vvalido + 1
	i = i + 1
	
new = array(zeros(vvalido, dtype = float))
i = 0
m = 0

while(i < size(vtemper)):
	if(vtemper[i] < 50):
		new[m] = new[i]
		m = m + 1
	i = i + 1
print(new)