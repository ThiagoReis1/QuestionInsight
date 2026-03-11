kwh = float(input())
vf = 10.00

conta = (0.43 * kwh) + vf

valort = conta + conta * 0.25

print(round(valort, 2))
