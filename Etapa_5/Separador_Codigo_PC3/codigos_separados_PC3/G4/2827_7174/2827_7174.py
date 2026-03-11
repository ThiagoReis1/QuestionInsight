from numpy import*
nota=array(eval(input("notas:")))
i=0
while(i!=size(nota)):
	if(nota[i]>4 and nota[i]<5):
		nota[i]=4
		i=i+1
	elif(nota[i]>9 and nota[i]<10):
		nota[i]=10
		i=i+1
	else:
		i=i+1
print(nota)