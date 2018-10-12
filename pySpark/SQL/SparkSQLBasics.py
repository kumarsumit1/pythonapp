from pyspark.sql import SparkSession
import inspect



def basic_df_example(spark):
    dataframe=spark.read.json("../data/retail_json_db/categories/")
    dataframe.show()
    dataframe.printSchema()
    help(dataframe)
    categories.select("category_name").show(n=2,truncate=False)
    categories.select("category_name",(categories['category_id']+1).alias("summed_up")).show()
    categories.withColumn("summ",categories['category_id']+1).show()










if __name__ == "__main__" :
    spark = SparkSession.builder.appName("Spark-SQL-Basic").getOrCreate()
    
    basic_df_example(spark)
    