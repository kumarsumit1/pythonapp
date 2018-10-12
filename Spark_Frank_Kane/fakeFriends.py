from pyspark import SparkConf,SparkContext

#Average Friends by age

#define 
def rowSum(rowElement):
    #print("The methods of row elements are",dir(rowElement))
    #print("the value of rowElement is ", rowElement.data)
    #print("the value of rowElement is ", rowElement.index)
    #print("the value of rowElement is ", rowElement.maxindex)
    #age=rowElement[0]
    frndCount=rowElement.data
    sum=0
    count=0
    for item in frndCount:
        sum=sum+int(item[0])
        count=count+int(item[1])
    return (sum,count)    
    
conf = SparkConf().setMaster("local").setAppName("FakeFriends")

sc = SparkContext(conf=conf);

friends=sc.textFile("./fakefriends.csv")

print(friends.first())



frenRDD = friends.map(lambda x : (x.split(",")[2],(x.split(",")[3],1)))

print(frenRDD.first())

frenRDD.foreach(lambda x : print("The elements are ",x[0],x[1][0],x[1][1]))

sumOfFrnd=frenRDD.groupByKey().mapValues(rowSum)

sumOfFrnd.foreach(lambda x: print("Age sum total of friends and their count", x))

avgFrndCount=sumOfFrnd.mapValues(lambda x : x[0]/x[1])

avgFrndCount.foreach(lambda x : print("row wise elements are ",x))

##Second approach using reduce by key
fl=frenRDD.reduceByKey(lambda x,y : (int(x[0])+int(y[0]),int(x[1])+int(y[1])))

fl.foreach(lambda x: print("The val is",x))

fl.mapValues(lambda x : x[0]/x[1]).foreach(lambda y : print(" The elements are ",y))


## Third approach using aggregate by key
seqOp = (lambda x,y : (int(x[0])+int(y[0]),int(x[1])+int(y[1])))
combOp = (lambda x,y : (int(x[0])+int(y[0]),int(x[1])+int(y[1])))
#seqOp = (lambda x, y: (int(x[0]) + int(y[0]), int(x[1]) + int(y[1])))
#combOp = (lambda x, y: (int(x[0]) + int(y[0]), int(x[1]) + int(y[1])))

flt=frenRDD.aggregateByKey((0,0), seqOp, combOp).mapValues(lambda x : x[0]/x[1])

flt.foreach(lambda y:print("The elems are",y))



'''
fe=te.collect()

print(type(fe))

for item in fe:
 print("the first item is ",item[0])
 print("the second item is ",item[1])
     for it in item[1]:
     print("the elements are",it)'''

