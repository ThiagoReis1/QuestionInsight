mana = (int(input("mana: ")))
feitico = (int(input("feitico: ")))
recupera = int(input("recupera: "))

dias = 0
fim = mana

while(fim > 0):
	fim = fim - feitico + recupera
	dias = dias + 1
print(dias)