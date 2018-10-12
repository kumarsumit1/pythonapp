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