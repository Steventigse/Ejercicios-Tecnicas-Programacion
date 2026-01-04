class Animal: # Clase Padre
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal): # Clase Hija que hereda de Animal
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Uso
mi_perro = Perro("Rex")
print(mi_perro.ladrar())