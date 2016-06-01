# ElasticsearchPerformance
My performance measuring scripts

 - pip install MySQL-python
 - pip install requests
 - pip install elasticsearch
 - 
 - https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266
 - http://dev.mysql.com/downloads/connector/c/6.0.html#downloads
 - 
 
```
CREATE DATABASE  IF NOT EXISTS `forum`;
USE `forum`;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(150) DEFAULT NULL,
  `lastname` varchar(150) DEFAULT NULL,
  `username` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10002 DEFAULT CHARSET=utf8;
```
