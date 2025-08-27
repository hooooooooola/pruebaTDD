import pytest
from unittest.mock import Mock, patch
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
    assert gestor.cacho_actual is None
    assert gestor.direccion is None


def test_determinar_cacho_inicial_sin_empate(mocker):
    """
    el cacho con el dado más alto inicia la partida
    """
    gestor = GestorPartida(3)
    
    # mocks para no usar testear con randoms 
    mock_dados = [3, 6, 4]  
    
    with patch('src.juego.gestor_partida.GeneradorAleatorio.generar_numero', side_effect=mock_dados): # use esto with patch con un mock para reemplazar los numeros random, no se si hay una mejor manera pero lo dejo asi por mientras :D
        # act
        cacho_inicial = gestor.determinar_cacho_inicial()
    
    # assert
    assert cacho_inicial == gestor.cacho_actual


def test_determinar_cacho_inicial_con_empate(mocker):
    """
    en caso de empate se vuelve a tirar dados solo para los empatados
    """
    # Arrange
    gestor = GestorPartida(2)
    
    # mock para randoms
    mock_dados = [5, 5, 2, 6] 
    
    with patch('src.juego.gestor_partida.GeneradorAleatorio.generar_numero', side_effect=mock_dados): # lo mismo por aca
        # act
        cacho_inicial = gestor.determinar_cacho_inicial()
    
    # assert
    assert cacho_inicial == gestor.cacho_actual

def test_establecer_direccion():
    """
    establecer la direccion de la partida
    """
    gestor = GestorPartida(2)
    
    # acts y asserts
    gestor.establecer_direccion("antihorario")
    assert gestor.direccion == "antihorario"
    gestor.establecer_direccion("horario")
    assert gestor.direccion == "horario"