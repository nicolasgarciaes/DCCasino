# Tarea 1: DCCasino :school_satchel:

## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:


#### Programación Orientada a Objetos: 38 pts (28%)
##### ✅ Diagrama <El diagrama posee, tanto las clases como su funcionalidd solicitada, junto con sus atributos y respectivos métodos.\>
##### ✅ Definición de clases, atributos, métodos y properties <Esta definida cada clase con sus atributos, métodos y properties en caso de ser necesario, tanto para casino, jugadores, juego y bebestibles.\>
##### ✅ Relaciones entre clases <Las clases se relacionan de buena manera, la Casino llama a cada una de ellas, y entre ellas tambien se relacionan de manera adecuada, adicionalmente, se definio como ABS a la clase bebestible y a las distintas personalidades como clases hijas de la clase padre jugador.\>
#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida <Se pueda crear más de una partida en el casino, se muestran a todos los jugadores con sus respectivos valores y se puede escoger a uno, luego estan todas las posibles acciones del menú, ya sea, jugador, comprar, ver habilidades y el show, tambien la opción de volver atras, en cada uno de los menús.\>
#### Acciones: 35 pts (26%)
##### ✅ Jugador <El jugador posee todas las acciones solicitadas, junto a algunas adicionales para el funcionamiento del código.\>
##### ✅ Juego <El juego posee todas las acciones solicitadas, junto a algunas adicionales para el funcionamiento del código. \>
##### ✅ Bebestible <Los bebestibles poseen todas las acciones solicitadas, junto a algunas adicionales para el funcionamiento del código.\>
##### ✅ Casino <El casino maneja todo el funcionamiento del código, posee todas sus acciones y algunas adicionales para el funcionamiento del código.>
#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio <El menú de inicio muestra la opción de salir o de inicar una partida.\>
##### ✅ Opciones de jugador <Se muestran todas las opciones que esten dentro del archivo jugadores.csv\>
##### ✅ Menú principal <El jugador tiene las opciones de jugar, comprar, ver habilidades, ver show, volver al menú anterior y salir.\>
##### ✅ Opciones de juegos <El jugador puede jugar todos los juegos dentro de la archivo juegos.csv, tambien volver al menú anterior y salir\>
##### ✅ Carta de bebestibles <Se le mostraran todos los bebestibles disponibles en el archivo bebestibles.csv junto con sus tipos y precios, podra comprar, volver al menú anterior y salir.\>
##### ✅ Ver estado del Jugador <Podra ver todas sus habilidades, junto con volver al menú anterior y salir.\>
##### ✅ Robustez <Los distintos menús son aprueba de cualquier input, en caso de error, se entrega otra oportunidad o se vuelve al menú anterior, esto esta a criterio del enunciado.\>
#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV  <Lee todos los archivos, independiente del orden en que vengan sus columnas, es decir, si viene nombre,personalidad o personalidad,nombre los lee bien\>
##### ✅ parametros.py <Estan integrados todos los parametros solicitados en el enunciado, junto con VALOR_DEUDA, la cual es el valor de la deuda del jugador.\>
#### Bonus: 3 décimas máximo
##### ✅ Ver Show <Al apretar la opción de ver Show, inmediatamente ingresa al Show, en caso de tener el dinero suficiente, y pierde el dinero pero gana los atributos.\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. El programa está modularizado, asi que, es importante tener en la misma carpeta que ```main.py```, los archivos ```clases_casino.py```, ```clases_bebestibles.py```, ```clases_juegos.py```, ```clases_jugadores.py```, ```archivos.py``` y ```parametros.py```
2. Adicionalmente, los archivos ```bebestibles.csv```, ```juegos.csv``` y ```jugadores.csv```, tambien deben estar en la misma carpeta que ```main.py``` 


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint() y random()```
2. ```tabulate```: ```tabulate()``` (debe instalarse)
3. ```abc```: ```ABC() y abstractmethod()```



### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clases_casino```: Contiene a ```Casino```
2. ```clases_bebestibles```: Contiene a ```Bebestible```, ```Jugo```, ```Gaseosa``` y ```Brebaje_magico```
3. ```clases_juegos```: Contiene a ```Juegos```
4. ```clases_jugadores```: Contiene a ```Jugador```, ```Tacano```, ```Bebedor```, ```Casual``` y ```Ludopata```
5. ```archivos```: Contiene a ```Archivos```Hecha para <Leer los archivos, ordenar la información y entregar las respectivas tablas que se printean>


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Supongo que la persona que ejecuta el código, sabe como funciona mas o menos el DCCasino, ya que no hay una explicación previa 1>


### Funcionamiento del código :sunglasses:

<En una primera instancia, se ejecuta Casino.menu_inicio(), en donde se entra a la función del menú inicio de Casino, y luego se pide un input para ver si quiere jugar o abandonar el juego, en caso de ingresar al juego, se lleva a Casino.opciones_jugador(), menú en el cual se printea una tabla con todas las opciones de jugadores con sus personalidades, se podrá, volver al menú anterior, salir del juego o seleccionar el jugador que se desee, posteriormente, se crea un Jugador, de acuerdo a su personalidad, con todos sus atributos provenientes del archivo.csv respectivo y se ingresa a Casino.menu_principal(jugador)>

<Ya en el menú principal, se entregan todas las opciones disponibles, si decide jugar, se printea la lista de juegos, junto con volver y salir, en caso de que elegir un juego, se muestra el dinero que posee, el dinero que le falta para pagar la deuda, los rangos de apuesta asociado al juego, en caso apostar un dinero válido, se calcula la probabilidad de ganar del juego asociado a ese juego, luego se calcula la probabilidad de ganar del juego y se compara con un número random(), si gana, se duplica el dinero apostado, y si pierde, pierde el dinero apostado, e independiente del resultado, puede suceder o no el evento especial, en caso de que suceda, se gana un bebestible al azar de todos los bebestibles disponibles y gana sus atributos, pero sin perder su dinero.

<En caso de que el jugador tenga 0 dinero, no podrá seguir jugando el juego, en caso de que posea dinero, pero no posea la energía suficiente, se le recomendará comprar un bebestible, en caso de poseer dinero, pero no energía y si el dinero es menor al bebestible más barato, no podrá seguir jugando y perderá el juego.>

<Es importante destacar, que las personalidades Casual y Ludopatia, cumplen con los requisitos del enunciado.>

<Al momento de elegir comprar un bebestible, podrá ver todos los bebestibles, con sus tipos y precio, si consume uno, se le aplican sus efectos con respecto a su personalidad, y pierde el dinero del valor del bebestible, también se podrá volver al menú o salir.>

<Si quiere ver sus habilidades, se printearan todas ellas, junto al valor restante para saldar la deuda, junto con volver al menú anterior y salir.>

<Si decide ver el Show, perderá el dinero del valor del show, pero ganará los atributos del show, cabe destacar que en el menú inicial, también se puede volver al menú anterior o salir.>