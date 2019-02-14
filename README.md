## Setting up Pyhon
1. https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/


## Steps to install Spark and Python

1. http://sundog-education.com/spark-python/
2. https://towardsdatascience.com/machine-learning-with-pyspark-and-mllib-solving-a-binary-classification-problem-96396065d2aa
.. https://medium.com/@mrpowers/creating-a-pyspark-project-with-pytest-pyenv-and-egg-files-d2709eb1604c
.. https://www.supergloo.com/fieldnotes/how-to-deploy-python-programs-to-a-spark-cluster/
3. https://medium.com/@amimahloof/how-to-package-a-python-project-with-all-of-its-dependencies-for-offline-install-7eb240b27418
4. https://bytes.grubhub.com/managing-dependencies-and-artifacts-in-pyspark-7641aa89ddb7


https://www.datacamp.com/community/tutorials/apache-spark-tutorial-machine-learning

https://mapr.com/blog/churn-prediction-pyspark-using-mllib-and-ml-packages/


## Spark Certification 

https://www.youtube.com/watch?v=yXBrcOTa_w4&list=PLf0swTFhTI8rT3ApjBqt338MCO0ZvReFt&index=33

[Link of CDH Docker Image] (
https://downloads.cloudera.com/demo_vm/docker/cloudera-quickstart-vm-5.13.0-0-beta-docker.tar.gz )

https://www.cloudera.com/documentation/enterprise/5-13-x/topics/quickstart_docker_container.html
## Steps to install CDH
    
	docker import cloudera-quickstart-vm-5.13.0-0-beta-docker.tar cloudera/quickstart:latest
	
	docker images
	
	docker run --hostname=quickstart.cloudera --privileged=true -t -i [OPTIONS] [IMAGE] /usr/bin/docker-quickstart

###### Option Description

--hostname=quickstart.cloudera  ->
	**Required**: Pseudo-distributed configuration assumes this hostname.

--privileged=true ->
	**Required**: For HBase, MySQL-backed Hive metastore, Hue, Oozie, Sentry, and Cloudera Manager.

-t ->	**Required**: Allocate a pseudoterminal. Once services are started, a Bash shell takes over. This switch starts a terminal emulator to run the services.

-i -> 	**Required**: If you want to use the terminal, either immediately or connect to the terminal later.

-p 8888 -> 	**Recommended**: Map the Hue port in the guest to another port on the host.

-p [PORT] -> 	**Optional**: Map any other ports (for example, 7180 for Cloudera Manager, 80 for a guided tutorial).

-d -> 	**Optional**: Run the container in the background.

*docker run hostname=quickstart.cloudera privileged=true -t -i -v /home/sangeles/Byte/BIGDATA/Hadoop/Cloudera:/src publish-all=true -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /usr/bin/docker-quickstart*
	
Tried:
docker run --hostname=quickstart.cloudera --privileged=true -t -i --publish-all=true -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /usr/bin/docker-quickstart	
	
From cdh cmd line	
/home/cloudera/cloudera-manager --express	
	
	
service ntpd restart	
	
 cloudera user :\
     username: cloudera \
    password: cloudera
	
The root account password is cloudera.

The root MySQL password (and the password for other MySQL user accounts) is also cloudera

Cloudera Manager is not started by default. To see options for starting Cloudera Manager, run the following command:

/home/cloudera/cloudera-manager
	
[ Tutorial CDH ] ( https://medium.com/@SnazzyHam/how-to-get-up-and-running-with-clouderas-quickstart-docker-container-732c04ed0280 )

[ Spark Packaging ] ( https://bytes.grubhub.com/managing-dependencies-and-artifacts-in-pyspark-7641aa89ddb7 )
                     (https://github.com/alekseyig/spark-submit-deps )

[ Spark Pack ] ( https://developerzen.com/best-practices-writing-production-grade-pyspark-jobs-cb688ac4d20f )


## Sample spark-submit  https://github.com/alekseyig/spark-submit-deps

/usr/lib/spark/bin/spark-submit --conf spark.hadoop.yarn.resourcemanager.connect.max-wait.ms=60000 --conf spark.hadoop.fs.defaultFS=hdfs://ip-172-31-105-149.ec2.internal:8020 --conf spark.hadoop.yarn.resourcemanager.address=ip-172-31-105-149.ec2.internal:8032 --conf spark.dynamicAllocation.enabled=true --conf spark.shuffle.service.enabled=true --conf spark.dynamicAllocation.minExecutors=1 --conf spark.dynamicAllocation.maxExecutors=38 --conf spark.executor.memory=5g --conf spark.executor.cores=4 --name tape --master yarn --deploy-mode cluster --jars /opt/amazon/superjar/glue-assembly.jar --files /tmp/glue-default.conf,/tmp/glue-override.conf,/opt/amazon/certs/InternalAndExternalAndAWSTrustStore.jks,/opt/amazon/certs/rds-combined-ca-bundle.pem,/opt/amazon/certs/redshift-ssl-ca-cert.pem,/opt/amazon/certs/RDSTrustStore.jks,/tmp/image-creation-time,,/tmp/g-3a0f2403b8c8a7ead7c4454d76bb788e5c250b9a-7612692496177147945/script_2018-10-16-10-57-53.py --py-files /tmp/PyGlue.zip /tmp/runscript.py script_2018-10-16-10-57-53.py --JOB_NAME stocksjob1 --JOB_ID j_2dde8c599ddd2f6b43d39eb153223626fdd9eb40a046383fa40a638a08dba628 --JOB_RUN_ID jr_d3c41b4da8db2b8ca62cac390765d25f9e839ae8f72569436c7659da5a46d4e0 --job-bookmark-option job-bookmark-disable --TempDir s3://aws-glue-temporary-145548758791-us-east-1/demr255048