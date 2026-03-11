from numpy import*
vet= array(eval(input("")))
f= sum(vet)-min(vet)
g= size(vet) - 1
media= f/g
print(round(media, 2))