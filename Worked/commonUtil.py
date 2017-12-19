# -*- coding: utf-8 -*-
"""


@author: sumit.kumar
"""
import os,ftplib
import json,datetime,urllib2,urllib
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext,SQLContext
#import requests

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0


# instantiate
config = ConfigParser()

# parse existing file
config.read('config.ini')


def fetchProperty(section,key):
    try:
        return config.get(section, key)
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________ 0 Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute fetchProperty : %s : %s " %("Property File key not found", str(e)))
'''
def updateJobExecDetails( cId,status,modifiedBy,runDate,ulerId):
    try:
        updateUrl=fetchProperty('API', 'UPDATE_EXEC_API')
        
        # data to be sent to Update
        updateJson = {"cId":cId,
                      "status":status,
                      "modifiedBy":modifiedBy,
                      "runDate" : runDate,
                      "scheduler" : { "ulerId" : ulerId}
                      }
        
        resp = requests.post(url = updateUrl, json = updateJson)
        if resp.status_code==200:
            print("The response received is : ",resp.text)
            return resp.text
        else:
            print("The response received is : ",resp.status_code)
            print("The data fetched is : ",resp.text)
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________ Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute updateJobExecDetails : %s : %s " %("API request", str(e)))
'''
##
# This function will fetch dataset details from API
#
##  

def postDetails( cId,status,modifiedBy,runDate,ulerId):
    try:
        updateUrl=fetchProperty('API', 'UPDATEEXEC_API')
        
        # data to be sent to Update
        updateJson = {"cId":cId,
                      "status":status,
                      "modifiedBy":modifiedBy,
                      "runDate" : runDate,
                      "uler" : { "ulerId" : ulerId}
                      }
        req = urllib2.Request(updateUrl, json.dumps(updateJson), headers={'Content-type': 'application/json', 'Accept': 'application/json'})
        resp = urllib2.urlopen(req)
        return resp.read()       
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute postDetails : %s : %s " %("API request", str(e)))
    

def getDetails(section,api,queryParam):
    try:
      url = fetchProperty(section, api)
      print(url)
      if queryParam:
          print("in If block")
          param=urllib.urlencode(queryParam)
          print(param)    
          response = urllib2.urlopen(url+"/?"+param)
          re=response.read()
          print re 
      else:
          print("in else block "+url)
          response = urllib2.urlopen(url)  
          print response.info()
          re=response.read()
          print re       
      #data = json.loads(re)    
      return re
    except Exception as e:
         print (str(datetime.datetime.now()) + "____________ Abruptly Exited________________")
         raise Exception("Exception::msg::Could not execute getDetails : %s : %s " %("API request", str(e)))    
        
'''            
def fetchDetails(section,api,queryParam):
    try:
        queryUrl = fetchProperty(section, api)

        response= requests.get(url=queryUrl,params =queryParam)
        if response.status_code==200:
            print("The response recieved is : ",response.text)
            return response.text
        else:
            print("The response recieved is : ",response.status_code)
            print("The data fetched is : ",response.text)
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute fetchDetails : %s : %s " %("API request", str(e)))    
'''    
    
def fetchJobDetails():
    try:
       return getDetails('API', 'JOB_API',None)
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute fetchJobDetails : %s : %s " %("API request", str(e)))  
    
def fetchDatasetDetails(Id):
    try:
        queryParam= {"Id":Id
                    }
        
        return getDetails('API', '_API',queryParam)
    except Exception as e:
        print (str(datetime.datetime.now()) + "____________ Abruptly Exited________________")
        raise Exception("Exception::msg::Could not execute fetchDatasetDetails : %s : %s " %("API request", str(e)))      
           


def createSparkContext(APP_NAME,log_level):
    try:
                # Configure Spark
        conf = SparkConf().setAppName(APP_NAME)
        # Comment this line in non local env
        # conf = conf.setMaster("local[*]")
        #conf.set('spark.testing.memory','6147480000')
        sc = SparkContext(conf=conf)
        #sc=SparkContext.getOrCreate(conf=conf)
        #sc.addPyFile(path)   

        log4j = sc._jvm.org.apache.log4j  
        #if log_level=="ERROR" :
        #    log4j.LogManager.getRootLogger().setLevel(log4j.LogManager.getRootLogger().setLevel(log4j.Level.ERROR))
        #elif log_levle=="WARN" :
        #log4j.LogManager.getRootLogger().setLevel(log4j.LogManager.getRootLogger().setLevel(log4j.Level.WARN))
       
        #print("The value of sc._jsc.sc().isStopped() ::",sc._jsc.sc().isStopped())
        #print("The value of sc.isStopped ::",sc.isStopped())
        return sc
    except Exception as e:
         print (str(datetime.datetime.now()) + "____________Spark Context creation Failed________________")
         
         
def publishSCP(fileAbsPathName,user,password,serverDetails,destinationPath):
    try:
       return os.system("scp FILE USER@SERVER:PATH")
   #os.system('scp "%s" "%s:%s"' % (fileAbsPathName, remotehost, remotefile) )
   #os.system("scp API-0.0.1-SNAPSHOT.war user@serverIp:/path")
    except Exception as e:
      print (str(datetime.datetime.now()) + "____________Spark Context creation Failed________________")   

      
def uploadFileFTP(server, username, password,sourceFilePath,destinationFileName,destinationDirectory ):
    #print("the details are : server : %s username : %s password : %s"% (server, username, password))
    myFTP = ftplib.FTP(server, username, password)
    print ("The present working directory is ::"+myFTP.pwd())
    # Changing Working Directory
    myFTP.cwd(destinationDirectory)
    print ("Changing the working directory to ::"+myFTP.pwd())
    print("The source file path is ::"+sourceFilePath)
    if os.path.isfile(sourceFilePath):
        fh = open(sourceFilePath, 'rb')
        print ("The file name is "+destinationFileName)
        myFTP.storbinary('STOR %s' % destinationFileName, fh)
        fh.close()
        myFTP.quit()
        print("File has been successfully processed")
    else:
        print "Source File does not exist"           
                 