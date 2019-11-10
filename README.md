# PRUEBA Big Data
La prueba consiste en 3 ejercicios

### Primero

- 1.Cargar el archivo csv por medio de comandos dentro de Databricks Community.

Primero, cargo el archivo CSV y muestro los datos. 
![](https://drive.google.com/open?id=1seOtKeG4RY1p_x32keMELnw3VYS_4EEV)
![](https://drive.google.com/open?id=1aE_xca1TPcglXZrc2IIyQcKQ2F5gvPux)

- 2.Extraer las columnas text y tweet_created

Capturo los dos campos con los que voy a trabajar y lo paso a DataFrame(pandas)
![](https://drive.google.com/open?id=17hs-AhxE9c7otxlhBfxRQKazTzOMmeEC)

  - 3.Construir una nueva columna con los hashtags dentro del tweet.

  Con la libreria pandas y una expresion regular creo la nueva columna con los hashtags
![](https://drive.google.com/open?id=1N7MenW5XLowU_gOu6WWJFZ6tnqvYUsg-)

  - 4.Encontrar cuales son los 10 hashtags que más se utilizan

Elimino filas con datos nulos, realiza el conteo de los hashtag, ordeno y muestro los 10 hashtag mas utilizados
![](https://drive.google.com/open?id=1xJhmUbEkv-TT-L_fZ0DHq2kjto0OQ0CH)
![](https://drive.google.com/open?id=1Ev9qRUK-uEgH2XPYywSNaP4Pw284y65k)

### Segundo
Construir un script de python que permita simular los movimientos de todas las piezas de ajedrez dada una posición aleatoria dentro del tablero

-2. Creo la funcion principal que determina cual es la posicion y la ficha a mostrar
-3. Por cada pieza creo una funcion ya el comportamiento es distinto en cada uno 

### Tercero
Construir una clase en python que permita simular un objeto algebraico

-1 [Operaciones] Clase abstracta para obligar a usar los siguientes metodos que necesita la clase principal
-2 [OpPolinomial] Clase que implementa los metodos de la clase abstracta operaciones
-3 [Polinomio] Clase entidad del polinomio que se le quito la responsabilidad de las operaciones a realizar
-4 [ObjAlgrebraico] Clase principal
