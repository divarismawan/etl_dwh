/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.1.35-MariaDB : Database - db_dimensional_perpus
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_dimensional_perpus` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_dimensional_perpus`;

/*Table structure for table `dim_buku` */

DROP TABLE IF EXISTS `dim_buku`;

CREATE TABLE `dim_buku` (
  `id_detail_buku` int(11) NOT NULL,
  `id_buku` int(11) DEFAULT NULL,
  `title_buku` varchar(30) DEFAULT NULL,
  `barcode_buku` varchar(30) DEFAULT NULL,
  `tanggal_release` date DEFAULT NULL,
  PRIMARY KEY (`id_detail_buku`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_buku` */

insert  into `dim_buku`(`id_detail_buku`,`id_buku`,`title_buku`,`barcode_buku`,`tanggal_release`) values 
(1,1,'Bitterblue ','BB-R11-1001','2001-07-09'),
(2,1,'Bitterblue ','BB-R11-1002','2001-07-09'),
(3,2,'The Hobbit','TH-R12-2001','2006-07-09'),
(4,2,'The Hobbit','TH-R12-2002','2006-07-09'),
(5,3,'The Martian','TM-R12-3001','2010-12-02'),
(6,3,'The Martian','TM-R12-3002','2010-12-02'),
(7,4,'Carrie ','CR-R12-4001','2011-11-09'),
(8,4,'Carrie ','CR-R12-4002','2011-11-09'),
(9,4,'Carrie ','CR-R12-4003','2011-11-09'),
(10,1,'Bitterblue ','BB-R21-1001','2001-07-09'),
(11,1,'Bitterblue ','BB-R21-1002','2001-07-09'),
(12,5,'The Book Thief ','TB-R21-5001','2015-08-28'),
(13,5,'The Book Thief ','TB-R21-5002','2015-08-28'),
(14,5,'The Book Thief ','TB-R21-5003','2015-08-28'),
(15,6,'The Sound and The Fu','SF-R22-6001','2014-11-01'),
(16,6,'The Sound and The Fu','SF-R22-6002','2014-11-01'),
(17,6,'The Sound and The Fu','SF-R22-6003','2014-11-01'),
(18,3,'The Martian','TM-R22-3001','2010-12-02'),
(19,3,'The Martian','TM-R22-3002','2010-12-02'),
(20,5,'The Book Thief ','TB-R31-5001','2015-08-28'),
(21,5,'The Book Thief ','TB-R31-5002','2015-08-28'),
(22,5,'The Book Thief ','TB-R31-5003','2015-08-28'),
(23,7,'Darkness at Noon','DN-R32-7001','2015-03-09'),
(24,7,'Darkness at Noon','DN-R32-7002','2015-03-09'),
(25,7,'Darkness at Noon','DN-R32-7003','2015-03-09');

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id_member` int(11) NOT NULL,
  `nama_member` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_member`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_member` */

insert  into `dim_member`(`id_member`,`nama_member`) values 
(1,'Kayla'),
(2,'Vanessa'),
(3,'Lisa'),
(4,'Braham'),
(5,'Scott'),
(6,'Amelia'),
(7,'Maria'),
(8,'Tesla'),
(9,'Candra'),
(10,'Krisna');

/*Table structure for table `dim_pegawai` */

DROP TABLE IF EXISTS `dim_pegawai`;

CREATE TABLE `dim_pegawai` (
  `id_pegawai` int(11) NOT NULL,
  `nama_pegawai` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_pegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_pegawai` */

insert  into `dim_pegawai`(`id_pegawai`,`nama_pegawai`) values 
(1,'Madelyn'),
(2,'Poppy'),
(3,'Johnson'),
(4,'Windi'),
(5,'Tole'),
(6,'ROBERT'),
(7,'Risma');

/*Table structure for table `dim_penerbit` */

DROP TABLE IF EXISTS `dim_penerbit`;

CREATE TABLE `dim_penerbit` (
  `id_penerbit` int(11) NOT NULL,
  `nama_perusahaan` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_penerbit`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_penerbit` */

insert  into `dim_penerbit`(`id_penerbit`,`nama_perusahaan`) values 
(1,'Elexmedia Komputindo'),
(2,'Mandiri Dian Semesta'),
(3,'GRAMEDIA');

/*Table structure for table `dim_penulis` */

DROP TABLE IF EXISTS `dim_penulis`;

CREATE TABLE `dim_penulis` (
  `id_penulis` int(11) NOT NULL,
  `nama_penulis` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_penulis`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_penulis` */

insert  into `dim_penulis`(`id_penulis`,`nama_penulis`) values 
(1,'Asma Nadia'),
(2,'Andrea Hirata'),
(3,'Tere Liye'),
(4,'Raditya Dika'),
(5,'Ika Natassa');

/*Table structure for table `dim_perpus` */

DROP TABLE IF EXISTS `dim_perpus`;

CREATE TABLE `dim_perpus` (
  `id_perpus` int(11) NOT NULL,
  `nama_perpus` varchar(30) DEFAULT NULL,
  `alamat_perpus` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_perpus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_perpus` */

insert  into `dim_perpus`(`id_perpus`,`nama_perpus`,`alamat_perpus`) values 
(1,'Tianjin Binhai Library','Tianjin'),
(2,'Seattle Public Library','Washington'),
(3,'Library of Birmingham','Inggris');

/*Table structure for table `dim_rak` */

DROP TABLE IF EXISTS `dim_rak`;

CREATE TABLE `dim_rak` (
  `id_rak` int(11) NOT NULL,
  `nama_rak` varbinary(30) DEFAULT NULL,
  PRIMARY KEY (`id_rak`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_rak` */

insert  into `dim_rak`(`id_rak`,`nama_rak`) values 
(1,'Tianjin Rak Novel'),
(2,'Tianjin Rak Ilmiah'),
(3,'Seattle Rak Novel'),
(4,'Seattle Rak Ilmiah'),
(5,'Birmingham Rak Novel'),
(6,'Birmingham Rak Ilmiah');

/*Table structure for table `fakta_trans` */

DROP TABLE IF EXISTS `fakta_trans`;

CREATE TABLE `fakta_trans` (
  `id_fakta_trans` int(11) NOT NULL AUTO_INCREMENT,
  `id_detail_trans` int(11) DEFAULT NULL,
  `id_trans` int(11) DEFAULT NULL,
  `id_detail_buku` int(11) DEFAULT NULL,
  `id_rak` int(11) DEFAULT NULL,
  `id_perpus` int(11) DEFAULT NULL,
  `id_penerbit` int(11) DEFAULT NULL,
  `id_penulis` int(11) DEFAULT NULL,
  `id_member` int(11) DEFAULT NULL,
  `id_pegawai` int(11) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  PRIMARY KEY (`id_fakta_trans`),
  KEY `id_trans` (`id_trans`),
  KEY `id_buku` (`id_detail_buku`),
  KEY `id_penerbit` (`id_penerbit`),
  KEY `id_penulis` (`id_penulis`),
  KEY `id_member` (`id_member`),
  KEY `id_pegawai` (`id_pegawai`),
  KEY `id_waktu` (`tanggal_pinjam`),
  KEY `id_perpus` (`id_perpus`),
  KEY `id_rak` (`id_rak`),
  CONSTRAINT `fakta_trans_ibfk_2` FOREIGN KEY (`id_detail_buku`) REFERENCES `dim_buku` (`id_detail_buku`),
  CONSTRAINT `fakta_trans_ibfk_3` FOREIGN KEY (`id_penerbit`) REFERENCES `dim_penerbit` (`id_penerbit`),
  CONSTRAINT `fakta_trans_ibfk_4` FOREIGN KEY (`id_penulis`) REFERENCES `dim_penulis` (`id_penulis`),
  CONSTRAINT `fakta_trans_ibfk_5` FOREIGN KEY (`id_member`) REFERENCES `dim_member` (`id_member`),
  CONSTRAINT `fakta_trans_ibfk_6` FOREIGN KEY (`id_pegawai`) REFERENCES `dim_pegawai` (`id_pegawai`),
  CONSTRAINT `fakta_trans_ibfk_8` FOREIGN KEY (`id_perpus`) REFERENCES `dim_perpus` (`id_perpus`),
  CONSTRAINT `fakta_trans_ibfk_9` FOREIGN KEY (`id_rak`) REFERENCES `dim_rak` (`id_rak`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

/*Data for the table `fakta_trans` */

insert  into `fakta_trans`(`id_fakta_trans`,`id_detail_trans`,`id_trans`,`id_detail_buku`,`id_rak`,`id_perpus`,`id_penerbit`,`id_penulis`,`id_member`,`id_pegawai`,`tanggal_pinjam`,`tanggal_kembali`) values 
(1,1,1,11,3,2,3,2,3,5,'2017-07-11','2017-07-14'),
(2,2,2,9,2,1,2,3,4,2,'2017-08-08','2017-08-13'),
(3,3,2,3,1,1,1,1,4,2,'2017-08-08','2017-08-13'),
(4,4,3,5,2,1,2,5,5,5,'2017-08-11','2017-08-16'),
(5,5,4,10,3,2,3,2,5,2,'2017-09-07','2017-09-12'),
(6,6,5,10,3,2,3,2,4,1,'2017-10-11','2017-10-12'),
(7,7,6,4,1,1,1,1,5,5,'2017-10-12','2017-10-14'),
(8,8,7,13,3,2,2,3,4,2,'2017-10-19','2017-10-21'),
(9,9,7,1,1,1,3,2,4,2,'2017-10-19','2017-10-21'),
(10,10,7,6,2,1,2,5,4,2,'2017-10-19','2017-10-21'),
(11,11,8,9,2,1,2,3,2,3,'2017-11-23','2017-11-25'),
(12,12,8,6,2,1,2,5,2,3,'2017-11-23','2017-11-25'),
(13,13,9,15,4,2,2,4,4,1,'2017-12-14','2017-12-16'),
(14,14,10,8,2,1,2,3,3,1,'2018-01-08','2018-01-11'),
(15,15,11,10,3,2,3,2,1,2,'2018-02-07','2018-02-10'),
(16,16,11,15,4,2,2,4,1,2,'2018-02-07','2018-02-10'),
(17,17,12,15,4,2,2,4,3,2,'2018-02-15','2018-02-20'),
(18,18,12,11,3,2,3,2,3,2,'2018-02-15','2018-02-20'),
(19,19,13,5,2,1,2,5,1,3,'2018-03-08','2018-03-15'),
(20,20,13,12,3,2,2,3,1,3,'2018-03-08','2018-03-15'),
(21,21,14,9,2,1,2,3,4,2,'2018-04-05','2018-04-12'),
(22,22,14,2,1,1,3,2,4,2,'2018-04-05','2018-04-12'),
(23,23,15,7,2,1,2,3,1,5,'2018-05-06','2018-05-10'),
(24,24,16,11,3,2,3,2,2,3,'2018-06-12','2018-06-19'),
(25,25,16,1,1,1,3,2,2,3,'2018-06-12','2018-06-19'),
(26,26,17,8,2,1,2,3,4,5,'2018-07-15','2018-07-19'),
(27,27,18,14,3,2,2,3,1,4,'2018-08-16','2018-08-28'),
(28,28,19,1,1,1,3,2,4,3,'2018-09-04','2018-09-13'),
(29,29,19,3,1,1,1,1,4,3,'2018-09-04','2018-09-13'),
(30,30,20,11,3,2,3,2,5,2,'2018-10-20','2018-10-26'),
(31,31,21,14,3,2,2,3,2,3,'2018-10-23','2018-10-27'),
(32,32,21,16,4,2,2,4,2,3,'2018-10-23','2018-10-27'),
(33,33,21,12,3,2,2,3,2,3,'2018-10-23','2018-10-27'),
(34,34,21,20,5,3,2,3,2,3,'2018-10-23','2018-10-27'),
(35,35,22,23,6,3,1,5,1,5,'2018-10-23','2018-10-27'),
(36,36,22,17,4,2,2,4,1,5,'2018-10-23','2018-10-27'),
(37,37,23,25,6,3,1,5,3,1,'2018-10-26','2018-10-29'),
(38,38,24,18,4,2,2,5,4,1,'2018-10-27','2018-10-30'),
(39,39,25,23,6,3,1,5,5,3,'2018-11-02','2018-11-04'),
(40,40,25,14,3,2,2,3,5,3,'2018-11-02','2018-11-04'),
(41,41,25,13,3,2,2,3,5,3,'2018-11-02','2018-11-04');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
