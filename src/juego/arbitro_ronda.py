from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:

    def resolver_duda(self, apuesta, cacho_apostador, cacho_dudador, todos_los_cachos):
        cantidad_apostada = apuesta["cantidad"]
        pinta_apostada = apuesta["pinta"]
        
        total = ContadorPintas.contar(todos_los_cachos, pinta_apostada)
        
        if total >= cantidad_apostada:
            cacho_dudador.perder_dado()
            return 0
        else:
            cacho_apostador.perder_dado()
            return 1