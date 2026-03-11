n=float(input("Digite o numero de mols"))
v=float(input("Digite o volume"))
t=float(input("Digite a temperatura"))
tc=t+273.1
r=0.082057
p=(n*r*tc)/v
print(p)