
##- 1.Cargar el archivo csv por medio de comandos dentro de Databricks Community.

## Primero, cargo el archivo CSV y muestro los datos. 

import numpy as np
import pandas as pd
import collections

file_location = "/FileStore/tables/Tweets.csv"
file_type = "csv"

# Opciones
infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

# Leer Csv
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)


#### Spark SQL
#- 2.Extraer las columnas text y tweet_created

#Capturo los dos campos con los que voy a trabajar y lo paso a DataFrame(pandas)

df.createOrReplaceTempView("tweets")
sqlDF = spark.sql("SELECT text,tweet_created FROM tweets")
tweetsanddate = sqlDF.toPandas()


#### DataFrame
#- 3.Construir una nueva columna con los hashtags dentro del tweet.

#Con la libreria pandas y una expresion regular creo la nueva columna con los hashtags

tweetsanddate["hashtag"] = tweetsanddate.text.str.findall(r'@.*?(?=\s|$)')
tweetsanddate.head()


#### RDD
#- 4.Encontrar cuales son los 10 hashtags que más se utilizan

#Elimino filas con datos nulos, realiza el conteo de los hashtag, ordeno y muestro los 10 hashtag mas utilizados

total = np.array([], dtype="str")
for tw in tweetsanddate.hashtag:
  total = np.append(total,tw)
data_has = pd.DataFrame(total).reset_index()
data_has.columns = ['id','hashtag']
data_has = data_has.dropna()
data_has.head(5)
rdd_has = sc.parallelize(data_has.hashtag).filter(lambda x: x is not None)
d = rdd_has.countByValue()
ordered = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1],reverse=True))
diez_hashtag = pd.DataFrame(ordered, columns=ordered.keys(), index=[1])
diez_hashtag.T.head(10)

