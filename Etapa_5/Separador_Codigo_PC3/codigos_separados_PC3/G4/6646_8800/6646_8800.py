from numpy import*

n = array(eval(input("digite as notas: ")))

n0 = n[0]
n1 = n[1] * 2
n2 = n[2] * 3

media = (n0 + n1 + n2) / 6
print(round( media, 2))