# refactor-practice
Practica de refactor

Integrantes:
- Sebastian Tenorio
- Yoselyn Miranda
  
Descripción de la aplicación:

Es un programa que nos ayuda a convalidar los votos válidos de los candidatos en una región, si un candidato saco más del 50% de los votos totales sera el ganador de la votación, si dos candidatos empatan con el 50% será elegido el primero que aparezca en el archivo, sino se tomará a los dos candidatos que obtuvieron más votos para la segunda vuelta, tambien se hace una validación de los dnis de los votantes.

Pruebas Unitarias:

Se harán 4 pruebas unitarias:

| Test Case                           | Precondition                         | Test Steps                                                        | Test Data                      | Expected Result                                         |
|-------------------------------------|--------------------------------------|-------------------------------------------------------------------|-------------------------------|---------------------------------------------------------|
| Verificar la longitud de un dni| Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador |data =[ ['Áncash', 'Asunción', 'Acochaca', '1234567', 'Paula Daigle', '1'],['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1'],['Áncash', 'Asunción', 'Acochaca', '1237447', 'Paula Daigle', '1'],['Áncash', 'Asunción', 'Acochaca', '12345698', 'Aundrea Grace', '1'] ]| Voto no válido para el DNI: 1234567, Voto no válido para el DNI: 1237447,  ['Aundrea Grace'] |
| Verificar ganador con más del 50% de los votos | Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador | data = [['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'], ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'], ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']]| ['Aundrea Grace'] |
| Segunda vuelta | Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función calcularGanador|data = [['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],['Áncash', 'Asunción', 'Acochaca', '12345678', 'Aundrea Grace', '1'],['Áncash', 'Asunción', 'Acochaca', '87654321', 'Eddie Hinesley', '1'],['Áncash','Asunción', 'Acochaca', '87654321','Dennis Reyna','1']] |   ['Eddie Hinesley', 'Aundrea Grace']  |
| Empate | Se debe ingresar la data para el test.| Una vez ingresado la data se llamará a la función calcularGanador | data = [['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],['Áncash', 'Asunción', 'Acochaca', '86747322', 'Aundrea Grace', '1'],['Áncash', 'Asunción', 'Acochaca', '57538597', 'Eddie Hinesley', '1']] |   ['Eddie Hinesley']  |

Resultados de los casos de pruebas
