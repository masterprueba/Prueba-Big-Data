## PRUEBA Big Data

- 1.Cargar el archivo csv por medio de comandos dentro de Databricks Community.

Primero, cargo el archivo CSV y muestro los datos. 


- 2.Extraer las columnas text y tweet_created

Capturo los dos campos con los que voy a trabajar y lo paso a DataFrame(pandas)

  - 3.Construir una nueva columna con los hashtags dentro del tweet.

  Con la libreria pandas y una expresion regular creo la nueva columna con los hashtags

  - 4.Encontrar cuales son los 10 hashtags que más se utilizan

Elimino filas con datos nulos, realiza el conteo de los hashtag, ordeno y muestro los 10 hashtag mas utilizados