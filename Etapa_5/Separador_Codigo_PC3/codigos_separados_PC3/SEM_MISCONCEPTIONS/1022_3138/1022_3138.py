aresta=float(input("quanto q mede o baguio?"))
custo_app=float(input("quanto a facada?"))

from math import*
A=(2*aresta**2*(sqrt(2)+1))

custo_total=(A*custo_app)

print(round(custo_total, 2))