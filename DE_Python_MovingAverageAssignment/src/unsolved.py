from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

class MovingAverage:
    spark = None
    stockPriceInputDir = None
    size = 0
    def __init__(self, spark, stockPriceInputDir,size):
        self.spark = spark
        self.stockPriceInputDir = stockPriceInputDir
        self.size = size

    def calculate(self):
        print("in calculate")
        stockPriceSchema = StructType([\
                            StructField("stockId", IntegerType()),\
                            StructField("timeStamp", IntegerType()), \
                            StructField("stockPrice", DoubleType())\
                            ])
        stockPriceInput = self.spark.read.format("csv").option("header","true").schema(stockPriceSchema).load(self.stockPriceInputDir)
        stockPriceInput.registerTempTable("stockPrice")
        movingAverage = self.spark.sql("select stockId,timeStamp,stockPrice, avg(stockPrice) over( PARTITION BY stockId ORDER BY stockId,timeStamp ROWS BETWEEN 2 PRECEDING AND 0 FOLLOWING ) as moving_average from stockPrice")
        movingAverage.show()
        return movingAverage



class MovingAverageWithStockInfo:
    spark = None
    stockPriceInputDir = None
    stockInfoInputDir = None
    size = 0
    def __init__(self, spark, stockPriceInputDir,stockInfoInputDir,size):
        self.spark = spark
        self.stockPriceInputDir = stockPriceInputDir
        self.stockInfoInputDir = stockInfoInputDir
        self.size = size

    def calculate(self):
        pass

    def calculate_for_a_stock(self,stockId):
        pass