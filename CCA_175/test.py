from pyspark.sql import SparkSession

spark= SparkSession.builder.appName("test").getOrCreate()

#seqRdd=spark.sparkContext.sequenceFile("./tester", "org.apache.hadoop.io.IntWritable", "org.apache.hadoop.io.Text").toDF(["col1","col2"])

#seqRdd.show()

# for item in seqRdd.take(2):
#               print(item[0])
#               print(item[1].split(",")[2])

# hiveFile=spark.read.format('csv')\
#               .option("sep","\001")\
#               .load("./resources/hiveFile")

# hiveFile.show()

txt=spark.read.option("lineSep", 'info,').text('resources/textFile/customLineSep.txt')

txt.show(n=2,truncate=False)

print(txt.count())