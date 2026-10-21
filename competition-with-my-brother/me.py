print("Elije que quieres convertir")
numero1 = int(input("1.Celcius 2.Farengay 3. Kelvin: "))

if numero1 not in (1, 2, 3):
    print ("Invalido")
    exit()

print("A que unidad quieres convertir?")
numero2 = int(input("1. Celsius | 2. Farengay | 3. Kelvin: "))
if numero2 not in (1, 2, 3):
    print("Invalido")
    exit()

if numero1 == numero2:
    print("Invalido")
    exit()

valor = float(input("Ingresa el numero que quieres convertir: "))

if numero1 == 1 and numero2 == 2:
    coso1 = (valor * 9/5) +32
    print(valor, "Celcius equivale a", coso1, "Farengay")
    exit()
if numero1 == 1 and numero2 == 3:
    coso2 = (valor + 273.15) 
    print(valor, "Celcius equivale a", coso2, "Kelvin")
    exit()
if numero1 == 2 and numero2 == 1:
    coso3 = (valor - 32) / 1.8
    print(valor, "Farengay equivale a", coso3, "Celsius")
    exit()
if numero1 == 2 and numero2 == 3:
    coso4 = (valor - 32) / 1.8 + 273.15
    print(valor, "Farengay equivale a", coso4, "Kelvin")
    exit()
if numero1 == 3 and numero2 == 1:
    coso5 = (valor - 273.15)
    print(valor, "Kelvin equivale a", coso5, "Celcius")
    exit()
if numero1 == 3 and numero2 == 2:
    coso6 = ((valor - 273.15) * 1.8) + 32
    print(valor, "Kelvin equivale a", coso6, "Farengay")
    exit()