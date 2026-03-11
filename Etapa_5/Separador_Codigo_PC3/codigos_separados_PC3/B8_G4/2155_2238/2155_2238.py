from numpy import*
v = array(eval(input("Peso(Kg):")))
u = array(eval(input("Altura(m):")))

imc = zeros(size(v), dtype=float)

c = 0 
for i in v:
	imc[c] = round(i/(u[c]**2),2)
	c += 1 
print(imc)
print("O MAIOR IMC DA TURMA EH:",max(imc))

if (max(imc)<17):
	print(("muito abaixo do peso").upper())
elif (max(imc)>17)and(max(imc)<18.49):
	print(("abaixo do peso").upper())
elif (max(imc)>18.5)and(max(imc)<24.99):
	print(("peso normal").upper())
elif (max(imc)>25)and (max(imc)<29.99):
	print(("acima do peso").upper())
elif (max(imc)>30)and (max(imc)<34.99):
	print(("obesidade").upper())
elif (max(imc)>35)and (max(imc)<39.99):
	print(("obesidade severa").upper())
elif (max(imc)>40):
	print(("obesidade morbida").upper())
	