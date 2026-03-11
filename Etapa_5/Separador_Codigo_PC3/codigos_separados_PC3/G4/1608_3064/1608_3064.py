from numpy import*
x=array(eval(input("Informe os passageiros: ")))

i=0
s=0

while(i<size(x)):
	s=s+x[i]
	if(s>75):
		s=75
	i=i+1	
		
print(s)		