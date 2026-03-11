t = int(input("tempo de investimento: "))
Q0 = 1500
Qf = 1042000
i = (Qf/Q0) ** (1/t) - 1
print(round(i,5))