import unittest
from app import CalculaGanador

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.calculador = CalculaGanador()

    def test_ganador_con_mas_del_50(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Aundrea Grace'])

    def test_segunda_vuelta(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '87654321', 'Eddie Hinesley', '1']
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Eddie Hinesley', 'Aundrea Grace'])

    def test_empate(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1']
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Eddie Hinesley'])

    def test_dni_invalido(self):
        data = [
            ['Áncash', 'Asunción', 'Acochaca', '1234567', 'Eddie Hinesley', '1'],  # DNI inválido
            ['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1']
        ]
        resultado = self.calculador.calcularganador(data)
        self.assertEqual(resultado, ['Aundrea Grace'])

if __name__ == '__main__':
    unittest.main()