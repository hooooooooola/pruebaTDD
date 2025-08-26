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

def test_calzar_mas_mitad_dados(mocker):
    """
    se puede calzar cuando hay la mitad o mas de dados iniciales en juego
    """
    arbitro = ArbitroRonda()
    
    # mock cacho calzador con 3 dados
    cacho_calzador = Mock()
    cacho_calzador.cantidad_dados.return_value = 3
    
    # mocks de cachos
    otros_cachos = [Mock(), Mock()]
    otros_cachos[0].cantidad_dados.return_value = 2
    otros_cachos[1].cantidad_dados.return_value = 4
    
    cachos = [cacho_calzador] + otros_cachos
    
    # act -- 9 dados actuales >= 7.5 (mitad de 15)
    puede_calzar = arbitro.puede_calzar(cacho_calzador, cachos)
    
    # assert
    assert puede_calzar == True


def test_calzar_menos_mitad_dados(mocker):
    """
    no se puede calzar cuando hay menos de la mitad de dados iniciales
    """
    arbitro = ArbitroRonda()
    
    # mock cacho calzador con 2 dados
    cacho_calzador = Mock()
    cacho_calzador.cantidad_dados.return_value = 2
    
    otros_cachos = [Mock(), Mock()]
    otros_cachos[0].cantidad_dados.return_value = 2
    otros_cachos[1].cantidad_dados.return_value = 2
    
    cachos = [cacho_calzador] + otros_cachos
    
    # act -- 6 dados actuales < 7.5 (mitad de 15)
    puede_calzar = arbitro.puede_calzar(cacho_calzador, cachos)
    
    # assert
    assert puede_calzar == False


def test_calzar_solo_un_dado(mocker):
    """
    se puede calzar cuando el jugador solo tiene un dado
    """
    arbitro = ArbitroRonda()
    
    # mock dado calzador
    cacho_calzador = Mock()
    cacho_calzador.cantidad_dados.return_value = 1  # Solo un dado
    
    cachos = [cacho_calzador, Mock(), Mock()]
    
    # act y assert
    puede_calzar = arbitro.puede_calzar(cacho_calzador, cachos)
    assert puede_calzar == True
