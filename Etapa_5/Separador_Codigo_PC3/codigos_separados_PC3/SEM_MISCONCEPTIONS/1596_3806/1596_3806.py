from numpy import *

vet= array(eval(input("n: ")))
t=size(vet)-1
media= (sum(vet)-min(vet))/t
print(round(media,2))