p = float(input('pressão'))
n = float(input('número de mols'))
t = float (input('temperatura'))
T = t + 273.15
R = 0.082
v =  n * R * T / p
print(v)
