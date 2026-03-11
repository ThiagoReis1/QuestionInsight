from numpy import *
nota = array( eval ( input ("digite: ")))
i=0
total=0
				 
while i < size(nota):
	if i == 0:
		total = total + nota[i]*3
	if i == 1:
		total = total + nota[i]*2
	if i==2:
		total = total + nota[i]*4
	if i==3:
		total = total + nota[i]*1
	if i==4:
		total = total + nota[i]*3
		
	i = i + 1
				 
media = total / 13

				 
print(round(media,2))
				 