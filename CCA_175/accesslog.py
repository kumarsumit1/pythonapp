from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract

# https://opensource.com/article/19/5/log-data-apache-spark
# https://opensource.com/article/19/5/visualize-log-data-apache-spark


# https://datascience-enthusiast.com/Python/DataFrame_apache_log.html
spark = (
    SparkSession.builder.appName("access")
    .master("local[*]")
    .config("spark.driver.bindAddress", "localhost")
    .getOrCreate()
)

accessdf = spark.read.text("resources/textFile/accessLog.log")

accessdf.show(n=4)

pattern = r"(\S+) (\S+) (\S+) \[([\d\/A-Za-z\:\s\-]*)\] \"([A-Z]*) (\S*) ([A-Z\/0-9\.]+)\" ([0-9]+) ([0-9]*)"

fields = accessdf.select(
    regexp_extract("value", pattern, 1).alias("host"),
    regexp_extract("value", pattern, 2).alias("rfc931"),
    regexp_extract("value", pattern, 3).alias("authuser"),
    regexp_extract("value", pattern, 4).alias("timestamp"),
    regexp_extract("value", pattern, 5).alias("method"),
    regexp_extract("value", pattern, 6).alias("url"),
    regexp_extract("value", pattern, 7).alias("protocol"),
    regexp_extract("value", pattern, 8).alias("status"),
    regexp_extract("value", pattern, 9).alias("size"),
)

fields.show(n=4)
