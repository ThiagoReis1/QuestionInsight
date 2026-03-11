var = float(input("insira a quantidade de kwh: "))

V = (var * 0.43 + 10.0)

P = 0.25 * V

M = V + P


print(round(M, 2))