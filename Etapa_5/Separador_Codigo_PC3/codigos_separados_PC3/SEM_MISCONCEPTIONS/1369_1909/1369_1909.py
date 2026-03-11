flawless = float(input())
soul = float(input())
dwarven = float(input())

Gr_flaw = flawless / 4.0
Gr_soul = soul / 3.14
Gr_dwar = dwarven / 10.0

Vr_porcao = min(Gr_flaw,Gr_soul,Gr_dwar)

print(int(Vr_porcao))