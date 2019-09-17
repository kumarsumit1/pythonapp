# HDFS Commands

### Copy from local file system to HDFS
hadoop fs -copyFromLocal /home/varunu28/word_count.txt /user/varunu28/textfiles

### Getting details about files,blocks and location of files in a HDFS
hdfs fsck /user/varunu28/textfiles -files -blocks -locations

### Copy from HDFS to local file system
hadoop fs -copyToLocal /user/varunu28/textfiles .

### Copy from local file system to HDFS with changed blocksize and replication factor
hadoop fs -Ddfs.blocksize=67108864 -Ddfs.repliction=1 -copyFromLocal textfiles /user/varunu28/textfiles

# put Command
hadoop fs -put /home/training/test_data.txt /user/cloudera/data

# put Command to overwrite the file if it already exists
hadoop fs -put -f /home/training/test_data.txt /user/cloudera/data

# get command to copy data from HDFS to local machine
hadoop fs -get /user/cloudera/data/test_data.txt /home/training/data

# get command to copy data from HDFS to local machine and keep the file properties same as the source HDFS folder
hadoop fs -get -p /user/cloudera/data/test_data.txt /home/training/data

# get command to copy data from HDFS to local machine along with HDFS checkpoints
hadoop fs -get -crc /user/cloudera/data/test_data.txt /home/training/data

