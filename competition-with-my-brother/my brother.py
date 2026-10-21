while True :
    var1 = int(input(" Elige una opcion: >>> 1 para convertir de kelvin a cualquier grado, 2 para celcius a cualquier grado y 3 para farenheit a cualquier grado.. 4 para terminar <<< "))
    if var1 == 1:
        var2 = int(input(" 1 para kelvin a celcius y 2 para kelvin a farenheit "))
        if var2 == 1:
            var3 = float(input("Ingresa tus grados kelvin: "))
            var4 = var3 - 273.15
            print(" Tus grados son: " + str(var4))
        elif var2 == 2:
            var3 = float(input(" Ingresa tus grados kelvin: "))
            var4 = var3 - 273.15
            var5 = var4 * (9/5) + 32
            print(" Tus grados farenheit son: " + str(var5))
        else:
            print(" No valido ")
    elif var1 == 2:
        var2 = float(input(" 1 para celcius a kelvin y 2 para celcius a farenheit "))
        if var2 == 1:
            print(" Ingresa tus grados celcius: ")
            var3 = input(int)
            var4 = var3 + 273.15
            print(" Tus grados celcius son" + str(var4))
        elif var2 == 2:
            
            var3 = float(input(" Ingresa tus grados celcius: "))
            var4 = var3 + 273.15
            var5 = var4 * (9/5) + 32
            print(" Tus grados farenheit: son" + str(var5))
        else:
            print(" No valido ")

    elif var1 == 3:
        
        var2 = int(input(" 1 para farenheit a celcius y 2 para farenheit a kelvin "))
        if var2 == 1:
            var3 = float(input(" Ingresa tus grados farenheit: "))
            var4 = (var3 - 32) * (5/9)
            print(" Tus grados celcius son" + str(var4))
        elif var2 == 2:
            var3 = float(input(" Ingresa tus grados fahrenheit: "))
            var4 = (var3 - 32) * (5/9) + 273.15
            print(" Tus grados kelvin son: " + str(var4))
        else:
            print(" No valido ")
    elif var1 == 4:
        break
    else: 
        print(" No valido ")