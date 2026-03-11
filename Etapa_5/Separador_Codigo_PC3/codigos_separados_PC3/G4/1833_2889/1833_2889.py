#Ler a massa do caminhão A (Ma),massa do caminhão B (Mb), Velocidade do caminhão B (Vo)

Ma = float (input ("Qual a massa do caminhão A?"))
Mb = float (input ("Qual a massa do caminhão B?"))
Vo = float (input ("Qual a velocidade do caminhão B?"))

a = 2*Ma+Mb
b = Ma + Mb 

Vf = (a/b)*Vo

print (Vf)