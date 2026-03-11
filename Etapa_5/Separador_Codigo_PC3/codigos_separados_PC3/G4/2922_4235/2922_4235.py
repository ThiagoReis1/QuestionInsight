tempo = int(input("tempo: "))
Qo = 1500
Qf = 1042000
i = float((Qf/Qo)**(1/tempo)-1)
print(round(i, 5))