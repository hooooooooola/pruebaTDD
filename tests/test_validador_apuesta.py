from src.juego.validador.apuesta import ValidadorApuesta

def test_validador_apuesta():
    validador = ValidadorApuesta()
    assert validador.validar_apuesta(100) == True
    assert validador.validar_apuesta(0) == False