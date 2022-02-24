# Pyspark

spark-sql --master yarn --name spark_load_test -e "select * from retail.dgentab limit 2; select * from retail.dgentab limit 2;"

spark-submit --master yarn test.py

## Reading

1. Read the data as data frame, It converts the elements of Type Row having key value pairs.
Row(value='1,2,Football')
2. If you convert them to rdd then you get Row elements. hence first get all the values and then map them to your need.

```pyhton
categories=spark.read.text("resources/textFile/categories")
temp=categories.rdd.map(lambda rw: rw.value.split(",")).toDF(["col1","col2","col3"])
```

3. Use spark.read() which is internally uses all the supported formats of DataFrameReader()



## Write

1. Text file only supports single column DF. If your DF has multiple column then you get following error:
*Text data source supports only a single column, and you have 3 columns*
2. In spark 2.2 there are two ways to add constant value in a column in DataFrame:

   1) Using lit

   2) Using typedLit.

The difference between the two is that typedLit can also handle parameterized scala types e.g. List, Seq, and Map

3. Use DataFrame.write() which internally uses all the supported formats of DataFrameWriter(df)


## Debug

   1. Take care of of the difference between take(1) and first()

      ***While take(1) returns as list of elements first() will return only the element.***

   2. Take
   
   3. help ()
   
   4. dir ()

## Stpes to solve problem 

pyspark --master yarn --packages org.apache.spark:spark-avro_2.11:2.4.0

data:text/html <html contenteditable>

from pyspark.sql.functions import lit
from pyspark.sql.functions import concat,lit

prob1df= sqlContext.read.format("com.databricks.spark.avro").load("input_dir")

prob1df.printSchema()

prob1df=prob1df.selectExpr("to_date(_c0,'yyyyMMdd') as dt","_c1 as Ticker","cast(_c2 as double) as Open","cast(_c3 as double) as High", "cast(_c4 as double) as Low","cast(_c5 as double) as Close", "cast(_c6 as int) as Volume_for_the_day")

prob1samp=prob1df.sample(False, 0.1, seed=0).limit(1);

prob1samp.printSchema()

prob1samp.show()


create temp view
createOrReplaceTempView()




prob1out=spark.sql()
prob1out.write.format("com.databricks.spark.avro").save("output_dir");
out10.write.format("avro").option("comrpession","snappy").mode("overwrite").saveAsTable("test1_solutions.q10_soln",path="/verulam_blue/test1/problem10/solution/")

   import os
   os.system("hdfs dfs -ls -R /verulam_blue/test1")
   os.system("hdfs dfs -cat /verulam_blue/tests/data/tab_text/hr/part-00000-49651445-1cc9-487b-8f1f-2a2e3dd0b55f-c000.txt.gz | more")
   os.system("hdfs dfs -cat /verulam_blue/tests/data/tab_text/hr/part-00000-49651445-1cc9-487b-8f1f-2a2e3dd0b55f-c000.txt.gz | head") #Less command would not be efficient 
   os.system("hdfs dfs -tail /verulam_blue/tests/data/tab_text/hr/part-00000-49651445-1cc9-487b-8f1f-2a2e3dd0b55f-c000.txt.gz")
   
   
date and time conversion
   
   
prob1=spark.read.format("parquet").option("compression","gzip").load("/verulam_blue/tests/data/parquet/hr_records/")

prob1.printSchema()

 |-- name_prefix: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_initial: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- date_of_birth: date (nullable = true)
 |-- date_of_joining: date (nullable = true)
 |-- salary: integer (nullable = true)
 |-- last_pct_hike: integer (nullable = true)
 |-- ssn: string (nullable = true)
 |-- phone_nbr: string (nullable = true)
 |-- place_name: string (nullable = true)
 |-- county: string (nullable = true)
 |-- city: string (nullable = true)
 |-- state: string (nullable = true)
 |-- zip: string (nullable = true)
 |-- region: string (nullable = true)
 |-- user_name: string (nullable = true)


prob1.createOrReplaceTempView("prob1")

spark.sql("select * from prob1 tablesample(25 rows)").createOrReplaceTempView("prob1sample")

spark.sql("select * from prob1sample").show(15)


spark.sql("select first_name,last_name, month(date_of_joining) as month_of_joining,year(date_of_joining) as year_of_joining from prob1sample where year(date_of_joining)= 2015 order by month(date_of_joining) asc").show(5)



prob1out=spark.sql("select first_name,last_name, month(date_of_joining) as month_of_joining,year(date_of_joining) as year_of_joining from prob1 where year(date_of_joining)= 2015 order by month(date_of_joining) asc")



prob1out.write.format("json").option("compression","gzip").mode("overwrite").save("/verulam_blue/test1/problem1/solution/")


import os

os.system("hdfs dfs -ls -R /verulam_blue/test1/problem1/solution/ ")


spark.read.format("json").option("compression","gzip").load("/verulam_blue/test1/problem1/solution/").show(5)


   
Write only one file name    
https://mungingdata.com/apache-spark/output-one-file-csv-parquet/
   
   
#######

concat():

out4=prob1.selectExpr("concat(first_name,'|', last_name,cast(9 as string)) as result")

concat_ws():

out5=prob1.selectExpr("concat_ws('\t',*) as result")

out6=prob1.selectExpr("concat_ws('|',first_name,last_name,cast(9 as string))")

cast() : 
out7=prob1.selectExpr("cast(salary as string) as sal","cast(zip as int) as pin")


tablesample :
out8=spark.sql("select * from prob1 tablesample( 4 rows)")




Order by | nulls first 
spark.sql("select first_name from prob2 order by first_name nulls first").show(5)


accessing arrays (split ),converting arrasy to row /column

SELECT CONCTNS.splitted_cnctns[0] AS con1,
CONCTNS.splitted_cnctns[1] AS con2,
CONCTNS.splitted_cnctns[2] AS con3
FROM (SELECT split(connections,',') AS splitted_cnctns
FROM bdp.transact_tbl)CONCTNS;


cloase / nvl  -- done


trim() --remove space 


decimal places --round


string begins, ends , like , contains 

regex


df read table 

partition bucket

-----------
Three ques
pyspark launch best options
order insert
