import random

moustro = 100
vida = 100
player = input("como deseas llamar? ")
print("hola", player,"estas peleando contra moustro.png")

while True:
    descicion = int(input(f"tienes {vida} de vida que haras? 1=Atacar, 2=Curarse, 3=Huir "))
    if descicion not in (1, 2, 3):
        print("invalido chaval")
    elif descicion == 1:
        probabilidad1 = random.randint(0, 100)
        if probabilidad1 >= 80:
            moustro = moustro - random.randint(10, 20)
            print("se ha quedado", moustro,"de vida tio")
        else:
            print("haz fallado el golpe")
        probabilidad3= random.randint(0, 100)
        if moustro > 0:
            if probabilidad3 >= 80:
                print("pero el moustro te ha contraatacado")
                vida = vida - random.randint(10,20)
    elif descicion == 2:
        vida = vida + random.randint(5,12)
        if vida >= 100:
            vida = 100
        probabilidad2= random.randint(0, 100)
        if moustro > 0:
            if probabilidad2 >= 50:
                daño_monstruo = random.randint(7, 15)
                vida = vida - daño_monstruo
                print(f"pero el moustro te ha contraatacado y te quito {daño_monstruo} de vida. Te queda {vida} de vida.")
    elif descicion == 3:
        print("te has ido de alli como un maricon...")
        exit()
    if vida <= 0:
        print("haz perdido")
        exit()
    if moustro <= 0:
        print("GG haz ganado")
        exit()