rom numpy import*

p = array(eval(input()))
a = array(eval(input()))
k = size(p)
m = zeros(k, dtype=float)
j = 0
while (j < size(p)):
	imc = p[j]/(a[j]**2)
	m[j] = (round(m[j] + imc, 2))
	j = j + 1
if (max(m) < 17.00):
	l = "MUITO ABAIXO DO PESO"
if (max(m) >= 17.00 and max(m) <= 18.49):
	l = "ABAIXO DO PESO"
if (max(m) >= 18.50 and max(m) <= 24.99):
	l = "PESO NORMAL"
if (max(m) >= 25.00 and max(m) <= 29.99):
	l = "ACIMA DO PESO"
if (max(m) >= 30.00 and max(m) <= 34.99):
	l = "OBESIDADE"
if (max(m) >= 35.00 and max(m) <= 39.99):
	l = "OBESIDADE SEVERA"
if (max(m) >= 40.00):
	l = "OBESIDADE MORBIDA"
print(m)
print("O MAIOR IMC DA TURMA EH:",round(max(m),2))
print(l)