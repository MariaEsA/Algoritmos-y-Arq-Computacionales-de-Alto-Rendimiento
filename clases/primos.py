m = int(input("por favor, introduzca el valor a revisar:"))
for n in range(2, m + 1): 
    divisores = 0
    i= 2
    while i < n : 
        if n % i == 0 :
            divisores = divisores + 1
        i = i + 1
    if divisores == 0 :
        print (f"{n},",end="")
    #else : 
    #    print("No es primo")
