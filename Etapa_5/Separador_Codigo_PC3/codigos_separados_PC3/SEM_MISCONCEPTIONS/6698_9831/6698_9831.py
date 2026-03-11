pracas= int(input("entre com a qtde: "))
icms= 0.15

p1= (pracas * 9.80) + 20

vtotal= p1 * icms + p1


print(round(vtotal,2))