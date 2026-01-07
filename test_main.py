from main import calcular

def test_calcular_suma():
    # Hacemos un test simple para generar cobertura
    resultado = calcular(2, 3)
    assert resultado == 5