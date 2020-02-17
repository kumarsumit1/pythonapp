from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

spark = SparkSession.builder.appName("Spark-SQL-Basic").getOrCreate()

stockPriceInputDir = "data/stock_prices"
stockPriceDirtyInputDir = "data/stock_prices_dirty"
stockInfoInputDir = "data/stock_info"

stockPriceSchema = StructType([\
        StructField("stockId", IntegerType()),\
        StructField("timeStamp", IntegerType()), \
        StructField("stockPrice", DoubleType())\
    ])

stockInfoSchema = StructType([\
        StructField("stockId", IntegerType()),\
        StructField("stockName", StringType()), \
        StructField("stockCategory", StringType())\
    ])



stockPriceInput = spark.read.format("csv").option("header","true").schema(stockPriceSchema).load(stockPriceInputDir)
stockPriceInput.registerTempTable("stockPrice")
stockPriceDirtyInput = spark.read.format("csv").option("header","true").schema(stockPriceSchema).load(stockPriceDirtyInputDir)
stockPriceDirtyInput.registerTempTable("stockPriceDirty")
stockInfoInput = spark.read.format("csv").option("header","true").schema(stockInfoSchema).load(stockInfoInputDir)
stockInfoInput.registerTempTable("stockInfo")

print(stockPriceInput.show())
print(stockPriceInput.printSchema())


#print(stockInfoInput.show())
#print(stockInfoInput.printSchema())

#Task 1:
# Compute the moving average for every stockID with a predefined moving window size

# Window Size : 3 <
# ===Output Data== 
# _Columns_: stockId,timeStamp,stockPrice,moving_average 
# _Ordered by_: stockId,timeStamp

movingAverage = spark.sql("select stockId,timeStamp,stockPrice, avg(stockPrice) over( PARTITION BY stockId ORDER BY stockId,timeStamp ROWS BETWEEN 2 PRECEDING AND 0 FOLLOWING ) as moving_average from stockPrice")

print(movingAverage.show())

# _Task 1 :_ Count of each files
#  Load all the above files as spark dataframes and print the count of each of files.




# Task 2:
# Join with Projection - Join moving average calculated in Task1 with the stockInfo. ​ 

# Window Size : 3 
# ===Output Data== 
# _Columns_: stockId,timeStamp,stockPrice,moving_average,stockName,stockCategory

projection = movingAverage.join(stockInfoInput, movingAverage.stockId == stockInfoInput.stockId)\
              .select("stockPrice.stockId","timeStamp","stockPrice","moving_average","stockName","stockCategory")

print(projection.show())

# _Task 2 :_ Handle Nulls
# File : test/resources/input/stock_prices_dirty/0.csv
#  contains null values in amount column. Replace those null values with mean of column in spark dataframe.





# Task 3:
# Get the projected moving average data for a given stockId

# stockId :103 
# ===Output Data== 
# _Columns_:stockId,timeStamp,stockPrice,moving_average,stockName,stockCategory 

filterData=projection.filter(projection.stockId == 103)

print(filterData.show())

# _Task 3 :_ Add a Sequential Row ID
# For a joined dataframe, add an id column which contains sequence numbers from 1 to number of rows




# Task 4:
# Handle Nulls 
# File : data/stock_prices_dirty/0.csv 
# contains null values in stockPrice column.

# Filter all the non null rows 
# Columns: stockId,timeStamp,stockPrice

print(stockPriceDirtyInput.show())
print(stockPriceDirtyInput.printSchema())
nonNull= spark.sql("select * from stockPriceDirty where stockPrice is not null")
print(nonNull.show())


# _Task 4 :_ Sales with 5% Discount
# Add a column ​discount_amount​ to joined dataframe, which holds 5% discounted amount.