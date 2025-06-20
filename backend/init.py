import pymysql
from pymysql.constants import CLIENT
import os

# Fetch DB credentials from environment or hardcode for setup phase
db_root_user = os.getenv("DB_USER", "root")
db_root_password = os.getenv("DB_PASSWORD", "your_root_password")
db_host = os.getenv("DB_HOST", "db")
db_port = int(os.getenv("DB_PORT", 3306))
database = "speakint"

connection = pymysql.connect(host=db_host, user=db_root_user, password=db_root_password, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, client_flag=CLIENT.MULTI_STATEMENTS, port=db_port)

try:
    with connection.cursor() as cursor:
        # Create database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print(f"Database `{database}` ensured.")

        # Select the database
        cursor.execute(f"USE `{database}`;")
        
        # Now execute your table creation statements and other SQL commands
        #Create the `finding_word` table
        cursor.execute("""
        DROP TABLE IF EXISTS `finding_word`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `finding_word` (
            `id` int NOT NULL AUTO_INCREMENT,
            `word` varchar(255) DEFAULT NULL,
            `file_name` varchar(255) DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            `F_date` varchar(255) DEFAULT NULL,
            `F_Time` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `finding_word` created or already exists.")

        # Lock the table and disable/enable keys as per your SQL file
        cursor.execute("""
        LOCK TABLES `finding_word` WRITE;
        /*!40000 ALTER TABLE `finding_word` DISABLE KEYS */;
        /*!40000 ALTER TABLE `finding_word` ENABLE KEYS */;
        UNLOCK TABLES
        """)
        
        # Repeat for all other tables using the CREATE TABLE statements from your SQL file,
        # preserving the comments as Python comments above each execution.
        
        # Create the `findings` table
        cursor.execute("""
        DROP TABLE IF EXISTS `findings`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `findings` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `F_Notification` varchar(255) DEFAULT NULL,
            `F_Date` varchar(255) DEFAULT NULL,
            `F_Time` varchar(255) DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            `FILENAME` varchar(255) DEFAULT NULL,
            `f_words` text,
            PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `findings` created or already exists.")

        # Lock the findings table and disable/enable keys
        cursor.execute("""
        LOCK TABLES `findings` WRITE;
        /*!40000 ALTER TABLE `findings` DISABLE KEYS */;
        /*!40000 ALTER TABLE `findings` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        # Create the `notification` table
        cursor.execute("""
        DROP TABLE IF EXISTS `notification`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `notification` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `Notifications` varchar(255) DEFAULT NULL,
            `N_Status` int DEFAULT NULL,
            `N_date` date DEFAULT NULL,
            `N_Time` time DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            `Notification_Category` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `notification` created or already exists.")

        cursor.execute("""
        LOCK TABLES `notification` WRITE;
        /*!40000 ALTER TABLE `notification` DISABLE KEYS */;
        /*!40000 ALTER TABLE `notification` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        #Create the `organization` table
        cursor.execute("""
        DROP TABLE IF EXISTS `organization`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `organization` (
            `Org_ID` int NOT NULL AUTO_INCREMENT,
            `Org_Name` varchar(255) DEFAULT NULL,
            `Created_On` datetime DEFAULT NULL,
            PRIMARY KEY (`Org_ID`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `organization` created or already exists.")

        cursor.execute("""
        LOCK TABLES `organization` WRITE;
        /*!40000 ALTER TABLE `organization` DISABLE KEYS */;
        /*!40000 ALTER TABLE `organization` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        #Create the `search` table
        cursor.execute("""
        DROP TABLE IF EXISTS `search`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `search` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `User_ID` int DEFAULT NULL,
            `Search_String` varchar(255) DEFAULT NULL,
            `Group_Name` varchar(50) DEFAULT NULL,
            `Processed` int DEFAULT NULL,
            `Result` text,
            `date_time` varchar(255) DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            `FILENAME` text,
            PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `search` created or already exists.")

        cursor.execute("""
        LOCK TABLES `search` WRITE;
        /*!40000 ALTER TABLE `search` DISABLE KEYS */;
        /*!40000 ALTER TABLE `search` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        #Create the `suspicious_words` table
        cursor.execute("""
        DROP TABLE IF EXISTS `suspicious_words`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `suspicious_words` (
            `Words` varchar(255) DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `suspicious_words` created or already exists.")

        cursor.execute("""
        LOCK TABLES `suspicious_words` WRITE;
        /*!40000 ALTER TABLE `suspicious_words` DISABLE KEYS */;
        /*!40000 ALTER TABLE `suspicious_words` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        #Create the `upload` table
        cursor.execute("""
        DROP TABLE IF EXISTS `upload`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `upload` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `Translated_Text` longtext,
            `Transcribed_Text` longtext,
            `Filename` varchar(1000) DEFAULT NULL,
            `File_Length` varchar(200) DEFAULT NULL,
            `NER` text,
            `WordCloud_path` varchar(300) DEFAULT NULL,
            `Upload_location` varchar(300) DEFAULT NULL,
            `Status` int DEFAULT NULL,
            `P_ID` int DEFAULT NULL,
            `Language` varchar(255) DEFAULT NULL,
            `Sentiment` varchar(255) DEFAULT NULL,
            `upload_date` varchar(255) DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            `wavConverted` varchar(255) DEFAULT NULL,
            `Media_Type` varchar(255) DEFAULT NULL,
            `hashVal` longtext,
            `FileError` text,
            `file_status` varchar(255) DEFAULT NULL,
            `original_speakers` text,
            `Hindi_Translation` longtext,
            `process_time` int DEFAULT NULL,
            PRIMARY KEY (`ID`),
            FULLTEXT KEY `idx_Translated_text` (`Translated_Text`),
            FULLTEXT KEY `idx_Transcribed_text` (`Transcribed_Text`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `upload` created or already exists.")

        cursor.execute("""
        LOCK TABLES `upload` WRITE;
        /*!40000 ALTER TABLE `upload` DISABLE KEYS */;
        /*!40000 ALTER TABLE `upload` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        #Create the `user_details` table
        cursor.execute("""
        DROP TABLE IF EXISTS `user_details`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `user_details` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `Usernames` varchar(255) NOT NULL,
            `Passcode` varchar(255) NOT NULL,
            `Category` varchar(10) DEFAULT NULL,
            `Active_Status` varchar(255) NOT NULL,
            `Enable_Status` varchar(255) NOT NULL,
            `AdminID` int DEFAULT NULL,
            `License_start` varchar(255) DEFAULT NULL,
            `License_end` varchar(255) DEFAULT NULL,
            `user_count` int DEFAULT NULL,
            `Organizations` varchar(255) DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `Languages` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `user_details` created or already exists.")

        cursor.execute("""
        LOCK TABLES `user_details` WRITE;
        /*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
        INSERT INTO `user_details` VALUES (163,'admin@pelorus.in','Pelorus@123','Admin','Inactive','Enable',2,'28-08-2024','30-10-2025',10,'Pelorus',NULL,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(164,'client@pelorus.in','Client@123','Client','Inactive','Enable',2,'24-06-2024','30-10-2025',NULL,'Pelorus',1,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(165,'tsintel1@pelorus.in','tsintel@123','Client','Inactive','Enable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',2,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(166,'tsintel2@pelorus.in','tsintel@123','Client','Inactive','Enable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',3,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(167,'demo1@pelorus.in','Demo1@123','Client','Inactive','Enable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',4,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(168,'demo2@pelorus.in','Demo2@123','Client','Inactive','Enable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',5,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(169,'tantan@pelorus.in','Tantan@123','Client','Inactive','Disable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',6,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi'),(170,'ravina@pelorus.in','Ravina@123','Client','Inactive','Disable',2,'28-08-2024','30-10-2025',NULL,'Pelorus',7,'es,it,en,pt,de,ja,pl,ru,nl,id,in,ca,fr,tr,sv,uk,ms,no,fi,vi,th,sk,el,cs,hr,tl,da,ko,ro,bg,zh,gl,bs,ar,mk,hu,ta,hi,et,ur,sl,lv,az,he,lt,fa,cy,sr,af,kn,kk,is,mr,mi,sw,hy,be,ne,bn,gu,pa,ml,te,as,or,sa,kok,mai,mni,sat,sd,ks,doi');
        /*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        # Create the `user_groups` table
        cursor.execute("""
        DROP TABLE IF EXISTS `user_groups`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `user_groups` (
            `ID` int NOT NULL AUTO_INCREMENT,
            `Group_Name` varchar(255) DEFAULT NULL,
            `GroupID` int DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `description` text,
            PRIMARY KEY (`ID`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `user_groups` created or already exists.")

        cursor.execute("""
        LOCK TABLES `user_groups` WRITE;
        /*!40000 ALTER TABLE `user_groups` DISABLE KEYS */;
        /*!40000 ALTER TABLE `user_groups` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        # Create the `user_keyword_groups` table
        cursor.execute("""
        DROP TABLE IF EXISTS `user_keyword_groups`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `user_keyword_groups` (
            `group_id` int NOT NULL AUTO_INCREMENT,
            `group_name` varchar(255) DEFAULT NULL,
            `created_date` varchar(255) DEFAULT NULL,
            `UserID` int DEFAULT NULL,
            3+
            `ClientID` int DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`group_id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `user_keyword_groups` created or already exists.")

        cursor.execute("""
        LOCK TABLES `user_keyword_groups` WRITE;
        /*!40000 ALTER TABLE `user_keyword_groups` DISABLE KEYS */;
        /*!40000 ALTER TABLE `user_keyword_groups` ENABLE KEYS */;
        UNLOCK TABLES
        """)

        # Create the `user_keywords` table
        cursor.execute("""
        DROP TABLE IF EXISTS `user_keywords`;
        /*!40101 SET @saved_cs_client     = @@character_set_client */;
        /*!50503 SET character_set_client = utf8mb4 */;
        CREATE TABLE `user_keywords` (
            `keywordID` int NOT NULL AUTO_INCREMENT,
            `words` varchar(255) DEFAULT NULL,
            `group_id` int DEFAULT NULL,
            `created_date` varchar(255) DEFAULT NULL,
            `ClientID` int DEFAULT NULL,
            `AdminID` int DEFAULT NULL,
            `Category` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`keywordID`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;
        """)
        print("Table `user_keywords` created or already exists.")

        cursor.execute("""
        LOCK TABLES `user_keywords` WRITE;
        /*!40000 ALTER TABLE `user_keywords` DISABLE KEYS */;
        /*!40000 ALTER TABLE `user_keywords` ENABLE KEYS */;
        UNLOCK TABLES
        """)

                       
finally:
    connection.close()