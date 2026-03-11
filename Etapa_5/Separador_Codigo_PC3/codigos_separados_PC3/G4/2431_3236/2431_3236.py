ppc = float(input())
ppa = float(input())

desconto = ppa - (ppa * (35 / 100))

vf = ppc + desconto

print(float(round(ppc, 2)))
print(float(round(desconto, 2)))
print(float(round(vf, 2)))