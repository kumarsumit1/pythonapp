from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadTable").enableHiveSupport().getOrCreate()


temp = spark.read.table("movies_100k.movies")

temp.show(n=2)

temp.repartition(5).write.mode("overwrite").saveAsTable("retail.dgentab")
