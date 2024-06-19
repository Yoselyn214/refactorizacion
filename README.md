# refactor-practice
Practica de refactor

Integrantes:
- Sebastian Tenoria
- Yoselyn Miranda
  
Descripción de la aplicación:

Es un programa que nos ayuda a convalidar los votos válidos de los candidatos en una región, si un candidato saco más del 50% de los votos totales sera el ganador de la votación, si dos candidatos empatan con el 50% será elegido el primero que aparezca en el archivo, sino se tomará a los dos candidatos que obtuvieron más votos para la segunda vuelta, tambien se hace una validación de los dnis de los votantes.

Pruebas Unitarias:

Se harán 4 pruebas unitarias:

| Test Case                           | Precondition                         | Test Steps                                                        | Test Data                      | Expected Result                                         |
|-------------------------------------|--------------------------------------|-------------------------------------------------------------------|-------------------------------|---------------------------------------------------------|
| Verificar la longitud de un dni| Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador | ("Lima","Peru"), ("Tokyo","Japan") |   Aproximadamente 15490.18 km  |
| Verificar ganador con más del 50% de los votos | Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador | ("Paris","France"), ("Lisbon","Portugal") |   Aproximadamente 1452.31 km  |
| Segunda vuelta | Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador| ("Paris","France"), ("Lisbon","Portugal") |   Aproximadamente 1452.31 km  |
| Empate | Se debe ingresar la data para el test.| Una vez ingresado la data se llamará a la función calcularGanador | ("Paris","France"), ("Lisbon","Portugal") |   Aproximadamente 1452.31 km  |
