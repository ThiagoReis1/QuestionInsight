#Start!
p = float(input("qual a pressão do gas em atm's?"))
n = int(input("qual o número de mols do gas?"))
t = float(input("qual a temperatura do gás em celsius?"))
R = 0.082

L = ((t+273.15))

V = n*R*L/p

print(V)
