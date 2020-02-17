from pyspark.sql import SparkSession
from pyspark.sql.functions import concat,lit

spark= SparkSession.builder.appName("test").getOrCreate()

categories=spark.read.text("resources/textFile/categories")

temp=categories.rdd.map(lambda rw: rw.value.split(",")).toDF(["col1","col2","col3"])

#temp.select (concat('col1',lit(','),'col2',lit(','),'col3').alias("ca")).write.mode("overwrite").format("squence").save("./test")

#temp.select (concat('col1',lit(','),'col2',lit(','),'col3').alias("ca")).show()

test=temp.select (concat('col1',lit(','),'col2',lit(','),'col3').alias("ca")).rdd.map(lambda rw: (1, rw.ca)).saveAsSequenceFile("./tester",None)

for it in test.take(2):
     print(it)


#categories.show()