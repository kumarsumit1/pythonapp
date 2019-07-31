from math import exp
from random import randint
from datetime import datetime
# https://datarus.wordpress.com/2015/05/04/fighting-the-skew-in-spark/ 
def count_elements(splitIndex, iterator):
    n = sum(1 for _ in iterator)
    yield (splitIndex, n)
 
def get_part_index(splitIndex, iterator):
    for it in iterator:
        yield (splitIndex, it)
 
num_parts = 16
from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .getOrCreate()
 
sc = spark.sparkContext
# create the large skewed rdd
skewed_large_rdd = sc.parallelize(range(0,num_parts), num_parts)\
              .flatMap(lambda x: range(0, int(exp(x))))
 
print("skewed_large_rdd has %d partitions."%skewed_large_rdd.getNumPartitions())
print("The distribution of elements across partitions is: %s" \
               %str(skewed_large_rdd.mapPartitionsWithIndex(lambda ind, x: count_elements(ind, x))\
                             .take(num_parts)))
 
# put it in (key, value) form
skewed_large_rdd = skewed_large_rdd.mapPartitionsWithIndex(lambda ind, x: get_part_index(ind, x))\
              .cache()

skewed_large_rdd.count()
#skewed_large_rdd.take(4)
#[(0, 0), (1, 0), (1, 1), (2, 0)]

small_rdd = sc.parallelize(range(0,num_parts), num_parts).map(lambda x: (x, x)).cache()
small_rdd.count()

#small_rdd.take(4)
#[(0, 0), (1, 1), (2, 2), (3, 3)]

# t0 = datetime.now()
result = skewed_large_rdd.leftOuterJoin(small_rdd)
result.count() 
# print("The direct join takes %s"%(str(datetime.now() - t0)))

#result.take(4)
#[(0, (0, 0)), (1, (0, 1)), (1, (1, 1)), (2, (0, 2))]

# parameter to control level of data replication
N = 100 
# replicate the small rdd
small_rdd_transformed = small_rdd\
        .cartesian(sc.parallelize(range(0, N)))\
        .map(lambda x: ((x[0][0], x[1]), x[0][1]))\
                .coalesce(num_parts).cache() 

#1600
small_rdd_transformed.count()

# [((0, 0), 0), ((0, 1), 0), ((0, 2), 0), ((0, 3), 0)]
# small_rdd_transformed.take(4)

#[((0, 0), 0),
# ((0, 1), 0),
# ((0, 2), 0),
# ((2, 0), 2),
#  ((2, 1), 2),
#  ((2, 2), 2),
#   ((4, 0), 4),
#  ((4, 1), 4),
#  ((4, 2), 4),
#  ((4, 3), 4), ....
# add a random int to forma  new key
skewed_large_rdd_transformed = skewed_large_rdd.\
        map(lambda x: ((x[0], randint(0, N-1)), x[1]))\
                .partitionBy(num_parts).cache() 

skewed_large_rdd_transformed.count()

#skewed_large_rdd_transformed.take(10)
# [((3, 55), 8),
#  ((4, 98), 5),
#  ((4, 18), 15),
#  ((4, 18), 36),
#  ((5, 33), 18),
#  ((5, 81), 33),
#  ((5, 81), 41),
#  ((5, 17), 54),
#  ((5, 17), 62),
#  ((5, 1), 66)]   <--
 
# t0 = datetime.now()
result = skewed_large_rdd_transformed\
        .leftOuterJoin(small_rdd_transformed)
result.count()

#result.take(10)
# [((4, 98), (5, 4)),
#  ((5, 33), (18, 5)),
#  ((5, 1), (66, 5)),  <--
#  ((5, 97), (131, 5)),
#  ((6, 12), (70, 6)),
#  ((6, 12), (126, 6)),
#  ((6, 12), (358, 6)),
#  ((6, 76), (106, 6)),
#  ((6, 76), (302, 6)),
#  ((6, 76), (308, 6))]

# print("The hashed join takes %s"%(str(datetime.now() - t0)))

# spark.HDFScopyMerge()