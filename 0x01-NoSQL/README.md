```Back-end``` ```NoSQL``` ```MongoDB```

# Requirements
# MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using ```MongoDB``` (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: ```// my comment```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using ```wc```

### When working with docker container, the command ```sudo systemctl start mongod``` throws the error ```System has not been booted with systemd as init system (PID 1). Can't operate.```

| Systemd command | Sysvinit command |
| -------------- | ---------------- |
| systemctl start service_name | service service_name start |
| systemctl stop service_name | service service_name stop |
| systemctl restart service_name | service service_name restart |
| systemctl status service_name | service service_name status |
| systemctl enable service_name | chkconfig service_name on |
| systemctl disable service_name | chkconfig service_name off |


- I seemed to get over the issues with ```systemctl``` and ```service``` somehow.
- Trying to run ```mongo``` led to the error
```
MongoDB shell version v4.2.23
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
2023-01-17T08:25:39.554+0100 E  QUERY    [js] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed: SocketException: Error connecting to 127.0.0.1:27017 :: caused by :: Connection refused :
connect@src/mongo/shell/mongo.js:353:17
@(connect):2:6
2023-01-17T08:25:39.555+0100 F  -        [main] exception: connect failed
2023-01-17T08:25:39.555+0100 E  -        [main] exiting with code 1
```

## solution -> docker containers
- pull the mongo image from docker with specific version set to 4.2 as specified in the project. use the command
	- ```docker pull mongo:4.2```
	- the upside to this is that it runs on ubuntu 18.04 also a the ubuntu project requirement.
	- you then run the mongo:4.2 image, execute the container and install the needed packages you need with ```apt-get install <pkg_name>```. 
	- Note: you will need to install git, vim and python3
	- also make sure to name the container to a something you short and simple.
