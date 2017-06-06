-- MySQL dump 10.13  Distrib 5.5.55, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: movieRental
-- ------------------------------------------------------
-- Server version	5.5.55-0+deb8u1

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
-- Table structure for table `Accounts`
--

DROP TABLE IF EXISTS `Accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Accounts` (
  `CustomerId` int(11) NOT NULL,
  `AccountNo` varchar(1) DEFAULT NULL,
  `AccountType` varchar(10) DEFAULT NULL,
  `AcctCreatDate` date DEFAULT NULL,
  `Movie` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`CustomerId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts`
--

LOCK TABLES `Accounts` WRITE;
/*!40000 ALTER TABLE `Accounts` DISABLE KEYS */;
INSERT INTO `Accounts` VALUES (222222222,'2','limited','0000-00-00','2'),(444444444,'1','unlimited','2010-01-06','1');
/*!40000 ALTER TABLE `Accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actors`
--

DROP TABLE IF EXISTS `Actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Actors` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) DEFAULT NULL,
  `Gender` varchar(2) DEFAULT NULL,
  `Age` varchar(3) DEFAULT NULL,
  `Movies` varchar(100) DEFAULT NULL,
  `Rating` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Name_UNIQUE` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actors`
--

LOCK TABLES `Actors` WRITE;
/*!40000 ALTER TABLE `Actors` DISABLE KEYS */;
INSERT INTO `Actors` VALUES (1,'actor_3_name','M','45','','3'),(2,'CCH Pounder','M','59','tt0499549','0'),(3,'Joel David Moore','M','60','tt0499549','3'),(4,'Wes Studi','M','60','tt0499549','3'),(5,'Johnny Depp','M','22','tt0449088|tt0383574|tt1210819|tt1298650|tt1014759','5'),(6,'Orlando Bloom','M','28','tt0449088|tt0383574','5'),(7,'Jack Davenport','M','40','tt0449088|tt0383574','1'),(8,'Christoph Waltz','M','57','tt2379713','2'),(9,'Rory Kinnear','M','39','tt2379713|tt0830515|tt1074638','0'),(10,'Stephanie Sigman','M','35','tt2379713','4'),(11,'Tom Hardy','M','22','tt1345836','0'),(12,'Christian Bale','M','51','tt1345836|tt0438488','5'),(13,'Joseph Gordon-Levitt','M','24','tt1345836','1'),(14,'Doug Walker','M','32','tt5289954','2'),(15,'Rob Walker','M','59','tt5289954','1'),(16,'','M','43','tt5289954','3'),(17,'Daryl Sabara','M','57','tt0401729','3'),(18,'Samantha Morton','M','35','tt0401729','1'),(19,'Polly Walker','M','45','tt0401729','3'),(20,'J.K. Simmons','M','31','tt0413300|tt0316654','3'),(21,'James Franco','M','37','tt0413300|tt0316654|tt1623205','2'),(22,'Kirsten Dunst','M','57','tt0413300|tt0316654','0'),(23,'Brad Garrett','M','46','tt0398286','3'),(24,'Donna Murphy','M','28','tt0398286','1'),(25,'M.C. Gainey','M','60','tt0398286','3'),(26,'Chris Hemsworth','M','55','tt2395427|tt0848228','4'),(27,'Robert Downey Jr.','M','21','tt2395427|tt0848228|tt3498820|tt1300854','3'),(28,'Scarlett Johansson','M','60','tt2395427|tt0848228|tt3498820','2'),(29,'Alan Rickman','M','20','tt0417741|tt1014759','1'),(30,'Daniel Radcliffe','M','26','tt0417741','2'),(31,'Rupert Grint','M','49','tt0417741','2'),(32,'Henry Cavill','M','28','tt2975590|tt0770828','1'),(33,'Lauren Cohan','M','34','tt2975590','5'),(34,'Alan D. Purwin','M','39','tt2975590','0'),(35,'Kevin Spacey','M','24','tt0348150','3'),(36,'Marlon Brando','M','53','tt0348150','0'),(37,'Frank Langella','M','54','tt0348150','0'),(38,'Giancarlo Giannini','M','34','tt0830515','5'),(39,'Mathieu Amalric','M','60','tt0830515','1'),(40,'Ruth Wilson','M','49','tt1210819','5'),(41,'Tom Wilkinson','M','45','tt1210819','1'),(42,'Christopher Meloni','M','41','tt0770828','2'),(43,'Harry Lennix','M','30','tt0770828','4'),(44,'Peter Dinklage','M','29','tt0499448|tt1877832','2'),(45,'Pierfrancesco Favino','M','28','tt0499448','1'),(46,'DamiÃ¡n AlcÃ¡zar','M','44','tt0499448','3'),(47,'Sam Claflin','M','48','tt1298650','0'),(48,'Stephen Graham','M','38','tt1298650','0'),(49,'Will Smith','M','60','tt1409024','5'),(50,'Michael Stuhlbarg','M','54','tt1409024','3'),(51,'Nicole Scherzinger','M','42','tt1409024','0'),(52,'Aidan Turner','M','57','tt2310332|tt1170358','0'),(53,'Adam Brown','M','37','tt2310332|tt1170358','5'),(54,'James Nesbitt','M','18','tt2310332|tt1170358','2'),(55,'Emma Stone','M','31','tt0948470|tt1872181','2'),(56,'Andrew Garfield','M','50','tt0948470|tt1872181','4'),(57,'Chris Zylka','M','43','tt0948470','3'),(58,'Mark Addy','M','46','tt0955308','3'),(59,'William Hurt','M','54','tt0955308','5'),(60,'Scott Grimes','M','29','tt0955308','5'),(61,'Christopher Lee','M','45','tt0385752','0'),(62,'Eva Green','M','31','tt0385752','0'),(63,'Kristin Scott Thomas','M','43','tt0385752','3'),(64,'Naomi Watts','M','48','tt0360717','0'),(65,'Thomas Kretschmann','M','49','tt0360717|tt1216475','4'),(66,'Evan Parke','M','45','tt0360717','4'),(67,'Leonardo DiCaprio','M','20','tt0120338|tt1343092','3'),(68,'Kate Winslet','M','33','tt0120338','4'),(69,'Gloria Stuart','M','51','tt0120338','2'),(70,'Chris Evans','M','32','tt3498820','3'),(71,'Liam Neeson','M','44','tt1440129','1'),(72,'Alexander SkarsgÃ¥rd','M','38','tt1440129','4'),(73,'Tadanobu Asano','M','30','tt1440129','1'),(74,'Bryce Dallas Howard','M','19','tt0369610|tt0438488','5'),(75,'Judy Greer','M','54','tt0369610','1'),(76,'Omar Sy','M','20','tt0369610','0'),(77,'Albert Finney','M','22','tt1074638','2'),(78,'Helen McCrory','M','32','tt1074638','2'),(79,'Jon Favreau','M','43','tt1300854','1'),(80,'Don Cheadle','M','33','tt1300854','4'),(81,'Anne Hathaway','M','38','tt1014759','0'),(82,'Hugh Jackman','M','21','tt0376994|tt1877832','5'),(83,'Kelsey Grammer','M','59','tt0376994|tt2109248','5'),(84,'Daniel Cudmore','M','37','tt0376994','0'),(85,'Steve Buscemi','M','36','tt1453405','1'),(86,'Tyler Labine','M','51','tt1453405','2'),(87,'Sean Hayes','M','29','tt1453405','2'),(88,'Glenn Morshower','M','28','tt1055369|tt1399103','2'),(89,'Kevin Dunn','M','30','tt1055369|tt1399103','2'),(90,'Ramon Rodriguez','M','47','tt1055369','5'),(91,'Bingbing Li','M','28','tt2109248','4'),(92,'Sophia Myles','M','58','tt2109248','4'),(93,'Tim Holmes','M','57','tt1623205','0'),(94,'Mila Kunis','M','35','tt1623205','0'),(95,'B.J. Novak','M','35','tt1872181','3'),(96,'Jeff Bridges','M','21','tt1104001','3'),(97,'Olivia Wilde','M','38','tt1104001','3'),(98,'James Frain','M','42','tt1104001','3'),(99,'Joe Mantegna','M','53','tt1216475','1'),(100,'Eddie Izzard','M','36','tt1216475','2'),(101,'Ryan Reynolds','M','43','tt1133985','4'),(102,'Temuera Morrison','M','54','tt1133985','3'),(103,'Taika Waititi','M','37','tt1133985','1'),(104,'Tom Hanks','M','36','tt0435761','3'),(105,'John Ratzenberger','M','25','tt0435761|tt1217209','5'),(106,'Don Rickles','M','47','tt0435761','1'),(107,'Common','M','33','tt0438488','4'),(108,'Jason Statham','M','31','tt2820852','3'),(109,'Paul Walker','M','29','tt2820852','5'),(110,'Vin Diesel','M','35','tt2820852','5'),(111,'Peter Capaldi','M','22','tt0816711','2'),(112,'Brad Pitt','M','54','tt0816711','4'),(113,'Mireille Enos','M','34','tt0816711','5'),(114,'Jennifer Lawrence','M','57','tt1877832','4'),(115,'Benedict Cumberbatch','M','23','tt1408101','3'),(116,'Bruce Greenwood','M','50','tt1408101','5'),(117,'Noel Clarke','M','53','tt1408101','0'),(118,'Eddie Marsan','M','32','tt1351685','1'),(119,'Ewen Bremner','M','59','tt1351685','5'),(120,'Ralph Brown','M','44','tt1351685','0'),(121,'Elizabeth Debicki','M','25','tt1343092','2'),(122,'Steve Bisley','M','53','tt1343092','4'),(123,'Jake Gyllenhaal','M','43','tt0473075','5'),(124,'Richard Coyle','M','47','tt0473075','0'),(125,'Reece Ritchie','M','27','tt0473075','0'),(126,'Charlie Hunnam','M','25','tt1663662','5'),(127,'Clifton Collins Jr.','M','51','tt1663662','3'),(128,'Larry Joe Campbell','M','36','tt1663662','3'),(129,'Lester Speight','M','35','tt1399103','5'),(130,'Harrison Ford','M','34','tt0367882','3'),(131,'Ray Winstone','M','59','tt0367882','5'),(132,'Jim Broadbent','M','23','tt0367882','1'),(133,'A.J. Buckley','M','43','tt1979388','2'),(134,'Jack McGraw','M','57','tt1979388','2'),(135,'Peter Sohn','M','18','tt1979388','4'),(136,'Kelly Macdonald','M','24','tt1217209','1'),(137,'Julie Walters','M','55','tt1217209','1'),(138,'Sofia Boutella','M','52','tt2660888','0'),(139,'Melissa Roxburgh','M','36','tt2660888','5'),(140,'Lydia Wilson','M','38','tt2660888','1');
/*!40000 ALTER TABLE `Actors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `CustomerId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `LastName` varchar(20) DEFAULT NULL,
  `FirstName` varchar(10) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` varchar(2) DEFAULT NULL,
  `ZipCode` varchar(12) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `CreditCard` varchar(15) DEFAULT NULL,
  `Telephone` varchar(20) DEFAULT NULL,
  `hashPassword` varchar(20) DEFAULT NULL,
  `AccountType` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CustomerId`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'Werellagama','Nuwan','119','Stony Brook','NY','11790','nuwanwre@live.com','1234567890','0101234567','1','limited'),(3,'Werellagama','Nuwan','119','Stony Brook','NY','11790','sri','1234567890','0101234567','12','limited');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movies`
--

DROP TABLE IF EXISTS `Movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Movies` (
  `Id` varchar(10) NOT NULL,
  `Director` varchar(45) DEFAULT NULL,
  `Duration` varchar(45) DEFAULT NULL,
  `Actors` varchar(100) DEFAULT NULL,
  `Genre` varchar(100) DEFAULT NULL,
  `Title` varchar(100) DEFAULT NULL,
  `Rating` varchar(5) DEFAULT NULL,
  `Description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id_UNIQUE` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movies`
--

LOCK TABLES `Movies` WRITE;
/*!40000 ALTER TABLE `Movies` DISABLE KEYS */;
INSERT INTO `Movies` VALUES ('tt0120338','James Cameron','194','Leonardo DiCaprio|Kate Winslet|Gloria Stuart','Drama|Romance','Titanic','7.7','A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.'),('tt0316654','Sam Raimi','135','J.K. Simmons|James Franco|Kirsten Dunst','Action|Adventure|Fantasy|Romance','Spider-Man 2','7.3','Peter Parker is beset with troubles in his failing personal life as he battles a brilliant scientist named Doctor Otto Octavius.'),('tt0348150','Bryan Singer','169','Kevin Spacey|Marlon Brando|Frank Langella','Action|Adventure|Sci-Fi','Superman Returns','6.1','Superman reappears after a long absence, but is challenged by an old foe who uses Kryptonian technology for world domination.'),('tt0360717','Peter Jackson','201','Naomi Watts|Thomas Kretschmann|Evan Parke','Action|Adventure|Drama|Romance','King Kong','7.2','A movie crew, travelling to a mysterious island to shoot their picture, encounter a furious gorilla, taking their leading actress and forming a special relationship with her, protecting her at all cos'),('tt0367882','Steven Spielberg','122','Harrison Ford|Ray Winstone|Jim Broadbent','Action|Adventure|Fantasy','Indiana Jones and the Kingdom of the Crystal Skull','6.2','Famed archaeologist/adventurer Dr. Henry \"Indiana\" Jones is called back into action when he becomes entangled in a Soviet plot to uncover the secret behind mysterious artifacts known as the Crystal Sk'),('tt0369610','Colin Trevorrow','124','Bryce Dallas Howard|Judy Greer|Omar Sy','Action|Adventure|Sci-Fi|Thriller','Jurassic World','7.0','A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree.'),('tt0376994','Brett Ratner','104','Hugh Jackman|Kelsey Grammer|Daniel Cudmore','Action|Adventure|Fantasy|Sci-Fi|Thriller','X-Men: The Last Stand','6.8','When a cure is found to treat mutations, lines are drawn amongst the X-Men, led by Professor Charles Xavier, and the Brotherhood, a band of powerful mutants organized under Xavier\'s former ally, Magne'),('tt0383574','Gore Verbinski','151','Johnny Depp|Orlando Bloom|Jack Davenport','Action|Adventure|Fantasy','Pirates of the Caribbean: Dead Man\'s Chest','7.3','Jack Sparrow races to recover the heart of Davy Jones to avoid enslaving his soul to Jones\' service, as other friends and foes seek the heart for their own agenda as well.'),('tt0385752','Chris Weitz','113','Christopher Lee|Eva Green|Kristin Scott Thomas','Adventure|Family|Fantasy','The Golden Compass','6.1','In a parallel universe, young Lyra Belacqua journeys to the far North to save her best friend and other kidnapped children from terrible experiments by a mysterious organization.'),('tt0398286','Nathan Greno','100','Brad Garrett|Donna Murphy|M.C. Gainey','Adventure|Animation|Comedy|Family|Fantasy|Musical|Romance','Tangled','7.8','The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really i'),('tt0401729','Andrew Stanton','132','Daryl Sabara|Samantha Morton|Polly Walker','Action|Adventure|Sci-Fi','John Carter','6.6','Transported to Barsoom, a Civil War vet discovers a barren planet seemingly inhabited by 12-foot tall barbarians. Finding himself prisoner of these creatures, he escapes, only to encounter Woola and a'),('tt0413300','Sam Raimi','156','J.K. Simmons|James Franco|Kirsten Dunst','Action|Adventure|Romance','Spider-Man 3','6.2','A strange black entity from another world bonds with Peter Parker and causes inner turmoil as he contends with new villains, temptations, and revenge.'),('tt0417741','David Yates','153','Alan Rickman|Daniel Radcliffe|Rupert Grint','Adventure|Family|Fantasy|Mystery','Harry Potter and the Half-Blood Prince','7.5','As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as \"the property of the Half-Blood Prince\" and begins to learn more about Lord Voldemort\'s dark past.'),('tt0435761','Lee Unkrich','103','Tom Hanks|John Ratzenberger|Don Rickles','Adventure|Animation|Comedy|Family|Fantasy','Toy Story 3','8.3','The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it\'s up to Woody to convince the other toys that they weren\'t abandoned and to ret'),('tt0438488','McG','118','Christian Bale|Bryce Dallas Howard|Common','Action|Adventure|Sci-Fi','Terminator Salvation','6.6','In 2018, a mysterious new weapon in the war against the machines, half-human and half-machine, comes to John Connor on the eve of a resistance attack on Skynet. But whose side is he on, and can he be '),('tt0449088','Gore Verbinski','169','Johnny Depp|Orlando Bloom|Jack Davenport','Action|Adventure|Fantasy','Pirates of the Caribbean: At World\'s End','7.1','Captain Barbossa, Will Turner and Elizabeth Swann must sail off the edge of the map, navigate treachery and betrayal, find Jack Sparrow, and make their final alliances for one last decisive battle.'),('tt0473075','Mike Newell','116','Jake Gyllenhaal|Richard Coyle|Reece Ritchie','Action|Adventure|Fantasy|Romance','Prince of Persia: The Sands of Time','6.6','A young fugitive prince and princess must stop a villain who unknowingly threatens to destroy the world with a special dagger that enables the magic sand inside to reverse time.'),('tt0499448','Andrew Adamson','150','Peter Dinklage|Pierfrancesco Favino|DamiÃ¡n AlcÃ¡zar','Action|Adventure|Family|Fantasy','The Chronicles of Narnia: Prince Caspian','6.6','The Pevensie siblings return to Narnia, where they are enlisted to once again help ward off an evil king and restore the rightful heir to the land\'s throne, Prince Caspian.'),('tt0499549','James Cameron','178','CCH Pounder|Joel David Moore|Wes Studi','Action|Adventure|Fantasy|Sci-Fi','Avatar','7.9','A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.'),('tt0770828','Zack Snyder','143','Henry Cavill|Christopher Meloni|Harry Lennix','Action|Adventure|Fantasy|Sci-Fi','Man of Steel','7.2','Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet '),('tt0816711','Marc Forster','123','Peter Capaldi|Brad Pitt|Mireille Enos','Action|Adventure|Horror|Sci-Fi|Thriller','World War Z','7.0','Former United Nations employee Gerry Lane traverses the world in a race against time to stop the Zombie pandemic that is toppling armies and governments, and threatening to destroy humanity itself.'),('tt0830515','Marc Forster','106','Giancarlo Giannini|Mathieu Amalric|Rory Kinnear','Action|Adventure','Quantum of Solace','6.7','James Bond descends into mystery as he tries to stop a mysterious organization from eliminating a country\'s most valuable resource. All the while, he still tries to seek revenge over the death of his '),('tt0848228','Joss Whedon','173','Chris Hemsworth|Robert Downey Jr.|Scarlett Johansson','Action|Adventure|Sci-Fi','The Avengers','8.1','Earth\'s mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.'),('tt0948470','Marc Webb','153','Emma Stone|Andrew Garfield|Chris Zylka','Action|Adventure|Fantasy','The Amazing Spider-Man','7.0','After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to solve the mystery of his parent\'s mysterious death.'),('tt0955308','Ridley Scott','156','Mark Addy|William Hurt|Scott Grimes','Action|Adventure|Drama|History','Robin Hood','6.7','In 12th century England, Robin and his band of marauders confront corruption in a local village and lead an uprising against the crown that will forever alter the balance of world power.'),('tt1014759','Tim Burton','108','Johnny Depp|Alan Rickman|Anne Hathaway','Adventure|Family|Fantasy','Alice in Wonderland','6.5','Nineteen-year-old Alice returns to the magical world from her childhood adventure, where she reunites with her old friends and learns of her true destiny: to end the Red Queen\'s reign of terror.'),('tt1055369','Michael Bay','150','Glenn Morshower|Kevin Dunn|Ramon Rodriguez','Action|Adventure|Sci-Fi','Transformers: Revenge of the Fallen','6.0','Sam Witwicky leaves the Autobots behind for a normal life. But when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers\' war.'),('tt1074638','Sam Mendes','143','Albert Finney|Helen McCrory|Rory Kinnear','Action|Adventure|Thriller','Skyfall','7.8','Bond\'s loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost.'),('tt1104001','Joseph Kosinski','125','Jeff Bridges|Olivia Wilde|James Frain','Action|Adventure|Sci-Fi','TRON: Legacy','6.8','The son of a virtual world designer goes looking for his father and ends up inside the digital world that his father designed. He meets his father\'s corrupted creation and a unique ally who was born i'),('tt1133985','Martin Campbell','123','Ryan Reynolds|Temuera Morrison|Taika Waititi','Action|Adventure|Sci-Fi','Green Lantern','5.6','Reckless test pilot Hal Jordan is granted an alien ring that bestows him with otherworldly powers that inducts him into an intergalactic police force, the Green Lantern Corps.'),('tt1170358','Peter Jackson','186','Aidan Turner|Adam Brown|James Nesbitt','Adventure|Fantasy','The Hobbit: The Desolation of Smaug','7.9','The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.'),('tt1210819','Gore Verbinski','150','Johnny Depp|Ruth Wilson|Tom Wilkinson','Action|Adventure|Western','The Lone Ranger','6.5','Native American warrior Tonto recounts the untold tales that transformed John Reid, a man of the law, into a legend of justice.'),('tt1216475','John Lasseter','106','Joe Mantegna|Thomas Kretschmann|Eddie Izzard','Adventure|Animation|Comedy|Family|Sport','Cars 2','6.3','Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventu'),('tt1217209','Mark Andrews','93','Kelly Macdonald|John Ratzenberger|Julie Walters','Adventure|Animation|Comedy|Family|Fantasy','Brave','7.2','Determined to make her own path in life, Princess Merida defies a custom that brings chaos to her kingdom. Granted one wish, Merida must rely on her bravery and her archery skills to undo a beastly cu'),('tt1298650','Rob Marshall','136','Johnny Depp|Sam Claflin|Stephen Graham','Action|Adventure|Fantasy','Pirates of the Caribbean: On Stranger Tides','6.7','Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth, only to discover that Blackbeard and his daughter are after it too.'),('tt1300854','Shane Black','195','Robert Downey Jr.|Jon Favreau|Don Cheadle','Action|Adventure|Sci-Fi','Iron Man 3','7.2','When Tony Stark\'s world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.'),('tt1343092','Baz Luhrmann','143','Leonardo DiCaprio|Elizabeth Debicki|Steve Bisley','Drama|Romance','The Great Gatsby','7.3','A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his millionaire neighbor, Jay Gatsby.'),('tt1345836','Christopher Nolan','164','Tom Hardy|Christian Bale|Joseph Gordon-Levitt','Action|Thriller','The Dark Knight Rises','8.5','Eight years after the Joker\'s reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, fro'),('tt1351685','Bryan Singer','114','Eddie Marsan|Ewen Bremner|Ralph Brown','Adventure|Fantasy','Jack the Giant Slayer','6.3','The ancient war between humans and a race of giants is reignited when Jack, a young farmhand fighting for a kingdom and the love of a princess, opens a gateway between the two worlds.'),('tt1399103','Michael Bay','154','Glenn Morshower|Lester Speight|Kevin Dunn','Action|Adventure|Sci-Fi','Transformers: Dark of the Moon','6.3','The Autobots learn of a Cybertronian spacecraft hidden on the moon, and race against the Decepticons to reach it and to learn its secrets.'),('tt1408101','J.J. Abrams','132','Benedict Cumberbatch|Bruce Greenwood|Noel Clarke','Action|Adventure|Sci-Fi','Star Trek Into Darkness','7.8','After the crew of the Enterprise find an unstoppable force of terror from within their own organization, Captain Kirk leads a manhunt to a war-zone world to capture a one-man weapon of mass destructio'),('tt1409024','Barry Sonnenfeld','106','Will Smith|Michael Stuhlbarg|Nicole Scherzinger','Action|Adventure|Comedy|Family|Fantasy|Sci-Fi','Men in Black 3','6.8','Agent J travels in time to M.I.B.\'s early days in 1969 to stop an alien from assassinating his friend Agent K and changing history.'),('tt1440129','Peter Berg','131','Liam Neeson|Alexander SkarsgÃ¥rd|Tadanobu Asano','Action|Adventure|Sci-Fi|Thriller','Battleship','5.9','A fleet of ships is forced to do battle with an armada of unknown origins in order to discover and thwart their destructive goals.'),('tt1453405','Dan Scanlon','104','Steve Buscemi|Tyler Labine|Sean Hayes','Adventure|Animation|Comedy|Family|Fantasy','Monsters University','7.3','A look at the relationship between Mike and Sulley during their days at Monsters University -- when they weren\'t necessarily the best of friends.'),('tt1623205','Sam Raimi','130','Tim Holmes|Mila Kunis|James Franco','Adventure|Family|Fantasy','Oz the Great and Powerful','6.4','A frustrated circus magician from Kansas is transported to a magical land called Oz, where he will have to fulfill a prophecy to become the king, and release the land from the Wicked Witches using his'),('tt1663662','Guillermo del Toro','131','Charlie Hunnam|Clifton Collins Jr.|Larry Joe Campbell','Action|Adventure|Sci-Fi','Pacific Rim','7.0','As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from th'),('tt1872181','Marc Webb','142','Emma Stone|Andrew Garfield|B.J. Novak','Action|Adventure|Fantasy|Sci-Fi','The Amazing Spider-Man 2','6.7','When New York is put under siege by Oscorp, it is up to Spider-Man to save the city he swore to protect as well as his loved ones.'),('tt1877832','Bryan Singer','149','Jennifer Lawrence|Peter Dinklage|Hugh Jackman','Action|Adventure|Fantasy|Sci-Fi|Thriller','X-Men: Days of Future Past','8.0','The X-Men send Wolverine to the past in a desperate effort to change history and prevent an event that results in doom for both humans and mutants.'),('tt1979388','Peter Sohn','93','A.J. Buckley|Jack McGraw|Peter Sohn','Adventure|Animation|Comedy|Family|Fantasy','The Good Dinosaur','6.8','In a world where dinosaurs and humans live side-by-side, an Apatosaurus named Arlo makes an unlikely human friend.'),('tt2109248','Michael Bay','165','Bingbing Li|Sophia Myles|Kelsey Grammer','Action|Adventure|Sci-Fi','Transformers: Age of Extinction','5.7','Autobots must escape sight from a bounty hunter who has taken control of the human serendipity: Unexpectedly, Optimus Prime and his remaining gang turn to a mechanic, his daughter, and her back street'),('tt2310332','Peter Jackson','164','Aidan Turner|Adam Brown|James Nesbitt','Adventure|Fantasy','The Hobbit: The Battle of the Five Armies','7.5','Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'),('tt2379713','Sam Mendes','148','Christoph Waltz|Rory Kinnear|Stephanie Sigman','Action|Adventure|Thriller','Spectre','6.8','A cryptic message from Bond\'s past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to r'),('tt2395427','Joss Whedon','141','Chris Hemsworth|Robert Downey Jr.|Scarlett Johansson','Action|Adventure|Sci-Fi','Avengers: Age of Ultron','7.5','When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it\'s up to Earth\'s mightiest heroes to stop the villainous Ultron from ena'),('tt2660888','Justin Lin','122','Sofia Boutella|Melissa Roxburgh|Lydia Wilson','Action|Adventure|Sci-Fi|Thriller','Star Trek Beyond','7.5','The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy who puts them and everything the Federation stands for to the test.'),('tt2820852','James Wan','140','Jason Statham|Paul Walker|Vin Diesel','Action|Crime|Thriller','Furious 7','7.2','Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.'),('tt2975590','Zack Snyder','183','Henry Cavill|Lauren Cohan|Alan D. Purwin','Action|Adventure|Sci-Fi','Batman v Superman: Dawn of Justice','6.9','Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.'),('tt3498820','Anthony Russo','147','Robert Downey Jr.|Scarlett Johansson|Chris Evans','Action|Adventure|Sci-Fi','Captain America: Civil War','8.2','Political interference in the Avengers\' activities causes a rift between former allies Captain America and Iron Man.'),('tt5289954','Doug Walker','','Doug Walker|Rob Walker|','Documentary','Star Wars: Episode VII - The Force AwakensÂ           ','7.1','Add a PlotÂ Â»');
/*!40000 ALTER TABLE `Movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Orders` (
  `OrderId` int(11) NOT NULL,
  `Account` tinyint(4) DEFAULT NULL,
  `Movie` tinyint(4) DEFAULT NULL,
  `DateTime` date DEFAULT NULL,
  `ReturnDate` date DEFAULT NULL,
  PRIMARY KEY (`OrderId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1,1,1,'2011-11-09','0000-00-00'),(2,2,3,'2011-11-09',NULL),(3,1,3,'2011-12-09',NULL),(4,2,2,'2011-12-09',NULL);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Queue`
--

DROP TABLE IF EXISTS `Queue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Queue` (
  `QueueId` int(11) NOT NULL,
  `CustomerId` varchar(45) DEFAULT NULL,
  `MovieId` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`QueueId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Queue`
--

LOCK TABLES `Queue` WRITE;
/*!40000 ALTER TABLE `Queue` DISABLE KEYS */;
INSERT INTO `Queue` VALUES (1,'111111111','1'),(2,'111111111','2'),(3,'222222222','3'),(4,'222222222','2'),(5,'333333333','1');
/*!40000 ALTER TABLE `Queue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `StarsIn`
--

DROP TABLE IF EXISTS `StarsIn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `StarsIn` (
  `actorId` int(11) NOT NULL,
  `MovieId` varchar(45) NOT NULL,
  PRIMARY KEY (`actorId`,`MovieId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `StarsIn`
--

LOCK TABLES `StarsIn` WRITE;
/*!40000 ALTER TABLE `StarsIn` DISABLE KEYS */;
INSERT INTO `StarsIn` VALUES (1,'1'),(1,'3'),(2,'1');
/*!40000 ALTER TABLE `StarsIn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suggestions`
--

DROP TABLE IF EXISTS `Suggestions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Suggestions` (
  `CustomerId` int(11) NOT NULL,
  `MovieId` varchar(45) NOT NULL,
  PRIMARY KEY (`CustomerId`,`MovieId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suggestions`
--

LOCK TABLES `Suggestions` WRITE;
/*!40000 ALTER TABLE `Suggestions` DISABLE KEYS */;
INSERT INTO `Suggestions` VALUES (111111111,'1'),(222222222,'1'),(333333333,'2'),(333333333,'3');
/*!40000 ALTER TABLE `Suggestions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-06 15:43:38
