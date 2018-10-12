from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataFrameBasics").getOrCreate()

ppl=spark.read.json("./data/people.json")

ppl.show()

ppl.printSchema()

print( ppl.columns) 

des= ppl.describe()

print(type(des))

des.show()

# Apple stockes

appleStocks=spark.read.csv("./data/appl_stock.csv",inferSchema=True,header=True)

appleStocks.show()

print(appleStocks.head(3))

print(appleStocks.head(3)[0])

#SQL syntax
appleStocks.filter("Close < 500").select(["Open","Close"]).show()

#DF syntax
appleStocks.filter(appleStocks['Close'] < 500 ).select(['Open','Close']).show()

### In DF syntax the python 'and' and 'or' logic will not work.
### Also enclose each logical block within parantheses i.e () before '&' or '|'

#SQL syntax
appleStocks.filter("Close < 200 and Open !< 200 ").show()

#Now in DF syntax above logic will be , notice the parantheses , the not operator and ampersand operator.

# The block within filter is syntactically like java/scala block and not Python
appleStocks.filter( (appleStocks["Close"] < 200) &  ~(appleStocks['Open']< 200) ).show()


## Collecting data and converting the rows in Dict (Python's Map)
rowCollect=appleStocks.filter( (appleStocks["Close"] < 200) &  ~(appleStocks['Open']< 200) ).head(5)

print(rowCollect)

print(rowCollect[0])

print(rowCollect[0].asDict())

print(rowCollect[0].asDict()['Volume'])

###################  Group by and Aggregate ######################################

sales=spark.read.csv("./data/sales_info.csv", inferSchema=True,header=True)

sales.show() 

# Applying group by on a DF gives you 'GroupedData' on which one can apply : agg(),avg(),count(),max(),mean(),min(),sum()

#help(sales.groupBy("Company"))

#SQL syntax
sales.groupBy("Company").count().show()

sales.groupBy(sales["Company"]).count().show()

# Using aggregate function i.e agg() , 
# Note : it takes an argument as a Dict

sales.agg({"Company":"count"}).show()

sales.agg({"Sales":"max"}).show()

#agg function can be applied on GroupedData too . 
#so its like group by and then whatever aggregate function you apply in select clause

sales.groupBy("Company").agg({"Company":"count"}).show()

sales.groupBy("Company").agg({"Sales":"max"}).show()


# Importing functions

'''
#One way of importing 
import pyspark.sql.functions as fun

sales.select(fun.avg('Sales').alias("average_sales")).show()
'''
from pyspark.sql.functions import countDistinct,avg,stddev

#Note The alias is applied at column name itself
sales.select(avg('Sales').alias("average_sales")).show()

#Formatting the numbers
from pyspark.sql.functions import format_number

sales.select( format_number(avg("Sales"),2).alias("formatted_avg") ).show()

#Order by

#SQL syntax

sales.orderBy("Sales").show()

#DF syntax
sales.orderBy(sales['Sales']).show()

#If you want specific ordering then you will have to do it in DF format or go for SQL syntax completely i.e SQL statement
sales.orderBy(sales['Sales'].desc()).show()

#Missing Data

missingData=spark.read.csv("./data/ContainsNull.csv",header=True,inferSchema=True)

missingData.show()

#It will drop all the rows having any null value
missingData.na.drop().show()

#Threshold : here it will drop any row having 2 or more null vlaues

missingData.na.drop(thresh=2).show()

#'how' states how would you want to drop the null values, by default its set to 'any'
# similarly 'all' param will drop any row only if all the rows have null values

missingData.na.drop(how='any').show() 

#Subset : will drop columns having null and part of subset columns

missingData.na.drop(subset=['Sales']).show()

#Fill values substitutes null values with the argument values. 
#Also by default the fill values only replaces arg value with columns having same dataType

missingData.na.fill("replaces_StringType").show()

#replace int column types only
missingData.na.fill(0).show()

#replace string column types only
missingData.na.fill("0").show()

#fill can be used in conjuction with subset to be applicable only to specific columns only. Should be preferred

missingData.na.fill(0,subset=['Sales']).show()

#if we want to substitute any field with mean value 

missingData.na.fill( missingData.select( avg('Sales') ).collect()[0][0] , subset=['Sales']).show() 


# Date and Timestamps 

#DataFrame syntax
appleStocks.select(appleStocks['Date'],appleStocks['Open']).show()

#Dataset syntax
appleStocks.select(appleStocks.Date,appleStocks.Open).show()

#SQL syntax
appleStocks.select(['Date','Open']).show()

appleStocks.select("Date","Open").show()


from pyspark.sql.functions import hour,month,year,dayofmonth,dayofmonth,weekofyear,date_format,format_number

appleStocks.select(month(appleStocks['Date'])).show()

appleStocks.select(weekofyear(appleStocks['Date'])).show()

#Calculate average closing price per year.
# Steps 1. first find year cols, 2. group by year col 3. and then use average price on closing price

# 1. add year to DF

gpd=appleStocks.withColumn("yr", year(appleStocks['Date']) ).groupBy("yr").avg('Close','High')

gpd.show()

gpd.printSchema()

gpd.select(gpd["yr"],gpd["avg(Close)"].alias("avg_close"), gpd["avg(High)"].alias("avg_high")).show()

print(gpd.describe())

gpd.select(gpd["yr"],format_number(gpd["avg(Close)"],2).alias("avg_close"), format_number(gpd["avg(High)"],2).alias("avg_high")).show()

#select(avg('Close'),"yr").show()


