from abc import ABC, abstractmethod

# Clase Abstracta: Es un molde, no puedes crear un "Vehiculo" genérico
class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

# Clase Concreta: Aquí sí defines cómo se enciende
class Auto(Vehiculo):
    def encender(self):
        return "El auto ha encendido con llave electrónica."

# Uso
mi_auto = Auto()
print(mi_auto.encender())