# Estrategia para conductores
class ConductorStrategy:
    def calcular_ruta(self, origen, destino):
        print(f"Calculando ruta para conductor desde {origen} hasta {destino} basada en el tiempo.")

# Estrategia para peatones
class PeatonStrategy:
    def calcular_ruta(self, origen, destino):
        print(f"Calculando ruta para peatón desde {origen} hasta {destino} basada en la distancia.")

class NavegacionContexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular_ruta(self, origen, destino):
        self.estrategia.calcular_ruta(origen, destino)

# Código principal
if __name__ == "__main__":
    tipo_usuario = input("¿Eres conductor o peatón? ").lower()

    if tipo_usuario == "conductor":
        estrategia = ConductorStrategy()
    elif tipo_usuario == "peatón":
        estrategia = PeatonStrategy()
    else:
        print("Tipo de usuario no válido.")
        exit()

    origen = input("Ingrese el punto de origen: ")
    destino = input("Ingrese el punto de destino: ")

    # Creamos el contexto con la estrategia seleccionada y calculamos la ruta
    contexto = NavegacionContexto(estrategia)
    contexto.calcular_ruta(origen, destino)