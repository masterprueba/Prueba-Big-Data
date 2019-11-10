# PRUEBA Big Data
La prueba consiste en 3 ejercicios

### Primero

- 1.Cargar el archivo csv por medio de comandos dentro de Databricks Community.

Primero, cargo el archivo CSV y muestro los datos. 
![](http://img.fenixzone.net/i/JKAY43H.png)
![](http://img.fenixzone.net/i/3uG5aLd.png)

- 2.Extraer las columnas text y tweet_created

Capturo los dos campos con los que voy a trabajar y lo paso a DataFrame(pandas)
![](http://img.fenixzone.net/i/ZohsUym.png)

  - 3.Construir una nueva columna con los hashtags dentro del tweet.

  Con la libreria pandas y una expresion regular creo la nueva columna con los hashtags
![](http://img.fenixzone.net/i/5OSKkgy.png)

  - 4.Encontrar cuales son los 10 hashtags que más se utilizan

Elimino filas con datos nulos, realiza el conteo de los hashtag, ordeno y muestro los 10 hashtag mas utilizados
![](http://img.fenixzone.net/i/J10Hejw.png)
![](http://img.fenixzone.net/i/1NS9b3a.png)

### Segundo
Construir un script de python que permita simular los movimientos de todas las piezas de ajedrez dada una posición aleatoria dentro del tablero

- 2. Creo la funcion principal que determina cual es la posicion y la ficha a mostrar
- 3. Por cada pieza creo una funcion ya el comportamiento es distinto en cada uno 

### Tercero
Construir una clase en python que permita simular un objeto algebraico

- 1 [Operaciones] Clase abstracta para obligar a usar los siguientes metodos que necesita la clase principal
- 2 [OpPolinomial] Clase que implementa los metodos de la clase abstracta operaciones
- 3 [Polinomio] Clase entidad del polinomio que se le quito la responsabilidad de las operaciones a realizar
- 4 [ObjAlgrebraico] Clase principal
