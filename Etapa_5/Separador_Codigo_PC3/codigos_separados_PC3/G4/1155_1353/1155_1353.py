nvs=int(input("Número de cópias iniciais do vírus no sangue:"))
nls=int(input("Número inicial de leucócitos no sangue:"))

tv=float(input("Taxa (em %) de multiplicação diária do vírus:"))
tl=float(input("Taxa (em %) de multiplicação diária dos leucócitos:"))

tv=(tv/100)+1
tl=(tl/100)+1
d=1

while(nvs>=nls*2):
	nvs=nvs*tv
	nls=nls*tl
	d=d+1
print(d)

