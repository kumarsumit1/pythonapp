from pyspark import SparkConf,SparkContext

def parseline(line):
    arr=line.split(",")
    return (arr[0],arr[2],arr[3])

conf=SparkConf().setMaster("local").setAppName("MinMaxTemp")

sc = SparkContext(conf=conf)

tempFile=sc.textFile("./1800.csv")
print(tempFile.first())

maxFilterRDD=tempFile.filter(lambda rowStr: 'TMAX' in rowStr).map(parseline)
minFilterRDD=tempFile.filter(lambda rowStr: 'TMIN' in rowStr).map(parseline)

print(maxFilterRDD.first())

#print(minFilterRDD.first())




