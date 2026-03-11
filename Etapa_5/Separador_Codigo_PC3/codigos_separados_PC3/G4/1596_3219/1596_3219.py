from numpy import*
vet= array(eval(input( )))

x=sum(vet)-min(vet)
y= x/(size(vet)-1)
print(round(y,2))
