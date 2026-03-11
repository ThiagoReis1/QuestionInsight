from numpy import*
v=array(eval(input("Reais:")))
i=0
t=size(v)
M=0

while(i<t):
	M+=(v[i])**(2)
	i=i+1
media=(M/t)**(1/2)
media=round(media, 2)
print(media)