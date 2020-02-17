# Pyspark

## Reading

1. Read the data as data frame, It converts the elements of Type Row having key value pairs.
Row(value='1,2,Football')
2. If you convert them to rdd then you get Row elements. hence first get all the values and then map them to your need.

```pyhton
categories=spark.read.text("resources/textFile/categories")
temp=categories.rdd.map(lambda rw: rw.value.split(",")).toDF(["col1","col2","col3"])
```

## Debug

   1. Take care of of the difference between take(1) and first()

      ***While take(1) returns as list of elements first() will return only the element.***

   2. Take


## Write

1. Text file only supports single column DF. If your DF has multiple column then you get following error:
*Text data source supports only a single column, and you have 3 columns*
2. In spark 2.2 there are two ways to add constant value in a column in DataFrame:

   1) Using lit

   2) Using typedLit.

The difference between the two is that typedLit can also handle parameterized scala types e.g. List, Seq, and Map
