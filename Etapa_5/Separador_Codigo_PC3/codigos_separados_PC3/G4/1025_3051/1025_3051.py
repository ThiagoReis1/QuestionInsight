l=float(input("largura: "))
c=float(input("comprimento: "))
pre=float(input("valor do servico: "))

d1=max(l,c)
d2=min(l,c)

perimento=2*(d1+d2)
cust=perimento*pre
print(round(cust,2))