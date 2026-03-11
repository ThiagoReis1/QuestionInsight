from numpy import *

notas= array(eval(input("Notas: ")))

ex=min(notas)

m2=sum(notas)

m1=m2-ex

total=size(notas)

media= m1/(total-1)

print(round(media, 2))