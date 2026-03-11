from numpy import*
v=array(eval(input("vetor:")))
i=0
soma=0
total=0
media=0
n=size(v)
while(i<size(v)):
	soma=soma+(v[i]**(1/3))
	i=i+1
media=(soma/n)**(3)
print(round(media,2))

