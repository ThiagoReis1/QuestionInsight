from numpy import *

vn = array(str(input("Nome dos produtos: ")))
vq = array(eval(input("Quantidades: ")))


conta = (1.25* vq[0]) + (2.6* vq[1]) + (1.8* vq[2]) + (0.85* vq[3]) + (3.2* vq[4])

print(round(conta, 2))

