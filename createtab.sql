-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: egg
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `client_management_device`
--

DROP TABLE IF EXISTS `client_management_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_sent` tinyint(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mac_address` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mysql_username` varchar(255) NOT NULL,
  `mysql_password` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `type_id` int(11) DEFAULT NULL,
  `building_id` int(11) DEFAULT NULL,
  `mysql_database` varchar(255) NOT NULL,
  `update_time` datetime(6) DEFAULT NULL,
  `error` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac_address` (`mac_address`),
  KEY `client_management_de_type_id_672a59fa_fk_client_ma` (`type_id`),
  CONSTRAINT `client_management_de_type_id_672a59fa_fk_client_ma` FOREIGN KEY (`type_id`) REFERENCES `client_management_devicetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_management_devicetype`
--

DROP TABLE IF EXISTS `client_management_devicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_devicetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `en_name` varchar(255) NOT NULL,
  `cn_name` varchar(255) NOT NULL,
  `device_id` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `device_id` (`device_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_management_pointlog`
--

DROP TABLE IF EXISTS `client_management_pointlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_pointlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(255) NOT NULL,
  `is_sent` tinyint(1) NOT NULL,
  `data` longtext NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_management_pointserver`
--

DROP TABLE IF EXISTS `client_management_pointserver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_pointserver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `host` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `freq` int(11) DEFAULT NULL,
  `device_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `filename` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `client_management_po_device_id_f864d745_fk_client_ma` (`device_id`),
  KEY `client_management_po_type_id_02d0e900_fk_client_ma` (`type_id`),
  CONSTRAINT `client_management_po_device_id_f864d745_fk_client_ma` FOREIGN KEY (`device_id`) REFERENCES `client_management_device` (`id`),
  CONSTRAINT `client_management_po_type_id_02d0e900_fk_client_ma` FOREIGN KEY (`type_id`) REFERENCES `client_management_pointservertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_management_pointservertype`
--

DROP TABLE IF EXISTS `client_management_pointservertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_pointservertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `folder` varchar(255) NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `auto_match` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_management_pointunit`
--

DROP TABLE IF EXISTS `client_management_pointunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_management_pointunit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(255) NOT NULL,
  `points` longtext NOT NULL,
  `point_server_id` int(11) NOT NULL,
  `fields` longtext NOT NULL,
  `args_dict` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_id` (`u_id`),
  KEY `client_management_po_point_server_id_c1790cc8_fk_client_ma` (`point_server_id`),
  CONSTRAINT `client_management_po_point_server_id_c1790cc8_fk_client_ma` FOREIGN KEY (`point_server_id`) REFERENCES `client_management_pointserver` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-17 17:07:55
