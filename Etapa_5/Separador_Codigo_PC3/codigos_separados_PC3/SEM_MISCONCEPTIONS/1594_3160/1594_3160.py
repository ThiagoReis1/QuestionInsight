from numpy import*
vetordedanos= array([x,y,z])
print(vetordedanos)
vetordedanos[x] = vetordedanos[x]*peso1
vetordedanos[y] = vetordedanos[y]*vetordedanos[x] + 1.0
vetordedanos[z] = vetordedanos[z]*vetordedanos[y] + 1.0
danototal = vetordedanos[x]+ vetordedanos[y] + vetordedanos[z]
print(danototal)
