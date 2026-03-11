q0 = 1500
qf = 1042000
t = int(input("tempo? "))
i = float((qf/q0)**(1/t)-1)
print(round(i,5))