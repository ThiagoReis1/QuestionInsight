#Cupom de 35% de desconto para acompanhante ida e volta .
#Desconto so para o acompanhante

#Passagem do cliente (pc)
pc = float(input("preco numero 1"))

#Preco do acompanhante (pa)
pa = float(input("preco numero 2"))

#Valor do desconto (vd)
vd = 35

#Formula para o desconto (fd)
fd = pa - (pa * (vd / 100))

#Preco das passagens juntas (pj)
pj = pc + fd 

#Valores finais 

print(pc)
print(fd)
print(pj)