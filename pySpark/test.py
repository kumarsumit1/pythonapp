
# -*- coding: utf-8 -*-
"""

@author: sumit.kumar
"""

import os
import sys

#os.chdir("D:\sumit\code\PythonExamples")
#os.curdir

# Configure the environment. 
# Set this up to the directory where Spark is installed

#if 'SPARK_HOME' not in os.environ:
#    os.environ['SPARK_HOME'] = 'C:\Users\sumit.kumar\spark-1.6.1-bin-hadoop2.6'

# Create a variable for our root path

#SPARK_HOME = os.environ['SPARK_HOME']

# Add the following paths to the system path.

#sys.path.insert(0, os.path.join(SPARK_HOME, "python"))
#sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib"))
#sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib", "pyspark.zip"))
#sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib", "py4j-0.9-src.zip"))

# Initiate Spark context.

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import HiveContext
import pandas as pd


# Configure Spark Settings

conf = SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "2")
conf.setAppName("Spark")

# # Initialize SparkContext. 

sc = SparkContext('local', conf=conf)
# Test with a data file, I used an auto data file
sqlContext = HiveContext(sc)

sqlContext.setConf("hive.exec.dynamic.partition", "true")
sqlContext.setConf("hive.exec.dynamic.partition.mode", "nonstrict")
sqlContext.sql("CREATE DATABASE IF NOT EXISTS test")
pandas_df = pd.read_csv('D:\\value.csv')  
# assuming the file contains a header
# pandas_df = pd.read_csv('file.csv', names = ['column 1','column 2']) # if no header
s_df = sqlContext.createDataFrame(pandas_df)
s_df.count()

#print (s_df.count())

s_df.write.mode("overwrite").saveAsTable("test.value")
#sqlContext.sql("CREATE DATABASE IF NOT EXISTS test")

tab=sqlContext.sql("select * from test.value")
tab.printSchema()
tab.show(5, False)

   
