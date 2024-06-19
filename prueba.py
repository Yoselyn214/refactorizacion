import unittest
from app4 import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        # Pasamos un archivo vacío o ficticio
        self.calculador = CalculaGanador('')

    def test_ganador_con_mas_del_50(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        for fila in data:
            self.calculador.calculador.contar_voto(fila)
        resultado = self.calculador.calculador.calcular_ganador()
        
        print(f"Resultado esperado: ['Aundrea Grace'], Resultado obtenido: {resultado}")
        self.assertEqual(resultado, ['Aundrea Grace'])
        print("test_ganador_con_mas_del_50 pasó correctamente.")
        print("\n")

    def test_segunda_vuelta(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '87654321', 'Eddie Hinesley', '1'],
            ['Áncash','Asunción', 'Acochaca', '87654321','Dennis Reyna','1']
        ]
        for fila in data:
            self.calculador.calculador.contar_voto(fila)
        resultado = self.calculador.calculador.calcular_ganador()
        print(f"Resultado esperado: ['Eddie Hinesley', 'Aundrea Grace'], Resultado obtenido: {resultado}")
        self.assertEqual(resultado, ['Eddie Hinesley', 'Aundrea Grace'])
        print("test_segunda_vuelta pasó correctamente.")

    def test_empate(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86747322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57538597', 'Eddie Hinesley', '1']
        ]
        for fila in data:
            self.calculador.calculador.contar_voto(fila)
        resultado = self.calculador.calculador.calcular_ganador()
        #print(resultado)
        print(f"Resultado esperado: ['Eddie Hinesley'], Resultado obtenido: {resultado}")
        self.assertEqual(resultado, ['Eddie Hinesley'])
        print("test_empate pasó correctamente.")
        print("\n")

    def test_dni_invalido(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '1234567', 'Paula Daigle', '1'],  # DNI inválido
            ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '1237447', 'Paula Daigle', '1'], #DNI inválido
            ['Áncash', 'Asunción', 'Acochaca', '12345698', 'Aundrea Grace', '1']
        ]
        for fila in data:
            self.calculador.calculador.contar_voto(fila)
        resultado = self.calculador.calculador.calcular_ganador()
        #print(resultado)
        print(f"Resultado esperado: ['Aundrea Grace'], Resultado obtenido: {resultado}")
        self.assertEqual(resultado, ['Aundrea Grace'])
        print("test_dni_invalido pasó correctamente.")
        print("\n")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculaGanador)
    result = unittest.TextTestRunner().run(suite)
    if result.wasSuccessful():
        print("Todas las pruebas pasaron correctamente.")
