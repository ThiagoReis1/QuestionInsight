n = float(input("digite o numero de mols aqui: "))
v = float(input("digite o volume aqui: "))
t = float(input("digite a temperatura em celsius aqui: "))
r = 0.082057
# a seguir vamos determinar a formula de Clayperon para a devida aplicação
p = (n*r*(t + 273.1))/v
print(p)
