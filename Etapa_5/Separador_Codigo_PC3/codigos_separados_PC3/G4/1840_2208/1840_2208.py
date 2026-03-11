n=float(input("Digite o mol: "))
V=float(input("Digite o volume do gas: "))
t=float(input("Digite o gas: "))
T=t+273.1

R=0.082057

p=(n*R*T)/V

print(p)