# Snapbox API
Python Flask Rest API

## Run Mysql on Docker

docker run --name local-mysql -p 3306:3306 -v /var/lib/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=admin -d mysql:latest