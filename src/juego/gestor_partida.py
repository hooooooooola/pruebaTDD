from src.juego.cacho import Cacho

class GestorPartida:
    def __init__(self, cantidad_jugadores):
        self.cachos = [Cacho() for _ in range(cantidad_jugadores)]
        self.cacho_actual = None
        self.direccion = None
    
    