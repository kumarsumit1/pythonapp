from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
#https://acadgild.com/blog/windowing-functions-in-hive

spark = SparkSession.builder.appName("AnalyticalFunctions").getOrCreate()

df = spark.read.format("csv")\
              .option("header","False")\
              .option("compression","none")\
              .option("delimiter",",")\
              .load("resources/textFile/analticalFunctions.csv")
#"from_unixtime(unix_timestamp(_c0,'yyyyMMdd'),'yyyy-MM-dd') as dt"
dfcol=df.selectExpr("to_date(_c0,'yyyyMMdd') as dt","_c1 as Ticker","cast(_c2 as double) as Open","cast(_c3 as double) as High", "cast(_c4 as double) as Low","cast(_c5 as double) as Close", "cast(_c6 as int) as Volume_for_the_day")

dfcol.printSchema()

dfcol.show()

#print(df.count())
dfcol.registerTempTable("stocks")
#Lag 
#For an ascending order data Fetch prices of yesterday
#spark.sql("select Ticker,Open,lag(Open,2,0) over(partition by Ticker order by dt) as prevday_price,dt from stocks").show()

#Lead
#For an ascending order data Fetch prices of tomorrow
#spark.sql("select Ticker,Open,lead(Open,1,0) over(partition by Ticker order by dt) as nextday_price,dt from stocks").show()

#first_value
#First day price comparison each day
spark.sql("select Ticker, Open, first_value(Open) over(partition by Ticker order by dt) as firstday, dt from stocks").show()

#last_value
#Last day price comparision each day
spark.sql("select Ticker, Open, last_value(Open) over(partition by Ticker) as lastday,dt from stocks").show()
#Note : order by doesnt work in last_value clause

#Count
#number of rows present for each ticker.
spark.sql("select dt,Ticker, count(Ticker) over(partition by Ticker ) as count from stocks").show()

#Sum
#Finding running total of rows present in each ticker
spark.sql("select dt,Ticker,Open,sum(Open) over(partition by Ticker order by dt) as sum from stocks").show(30)

#Finding the percentage of each row value
spark.sql("select dt, Ticker, Volume_for_the_day, (sum(Volume_for_the_day) over (partition by Ticker order by dt)/sum(Volume_for_the_day) over(partition by Ticker))*100 as cenTot from stocks").show(30)

#Min
#minimum closing stock price for each particular ticker.
spark.sql("select dt,Ticker,close,min(Close) over(partition by Ticker ) minPrice from stocks").show()

#Max
#maximum closing stock price for each particular ticker.
spark.sql("select dt,Ticker,close,max(close) over(partition by Ticker) as maxVal from stocks").show()

#Avg
#average closing stock price for each particular ticker.
spark.sql("select dt,Ticker,close,avg(close) over(partition by Ticker) as avg from stocks").show()

#Rank()
#closing prices of the stock for each ticker
spark.sql("select dt,Ticker,Close,rank() over(partition by Ticker order by dt) as rnk from stocks").show(30)

#Dense_rank()
spark.sql("select dt,Ticker,close,dense_rank() over(partition by close order by dt) as rnk from stocks").show()


#row_number()
#closing price and its row number for each ticker.
spark.sql("select dt,Ticker,Volume_for_the_day,row_number() over (partition by Ticker order by dt) as rnum from stocks").show()

#cumit_dist()
#Cumilative distribution for volumer for the day
spark.sql("select dt,Ticker, Volume_for_the_day, cume_dist() over( partition by Ticker order by Volume_for_the_day) as cumdist from stocks ").show(30)


#Percent_rank()
spark.sql("select dt,Ticker, Volume_for_the_day,rank() over(partition by Ticker order by volume_for_the_day) as rnk,percent_rank() over(partition by Ticker order by volume_for_the_day) as pctrnk , cume_dist() over( partition by Ticker order by Volume_for_the_day) as cumdist from stocks").show(30)


#Ntile()
spark.sql("select dt,Ticker,volume_for_the_day,ntile(4) over(partition by ticker order by volume_for_the_day) as nt from stocks").show()

