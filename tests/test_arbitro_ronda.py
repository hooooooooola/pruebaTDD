import pytest
from unittest.mock import Mock
from src.juego.arbitro_ronda import ArbitroRonda


def test_dudar_incorrecto(mocker):
    """
    cuando hay igual o mas dados de los apostados el dudador pierde un dado
    """
    arbitro = ArbitroRonda()
    
    # mock contador de pintas en 3 
    mock_contador = mocker.patch('src.juego.arbitro_ronda.ContadorPintas')
    mock_contador.contar.return_value = 3
    
    # mocks de cachos
    cacho_apostador = Mock()
    cacho_apostador.dados = [1, 2, 3, 4, 5]  
    cacho_dudador = Mock()
    cacho_dudador.dados = [1, 2, 3, 4, 5]   
    
    apuesta = {"cantidad": 3, "pinta": 4}
    cachos = [cacho_apostador, cacho_dudador]
    
    # act y asserts
    resultado = arbitro.resolver_duda(apuesta, cacho_apostador, cacho_dudador, cachos)
    assert resultado == 0 
    cacho_dudador.perder_dado.assert_called_once()
    cacho_apostador.perder_dado.assert_not_called()


def test_dudar_correcto(mocker):
    """
    cuando hay menos dados de los apostados el apostador pierde un dado
    """
    arbitro = ArbitroRonda()
    
    # mock contador de pintas en 2
    mock_contador = mocker.patch('src.juego.arbitro_ronda.ContadorPintas')
    mock_contador.contar.return_value = 2
    
    # mocks de cachos
    cacho_apostador = Mock()
    cacho_apostador.dados = [1, 2, 3, 4, 5]
    cacho_dudador = Mock()
    cacho_dudador.dados = [1, 2, 3, 4, 5]
    
    apuesta = {"cantidad": 3, "pinta": 4}
    cachos = [cacho_apostador, cacho_dudador]
    
    # act y asserts
    resultado = arbitro.resolver_duda(apuesta, cacho_apostador, cacho_dudador, cachos)
    assert resultado == 1
    cacho_apostador.perder_dado.assert_called_once()
    cacho_dudador.perder_dado.assert_not_called()

def test_calzar_incorrecto(mocker):
    """
    cuando un jugador calza incorrectamente pierde un dado
    """
    arbitro = ArbitroRonda()
    
    # mock del contador para que no sea exacto
    mock_contador = mocker.patch('src.juego.arbitro_ronda.ContadorPintas')
    mock_contador.contar.return_value = 3  
    
    # mocks de cachos
    cacho_calzador = Mock()
    cacho_calzador.cantidad_dados.return_value = 3
    cacho_calzador.perder_dado = Mock()
    
    apuesta = {"cantidad": 4, "pinta": 5}
    cachos = [cacho_calzador, Mock(), Mock()]
    
    # act y asserts
    resultado = arbitro.resolver_calce(apuesta, cacho_calzador, cachos)
    assert resultado == 0
    cacho_calzador.perder_dado.assert_called_once()

def test_calzar_correcto(mocker):
    """
    cuando un jugador calza exactamente gana un dado
    """
    arbitro = ArbitroRonda()
    
    # mock del contador para que sea exacto 
    mock_contador = mocker.patch('src.juego.arbitro_ronda.ContadorPintas')
    mock_contador.contar.return_value = 4  
    
    # mocks de cachos
    cacho_calzador = Mock()
    cacho_calzador.cantidad_dados.return_value = 3  
    cacho_calzador.ganar_dado = Mock()
    
    apuesta = {"cantidad": 4, "pinta": 5}
    cachos = [cacho_calzador, Mock(), Mock()] 
    
    # act y asserts
    resultado = arbitro.resolver_calce(apuesta, cacho_calzador, cachos)
    assert resultado == 1   
    cacho_calzador.ganar_dado.assert_called_once()