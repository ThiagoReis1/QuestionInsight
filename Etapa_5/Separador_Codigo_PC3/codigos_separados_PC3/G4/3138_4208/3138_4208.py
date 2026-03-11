from numpy import*

N=array(eval(input("")))
tam=size(N)
soma=0
i=0
H=tam-1
while(i<=H):
	soma=soma+(N[i]**7)
	i=i+1
media=(soma/tam)**(1/7)
print(round(media,2))