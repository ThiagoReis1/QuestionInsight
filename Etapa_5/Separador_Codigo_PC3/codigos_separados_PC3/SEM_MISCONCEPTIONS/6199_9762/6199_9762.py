altmono = 1.8
txmono = 0.01
cont = 0

altfelino = float(input())
txfelino = float(input())

while altfelino < altmono:
	altfelino = (txfelino) + altfelino
	altmono = (txmono) + altmono
	cont = cont + 1
print(cont)