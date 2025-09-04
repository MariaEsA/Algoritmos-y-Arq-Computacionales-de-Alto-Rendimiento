x1 = int(input("Introduzca el valor 1:"))
x2 = int(input("Introduzca el valor 2:"))
if x1 > x2:
    lim = x1
else:
    if x2 > x1:
        lim = x2
    else:
        lim = x1
for i in range(x1 * x2, lim - 1, -1):
    if i % x1 == 0 and i % x2 == 0:
        mcm = i
print(mcm)
