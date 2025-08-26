from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:

    def resolver_duda(self, apuesta, cacho_apostador, cacho_dudador, cachos):
        cantidad_apostada = apuesta["cantidad"]
        pinta_apostada = apuesta["pinta"]
        
        total = ContadorPintas.contar(cachos, pinta_apostada)
        
        if total >= cantidad_apostada:
            cacho_dudador.perder_dado()
            return 0
        else:
            cacho_apostador.perder_dado()
            return 1

    def resolver_calce(self, apuesta, cacho_calzador, cachos):
        cantidad_apostada = apuesta["cantidad"]
        pinta_apostada = apuesta["pinta"]
        
        total = ContadorPintas.contar(cachos, pinta_apostada)
        
        if total == cantidad_apostada:  
            cacho_calzador.ganar_dado()
            return 1
        else:
            cacho_calzador.perder_dado()
            return 0

    def puede_calzar(self, cacho_calzador, cachos):
        """
        puede calzar si: 
        - si tiene solo un dado
        - si hay la mitad o mas de dados iniciales en juego
        """
        # un dado
        if cacho_calzador.cantidad_dados() == 1:
            return True
        
        # mitad de los dados (dados actuales >= cachos*5 / 2)
        return sum(cacho.cantidad_dados() for cacho in cachos) >= len(cachos) * 5 / 2
