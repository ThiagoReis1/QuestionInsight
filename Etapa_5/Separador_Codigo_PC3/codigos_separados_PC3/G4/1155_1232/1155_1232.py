
v = int(input("Número de cópias iniciais do vírus no sangue:"))
l = int(input("Número inicial de leucócitos no sangue:"))
tv = float(input("Taxa (em %) de multiplicação diária do vírus:"))
tl = float(input("Taxa (em %) de multiplicação diária dos leucócitos:"))

t = 1

while(2*l<=v):
	v = v + v*(tv/100)
	l = l + l*(tl/100)
	t = t + 1
	
print(t)