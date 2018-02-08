from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .getOrCreate()
 
sc = spark.sparkContext
myRdd = sc.parallelize([1,2,3,4,5,6,7,8])
print(myRdd.take(5))