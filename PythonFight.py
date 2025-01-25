class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.inventario = []
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def usar_pocima(self, tipo):
        if tipo == "vida":
            cantidad = int(input("¿Cuántos puntos de vida deseas restaurar? "))
            self.vida += cantidad
            print(self.nombre, "ha restaurado", cantidad, "puntos de vida.")
        elif tipo == "fuerza":
            self.fuerza += self.fuerza * 0.5
            print(self.nombre, "ha aumentado su fuerza en un 50%. Nueva fuerza:", self.fuerza)
        elif tipo == "inteligencia":
            self.inteligencia += self.inteligencia * 0.5
            print(self.nombre, "ha aumentado su inteligencia en un 50%. Nueva inteligencia:", self.inteligencia)
        else:
            print("Pócima desconocida.")

    def agregar_pocima(self, tipo):
        self.inventario.append(tipo)
        print(self.nombre, "ha agregado una pócima de tipo", tipo, "a su inventario.")

    def recibir_ataque(self, daño):
        if daño < self.defensa:
            print(self.nombre, "ha bloqueado el daño con su defensa.")
        else:
            daño_restante = daño - self.defensa
            self.vida -= daño_restante
            print(self.nombre, "ha recibido", daño_restante, "puntos de daño.")

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada, escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo  
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)
        print("·Escudo:", self.escudo)
        print("·Vida del escudo:", self.vida_escudo)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

    def recibir_ataque(self, daño):
        if daño < self.vida_escudo:
            self.vida_escudo -= daño
            print(self.nombre, "ha absorbido todo el daño con su escudo.")
        elif daño == self.vida_escudo:
            self.vida_escudo = 0
            print(self.nombre, "ha perdido su escudo.")
        else:
            daño_restante = daño - self.vida_escudo
            self.vida_escudo = 0
            self.vida -= daño_restante
            print(self.nombre, "ha perdido su escudo y ha recibido", daño_restante, "puntos de daño.")

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

    def recibir_ataque(self, daño):
        if daño < self.defensa:
            print(self.nombre, "ha bloqueado el daño con su defensa.")
        else:
            daño_restante = daño - self.defensa
            self.vida -= daño_restante
            print(self.nombre, "ha recibido", daño_restante, "puntos de daño.")

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre,":", sep="")
        daño_1 = jugador_1.daño(jugador_2)
        jugador_2.recibir_ataque(daño_1)
        print(">>> Acción de ", jugador_2.nombre,":", sep="")
        daño_2 = jugador_2.daño(jugador_1)
        jugador_1.recibir_ataque(daño_2)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Crear personajes
personaje_1 = Guerrero("McLovin", 20, 10, 14, 100, 4, 2)  # Guerrero con escudo
personaje_2 = Mago("MrGraso", 20, 45, 7, 100, 3)  # Mago

# Crear lista de personajes
personajes = [
    Guerrero("Merlin", 20, 15, 10, 100, 4, 2),
    Guerrero("Lancelot", 25, 10, 12, 80, 3, 1),
    Guerrero("Houdini", 30, 20, 15, 100, 5, 3)
]

# Ejercicio 1: Encontrar el personaje con más vida
personaje_mas_vida = max(personajes, key=lambda p: p.vida)
print(f"El personaje con más vida es {personaje_mas_vida.nombre} con {personaje_mas_vida.vida} puntos de vida.")

# Ejercicio 2: Calcular la suma total de inteligencia
total_inteligencia = sum(p.inteligencia for p in personajes)
print(f"La inteligencia total de los personajes es: {total_inteligencia}")

# Ejercicio 3: Encontrar personajes con vida mayor a un valor específico
valor_vida = int(input("Introduce el valor de vida: "))
personajes_filtrados = [p for p in personajes if p.vida > valor_vida]

if personajes_filtrados:
    print(f"Los personajes con vida mayor a {valor_vida} son:")
    for p in personajes_filtrados:
        print(f"- {p.nombre}: {p.vida} puntos de vida")
else:
    print(f"No hay personajes con vida mayor a {valor_vida}.")

# Mostrar atributos iniciales
personaje_1.atributos()
personaje_2.atributos()      

# Agregar pócimas al inventario
personaje_1.agregar_pocima("vida")
personaje_1.agregar_pocima("fuerza")
personaje_2.agregar_pocima("inteligencia")

# Usar pócimas
personaje_1.usar_pocima("vida")
personaje_2.usar_pocima("fuerza")

# Iniciar combate
combate(personaje_1, personaje_2)