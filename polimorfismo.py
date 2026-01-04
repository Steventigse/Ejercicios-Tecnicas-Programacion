class Gato:
    def sonido(self):
        return "Miau"

class Vaca:
    def sonido(self):
        return "Muuu"

# Función que demuestra polimorfismo: acepta cualquier objeto que tenga el método 'sonido'
def hacer_ruido(animal):
    print(animal.sonido())

# Uso
gato = Gato()
vaca = Vaca()
hacer_ruido(gato)
hacer_ruido(vaca)