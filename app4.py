import csv

# Técnica 5: Se dividió el código en diferentes métodos.
class LectorDatos:
    # Extracción de clases: se crea una clase separada para manejar la lectura de los datos
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_archivo(self):
        data = []
        with open(self.archivo, 'r') as csvfile:
            next(csvfile)  # Saltar la primera línea (encabezados)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

class CalculadorVotos:
    def __init__(self):
        self.total_votos = 0
        self.votosxcandidato = {}
        self.orden_aparicion = []

    # Técnica 1: Extracción de métodos: se crea un método para la validación del DNI (ver si tiene 8 dígitos).
    def es_dni_valido(self, dni):
        return len(dni) == 8 and dni.isdigit()

    # Extracción de métodos: se crea un método para el conteo de los votos y actualizar nuestros contadores.
    def contar_voto(self, fila):
        # Técnica 2: Renombrar variables: se utilizan nombres de variables más descriptivos para un mejor entendimiento.
        candidato = fila[4]
        esvalido = fila[5]
        dni = fila[3]

        if self.es_dni_valido(dni):
            if candidato not in self.votosxcandidato:
                self.votosxcandidato[candidato] = 0
                self.orden_aparicion.append(candidato)
            if esvalido == '1':
                self.votosxcandidato[candidato] += 1
                self.total_votos += 1
        else:
            print(f"Voto no válido para el DNI: {dni}")

    def calcular_ganador(self):
        # Técnica 3: Simplificación de condicionales: se van a simplificar las condiciones para definir quién es el ganador.

        # Ordenar candidatos por cantidad de votos en orden descendente
        ordenado = sorted(self.votosxcandidato.items(), key=lambda item: item[1], reverse=True)
        
        if len(ordenado) >= 2:
            primer_lugar, votos_primer = ordenado[0]
            segundo_lugar, votos_segundo = ordenado[1]

            # Ganador
            if votos_primer > self.total_votos / 2:
                return [primer_lugar]
            # Empate técnico del 50%, se trae al que apareció primero en el archivo
            elif votos_primer == votos_segundo == self.total_votos / 2:
                if self.orden_aparicion.index(primer_lugar) < self.orden_aparicion.index(segundo_lugar):
                    return [primer_lugar]
                else:
                    return [segundo_lugar]
            # Se trae a los dos primeros candidatos que pasarán a la segunda vuelta y que no alcanzaron más del 50%
            else:
                # Encontrar todos los candidatos con los dos votos más altos
                return [primer_lugar,segundo_lugar]
        elif len(ordenado) == 1:
            return [ordenado[0][0]]
        else:
            return []

class CalculaGanador:
    # Técnica 4: Extracción de clases: se crea una clase principal para manejar la lógica completa.
    def __init__(self, archivo):
        self.lector = LectorDatos(archivo)
        self.calculador = CalculadorVotos()

    def ejecutar(self):
        datos = self.lector.leer_archivo()
        for fila in datos:
            self.calculador.contar_voto(fila)
        return self.calculador.calcular_ganador()

# Ejemplo de uso
c = CalculaGanador('0204.csv')

# Para probar con datos de ejemplo
datatest = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]

# Probar con datos de ejemplo
calculador_prueba = CalculaGanador('')
calculador_prueba.calculador.votosxcandidato = {}
calculador_prueba.calculador.total_votos = 0
calculador_prueba.calculador.orden_aparicion = []
for fila in datatest:
    calculador_prueba.calculador.contar_voto(fila)
print(calculador_prueba.calculador.calcular_ganador())  # Debería imprimir: ['Aundrea Grace']

# Probar con datos del archivo CSV
print(c.ejecutar())

