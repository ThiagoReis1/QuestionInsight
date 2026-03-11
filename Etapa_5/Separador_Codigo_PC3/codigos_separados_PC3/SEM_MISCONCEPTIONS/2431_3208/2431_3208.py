cliente=float(input())
acompanhante=float(input())

desconto= acompanhante-(acompanhante*(35/100))
cl=cliente
ac=cliente+desconto
print(round(cl ,2))
print(round(desconto ,2))
print(round(ac ,2))