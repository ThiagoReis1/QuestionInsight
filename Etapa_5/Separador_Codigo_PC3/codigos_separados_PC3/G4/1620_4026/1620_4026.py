from numpy import*
temp=array(eval(input("Tempos dos banhos:")))
percent=array(eval(input("Percentual de abertura da torneira:")))
n=size(temp)
z=0
for i in range(n):
	z=z+(temp[i]*5*(percent[i]/100))
print(round(z, 2))