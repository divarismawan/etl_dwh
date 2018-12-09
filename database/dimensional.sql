/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.1.36-MariaDB : Database - db_dimensional_perpus
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
  `id_buku` int(11) NOT NULL,
  `nama_buku` varchar(30) DEFAULT NULL,
  `ISBN` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_buku`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_buku` */

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id_member` int(11) NOT NULL,
  `nama_member` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_member`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_member` */

/*Table structure for table `dim_pegawai` */

DROP TABLE IF EXISTS `dim_pegawai`;

CREATE TABLE `dim_pegawai` (
  `id_pegawai` int(11) NOT NULL,
  `nama_pegawai` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_pegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_pegawai` */

/*Table structure for table `dim_penerbit` */

DROP TABLE IF EXISTS `dim_penerbit`;

CREATE TABLE `dim_penerbit` (
  `id_penerbit` int(11) NOT NULL,
  `nama_perusahaan` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_penerbit`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_penerbit` */

/*Table structure for table `dim_penulis` */

DROP TABLE IF EXISTS `dim_penulis`;

CREATE TABLE `dim_penulis` (
  `id_penulis` int(11) NOT NULL,
  `nama_penulis` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_penulis`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_penulis` */

/*Table structure for table `dim_perpus` */

DROP TABLE IF EXISTS `dim_perpus`;

CREATE TABLE `dim_perpus` (
  `id_perpus` int(11) NOT NULL,
  `nama_perpus` varchar(30) DEFAULT NULL,
  `alamat_perpus` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_perpus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_perpus` */

/*Table structure for table `fakta_trans` */

DROP TABLE IF EXISTS `fakta_trans`;

CREATE TABLE `fakta_trans` (
  `id_fakta_trans` int(11) NOT NULL AUTO_INCREMENT,
  `id_detail_trans` int(11) DEFAULT NULL,
  `id_trans` int(11) DEFAULT NULL,
  `id_perpus` int(11) DEFAULT NULL,
  `id_buku` int(11) DEFAULT NULL,
  `id_penerbit` int(11) DEFAULT NULL,
  `id_penulis` int(11) DEFAULT NULL,
  `id_member` int(11) DEFAULT NULL,
  `id_pegawai` int(11) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  PRIMARY KEY (`id_fakta_trans`),
  KEY `id_trans` (`id_trans`),
  KEY `id_buku` (`id_buku`),
  KEY `id_penerbit` (`id_penerbit`),
  KEY `id_penulis` (`id_penulis`),
  KEY `id_member` (`id_member`),
  KEY `id_pegawai` (`id_pegawai`),
  KEY `id_waktu` (`tanggal_pinjam`),
  KEY `id_perpus` (`id_perpus`),
  CONSTRAINT `fakta_trans_ibfk_2` FOREIGN KEY (`id_buku`) REFERENCES `dim_buku` (`id_buku`),
  CONSTRAINT `fakta_trans_ibfk_3` FOREIGN KEY (`id_penerbit`) REFERENCES `dim_penerbit` (`id_penerbit`),
  CONSTRAINT `fakta_trans_ibfk_4` FOREIGN KEY (`id_penulis`) REFERENCES `dim_penulis` (`id_penulis`),
  CONSTRAINT `fakta_trans_ibfk_5` FOREIGN KEY (`id_member`) REFERENCES `dim_member` (`id_member`),
  CONSTRAINT `fakta_trans_ibfk_6` FOREIGN KEY (`id_pegawai`) REFERENCES `dim_pegawai` (`id_pegawai`),
  CONSTRAINT `fakta_trans_ibfk_8` FOREIGN KEY (`id_perpus`) REFERENCES `dim_perpus` (`id_perpus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fakta_trans` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
