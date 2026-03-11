from numpy import *

pont=array(eval(input("pontuacao:")))

i=0
a = 0
while (i < size(pont)):
	if (pont[i] == 1):
		a=  a +80
	if (pont[i] == 2):
		a = a + 40
	if (pont[i] == 3):
		a = a + 20
	i=i+1
	
print(a)
	