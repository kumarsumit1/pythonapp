from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

spark = SparkSession.builder.appName("Spark-SQL-Basic").getOrCreate()

stockPriceInputDir = "data/stock_prices/2.csv"

stockPriceSchema = StructType([\
        StructField("stockId", IntegerType()),\
        StructField("timeStamp", IntegerType()), \
        StructField("stockPrice", DoubleType())\
    ])

stockPriceInput = spark.read.format("csv").option("header","true").schema(stockPriceSchema).load(stockPriceInputDir)
stockPriceInput.registerTempTable("stockPrice")

print(stockPriceInput.show())
print(stockPriceInput.printSchema())

movingAverage = spark.sql("select stockId,timeStamp,stockPrice, avg(stockPrice) over( PARTITION BY stockId ORDER BY timeStamp RANGE BETWEEN 1 PRECEDING  AND 2 FOLLOWING) as moving_average from stockPrice")

print(movingAverage.show())

print(spark.sparkContext.version)