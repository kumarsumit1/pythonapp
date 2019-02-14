from pyspark.sql import SparkSession
import inspect



def basic_df_example(spark):
    categories=spark.read.json("../data/retail_json_db/categories/")
    categories.show()
    categories.printSchema()
    help(categories.show())
    categories.select("category_name").show(n=2,truncate=False)
    categories.select("category_name",(categories['category_id']+1).alias("summed_up")).show()
    categories.withColumn("summ",categories['category_id']+1).show()
    #DF syntax
    categories.filter(categories['category_id'] > 5).show()
    #SQL syntax
    categories.filter("category_id < 4").show()
    categories.groupby("category_department_id").count().show()
    #categories.groupBy(categories['category_department_id']).count().show()
    categories.createOrReplaceTempView("category")
    spark.sql("select * from category where category_id < 4").show()
    
def schema_inference_example(spark):
    print(dir(spark))
    print(vars(spark))
    print(type(spark.sparkContext))
    sc = spark.sparkContext()
    type(sc)    











if __name__ == "__main__" :
    spark = SparkSession.builder.appName("Spark-SQL-Basic").getOrCreate()
    
    #basic_df_example(spark)
    schema_inference_example(spark)
    