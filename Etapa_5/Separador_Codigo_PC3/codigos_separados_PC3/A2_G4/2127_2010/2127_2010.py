
from numpy import *

nota=array(eval(input()))

i=0
acm=0
while(i<size(nota)):
	if nota[i]==min(nota):
		acm=acm
	else:
		acm=acm+nota[i]

	i=i+1
media=acm/3.0
if (media>=50.0):
	print(round(media,2))
	print("APROVADO")
else:
	print(round(media,2))
	print("REPROVADO")
