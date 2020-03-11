#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pyspark.sql import SparkSession
from pyspark import SparkFiles


spark = SparkSession.builder.enableHiveSupport().getOrCreate()
print("--------------- started ------------------------")
spark.sparkContext.addFile("addFile.txt")

print("current directory : " + os.getcwd() )
print("SparkFiles: " + SparkFiles.getRootDirectory())
#After passing --files arg in spark submit this param will show a list of files
print("Dist Files: " + spark.conf.get("spark.yarn.dist.files"))

#Following line only returns the absolute path doesnt check if file exists or not.
print("SparkFiles : "+SparkFiles.get('addFile.txt'))
print("SparkFiles : "+SparkFiles.get('files.txt'))


with open(SparkFiles.get('addFile.txt')) as test_file:
    print(test_file.read())

#This will throw an error 
with open(SparkFiles.get('files.txt')) as test_file:
    print(test_file.read())    

# If file schema is not given,it defaults to fs.defaultFS setting in your core-site.xml 
# default value file:///
# But usually its set to hdfs://<NodeManager>:8020

spark.read.text('addFile.txt')
spark.read.text('files.txt')    

