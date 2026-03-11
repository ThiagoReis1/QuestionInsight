r = float(input("Quantidade de Ramem: "))
m = float(input("Quantidade de Menma: "))
b = float(input("Quantidade de Bolinho de arroz: "))
o = float(input("Quantidade de Onigi: "))

R = 7.00 ; M = 6.00 ; B = 3.00 ; O = 5.00 #RYOUS

vr = r * R
vm = m * M
vb = b * B
vo = o * O

valor = vr + vm + vb + vo

if( valor <= 42) :
	t = round( (valor - 3.00) ,2)
else:
	t = round( valor - ((valor/100)*10) ,2)
print(t, "ryous")