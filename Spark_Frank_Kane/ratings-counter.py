from pyspark import SparkConf,SparkContext

conf=SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc=SparkContext(conf=conf)

lines=sc.textFile("./ml-100k/u.data")
ratings=lines.map(lambda x : x.split()[2])
result=ratings.countByValue()

print(type(result))

#print(help(result))

for key,value in result.items():
    print(key,value)
    
    
#sorting the items
    