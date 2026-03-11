p = float(input("digite a pressao:"))
n = float(input("digite o num de mols:"))
t = float(input("digite a temperatura:"))
r = 0.082
v =(n*r*(t+273.15))/p
print(v)
