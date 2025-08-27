from src.juego.cacho import Cacho
from src.juego.dado import Dado
from src.servicios.generador_aleatorio import GeneradorAleatorio


class GestorPartida:
    def __init__(self, cantidad_jugadores):
        self.cachos = [Cacho() for _ in range(cantidad_jugadores)]
        self.cacho_actual = None
        self.direccion = None
    
    def determinar_cacho_inicial(self):
        cachos_participantes = self.cachos.copy()  
        
        # mientras no haya un ganador
        while True:
            valores = []
            for cacho in cachos_participantes:
                valor = GeneradorAleatorio.generar_numero(1, 6)
                valores.append((cacho, valor))
            
            # valor mas alto sacado
            max_valor = max(valores, key=lambda x: x[1])[1]
            ganadores = [cacho for cacho, valor in valores if valor == max_valor]
            
            # no hay empate
            if len(ganadores) == 1:
                self.cacho_actual = ganadores[0]
                return ganadores[0]
            
            # empate (solo los empatados siguen participando)
            cachos_participantes = ganadores