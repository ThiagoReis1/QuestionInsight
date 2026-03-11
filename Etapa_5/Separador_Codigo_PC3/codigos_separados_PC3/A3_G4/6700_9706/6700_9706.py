dias = int(input("dias: "))
diaria = 50.0
taxa = 30.0
icms=  18/100

vt = (dias * diaria)+ taxa
vf = vt + vt*18/100
print(round(vf, 2))