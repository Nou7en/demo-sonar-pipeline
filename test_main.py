from main import calcular

def test_calcular_suma():
    resultado = calcular(2, 3)
    assert resultado == 5