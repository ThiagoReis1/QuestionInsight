P=input(float("digite o valor da pressao: "))
n=input(float("Digite o valor de mols: "))
T=input(float("Digite o valor da temperatura: "))
Ta=(T+273.15)
R=0.082
v=(n*R*Ta)/P
print(v)