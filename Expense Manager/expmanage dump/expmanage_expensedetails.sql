-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: expmanage
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `expensedetails`
--

DROP TABLE IF EXISTS `expensedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expensedetails` (
  `Srno` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Description` varchar(45) NOT NULL,
  `credit` varchar(45) DEFAULT NULL,
  `debit` varchar(45) DEFAULT NULL,
  `category` varchar(45) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`Srno`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expensedetails`
--

LOCK TABLES `expensedetails` WRITE;
/*!40000 ALTER TABLE `expensedetails` DISABLE KEYS */;
INSERT INTO `expensedetails` VALUES (12,'2021-05-12','Jupiter Hospital',NULL,'8600','medical',10008),(13,'2021-05-10','MRI Scan',NULL,'28900','medical',10008),(14,'2021-05-08','Fuel tank refill',NULL,'3500','vehicle',10008),(15,'2021-05-01','Monthly salary','95000',NULL,'salary',10008),(16,'2021-05-03','Trends and H&M',NULL,'9500','clothing',10008),(17,'2021-03-02','Birthday party ',NULL,'6500','Restaurant',10008),(21,'2021-04-01','Monthly salary','95000',NULL,'salary',10008),(22,'2021-03-01','Monthly salary','95000',NULL,'salary',10008),(23,'2021-02-01','Monthly salary','95000',NULL,'salary',10008),(24,'2021-01-01','Monthly salary','95000',NULL,'salary',10008),(25,'2021-04-02','Blood tests',NULL,'4550','medical',10008),(26,'2021-03-04','Yearly Checkup',NULL,'9600','medical',10008),(27,'2021-02-18','medicines',NULL,'2500','medical',10008),(28,'2021-02-10','Health Insuarance',NULL,'36000','Insuarance',10008),(29,'2021-05-10','Credit card bill',NULL,'19000','Bills',10008),(30,'2021-04-10','Credit card bill',NULL,'35560','Bills',10008),(31,'2021-03-10','Credit card bill',NULL,'26500','Bills',10008),(32,'2021-05-14','Electricity Bill',NULL,'3500','Bills',10008),(33,'2021-03-11','Westside',NULL,'5500','clothing',10008),(34,'2021-03-25','Movie night',NULL,'3600','Entertainment ',10008),(35,'2021-05-04','Games',NULL,'3600','Entertainment ',10008),(37,'2021-05-14','Business Profit','156000',NULL,'Business ',10008),(38,'2021-05-14','Monthly Salary','125000',NULL,'salary',10009),(39,'2021-05-10','gorceries',NULL,'1560','grocery',10009),(40,'2021-05-10','credit card bill',NULL,'18600','Bills',10009),(41,'2021-05-14','Checkup',NULL,'2500','medical',10009),(44,'2021-05-16','Bonus','45000',NULL,'salary',10008);
/*!40000 ALTER TABLE `expensedetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-23 20:23:04
