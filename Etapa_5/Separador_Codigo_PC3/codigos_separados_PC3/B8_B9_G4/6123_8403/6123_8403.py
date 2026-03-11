c = float(input('Quantidade de combustivel: '))
if c < 17.5:
 qz = c + .8
elif c >= 17.5 and c < 35.0:
 qz = c +1.3
elif c >= 35 and c < 50.0:
 qz = c +2.1
elif c >= 50:
 qz = c +3.0
print(round(qz,2))