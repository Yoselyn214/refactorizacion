import csv

class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)  # Saltar la primera línea (encabezados)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(fila)
        return data

    def calcularganador(self, data):
        total_votos = 0
        votosxcandidato = {}
        orden_aparicion = []
        
        for fila in data:
            candidato = fila[4]
            esvalido = fila[5]
            dni = fila[3]

            # Verificar si el DNI es válido y es digito
            if len(dni) == 8 and dni.isdigit():
                if candidato not in votosxcandidato:
                    votosxcandidato[candidato] = 0
                    orden_aparicion.append(candidato)
                
                # Contar el voto si es válido
                if esvalido == '1':
                    votosxcandidato[candidato] += 1
                    total_votos += 1
            else:
                print(f"Voto no válido para DNI: {dni}")
        
        # Ordenar candidatos por cantidad de votos en orden descendente
        ordenado = sorted(votosxcandidato.items(), key=lambda item:item[1], reverse=True)

        # Calcular el ganador o los candidatos que pasan a segunda vuelta
        if len(ordenado) >= 2:
            primer_lugar, votos_primer = ordenado[0]
            segundo_lugar, votos_segundo = ordenado[1]

            #Ganador
            if votos_primer > total_votos / 2:
                return [primer_lugar]
            #Empate técnico del 50%, se trae al que aparecio primero en el archivo
            elif votos_primer == votos_segundo == total_votos / 2:
                if orden_aparicion.index(primer_lugar) < orden_aparicion.index(segundo_lugar):
                    return [primer_lugar]
                else:
                    return [segundo_lugar]
            #Se trae a los dos primeros candidatos que pasarán a la segunda vuelta y que no alcanzaron mas del 50%
            else:
                return [primer_lugar, segundo_lugar]
        else:
            return []

# Ejemplo de uso
c = CalculaGanador()

# Para probar con datos de ejemplo
datatest = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]

print(c.calcularganador(datatest))  # Debería imprimir : ['Aundrea Grace']

# Lo usaremos para probar con datos del archivo CSV
datos_csv = c.leerdatos()
print(c.calcularganador(datos_csv))
