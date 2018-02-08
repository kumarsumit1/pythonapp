# Initiate Spark context.

from pyspark import SparkContext
from pyspark import SparkConf
#from pyspark.sql import HiveContext
#import pandas as pd


# Configure Spark Settings

conf = SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "2")
conf.setAppName("Spark")

# # Initialize SparkContext. 

sc = SparkContext('local', conf=conf)

#Loading the data from file
orders=sc.textFile("./data/retail_db/orders")

orderItems= sc.textFile("./data/retail_db/order_items")


#print first element
print(orders.first())

#Print count
print(orders.count())

#Map to pair
orderPair=orders.map(lambda r : (len(r),r,r.split(",")[0]))

print(orderPair.first())

print(orders.map(lambda r : r.split(",")[3] ).distinct().collect())

ordersFiltered=orders.filter(lambda fil : fil.split(",")[3]=="CLOSED" or fil.split(",")[3]=="COMPLETE")

ordersFil= ordersFiltered.map(lambda x : (x.split(",")[0],x))

for of in ordersFil.take(10) : print(of)

#Accumulators

def filFunction(rw,ordersCompleted,ordersPending):
    status=rw.split(",")[3]=="COMPLETE" or rw.split(",")[3]=="CLOSED"
    if(status):
        ordersCompleted=ordersCompleted.add(1)
    else:
        ordersPending.add(1)
    return status     
       

ordersCompleted=sc.accumulator(0)
ordersPending=sc.accumulator(0)

ordersFilt=orders.filter(lambda rw : filFunction(rw,ordersCompleted,ordersPending))

print(ordersFilt.count())

#help(ordersCompleted)

print(ordersCompleted.value)
print(ordersPending.value)


#Now join order and order item , based on dates from oders and product id and cost from order items

ordersFilDate=ordersFilt.map(lambda x : (int(x.split(",")[0]),x.split(",")[1]))

orderIt = orderItems.map(lambda x : (int(x.split(",")[1]),((x.split(",")[2]),x.split(",")[3])))

print(ordersFilDate.first())

print(orderIt.first())


#Join the RDDs

injoin=ordersFilDate.join(orderIt)

lejoin=ordersFilDate.leftOuterJoin(orderIt)

rijoin=ordersFilDate.rightOuterJoin(orderIt)

fujoin=ordersFilDate.fullOuterJoin(orderIt)


for i in injoin.take(10) : print ("INNER JOIN :: ",i )

for i in lejoin.take(10) : print ("LEFT JOIN :: ", i)

for i in rijoin.take(10) : print ("RIGHT JOIN :: ", i)

for i in fujoin.take(10) : print ("FULL OUTER JOIN :: ", i)


prodRaw=open("./data/retail_db/products/part-00000").read().splitlines()

print(prodRaw[0])

prod=sc.parallelize(prodRaw)

prodMap=prod.map(lambda x : (x.split(",")[0],x))

print(prodMap.first())

#prod.cache()


#Import statement is required for storage level vals
from pyspark import StorageLevel

prod.persist(StorageLevel.MEMORY_ONLY)

print(prod.first())

for prd in prod.take(10): print( prd)

#help(prod.take(10))



sc.stop()
#Loading the data from list
#lst=list(range(1,10))

#lstRDD=sc.parallelize(lst)

#lstRDD.foreach(lambda r: print(r))

#help(lstRDD.take(5))

#1st task is to extract the data from csv files from hdfs, apply filters and ordering with specified columns.






