from numpy import*
vet=array(eval(input( )))
y=sum(vet)-min(vet)
x=size(vet)-1
media=y/x
print(round(media,2))