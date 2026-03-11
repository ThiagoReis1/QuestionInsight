from numpy import*
v=array(eval(input("Notas:")))
soma=sum(v)
menor=min(v)
n=size(v)
m=n-1		 
media=(soma-menor)/m
print(round(media,2))