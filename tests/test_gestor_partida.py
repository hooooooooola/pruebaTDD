from src.juego.gestor_partida import GestorPartida

def test_crear_partida_con_cachos():
    """
    crear una partida con cachos como jugadores
    """
    cantidad_jugadores = 3
    
    # act y asserts
    gestor = GestorPartida(cantidad_jugadores)
    assert len(gestor.cachos) == 3
    for cacho in gestor.cachos:
        assert cacho.cantidad_dados() == 5
    assert gestor.cacho_actual == None
    assert gestor.cacho_actual is None
    assert gestor.direccion is None