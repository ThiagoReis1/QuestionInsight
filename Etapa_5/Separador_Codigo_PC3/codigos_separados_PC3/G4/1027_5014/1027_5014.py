kwh = 0.43;
vfx = 10.0;
icms = 1.25;

kwhM = float(input("Quantos kwh Meroveu consumiu em um mes?"));
total = (kwhM*kwh)+vfx;
total = total*icms;


print(round(total, 2));