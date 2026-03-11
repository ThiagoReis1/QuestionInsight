from numpy import *

nota=array(eval(input()))

i=0
acm=0
while(i<size(nota)):
	if nota[i]==max(nota):
		acm=acm
	else:
		acm=acm+nota[i]

	i=i+1
media=acm/3.0
if (media>=5.0):
	print(round(media,2))
	print("APROVOU")
else:
	print(round(media,2))
	print("REPROVOU")
