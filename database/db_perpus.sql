/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.1.35-MariaDB : Database - db_perpus
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_perpus` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_perpus`;

/*Table structure for table `tb_buku` */

DROP TABLE IF EXISTS `tb_buku`;

CREATE TABLE `tb_buku` (
  `id_buku` int(3) NOT NULL AUTO_INCREMENT,
  `id_penulis` int(3) DEFAULT NULL,
  `id_penerbit` int(3) DEFAULT NULL,
  `title_buku` varchar(20) DEFAULT NULL,
  `tgl_release` date DEFAULT NULL,
  `ISBN` varchar(12) DEFAULT NULL,
  `time_update` date DEFAULT NULL,
  PRIMARY KEY (`id_buku`),
  KEY `id_penerbit` (`id_penerbit`),
  KEY `id_penulis` (`id_penulis`),
  CONSTRAINT `tb_buku_ibfk_2` FOREIGN KEY (`id_penerbit`) REFERENCES `tb_penerbit` (`id_penerbit`),
  CONSTRAINT `tb_buku_ibfk_3` FOREIGN KEY (`id_penulis`) REFERENCES `tb_penulis` (`id_penulis`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `tb_buku` */

insert  into `tb_buku`(`id_buku`,`id_penulis`,`id_penerbit`,`title_buku`,`tgl_release`,`ISBN`,`time_update`) values 
(1,2,3,'Bitterblue ','2001-07-09','SF5 AB2','2017-08-16'),
(2,1,1,'The Hobbit','2006-07-09','S4B 5FA','2017-08-24'),
(3,5,2,'The Martian','2010-12-02','G6G SG5','2017-09-14'),
(4,3,2,'Carrie ','2011-11-09','G5H H5Q','2017-10-19'),
(5,3,2,'The Book Thief ','2015-08-28','R7N 4AS','2017-11-23'),
(6,4,2,'The Sound and The Fu','2014-11-01','WG1 SH3','2017-12-20'),
(7,5,1,'Darkness at Noon','2015-03-09','F1G 32S','2017-12-28'),
(8,4,1,'The Grapes of Wrath','2014-07-03','W1V B6J','2018-01-10'),
(9,2,1,'The Good Slayer','2015-08-28','OP1 IV7','2018-02-20'),
(10,5,2,'White Panda','2016-06-14','WO6 D2O','2018-03-09'),
(11,1,2,'Invisible Man','2016-09-15','I9W OP1','2018-03-22'),
(12,3,1,'The Last Wish','2016-11-09','J0N K1D','2018-05-23'),
(13,2,2,'The Lord of the Flie','2017-01-27','KIA O1G','2018-07-26'),
(14,4,1,'Marmut Merah Jambu','2017-06-15','7G5 WEG','2018-09-13'),
(15,5,1,'No Rain No Rainbow','2017-10-17','G24 WE1','2018-11-21');

/*Table structure for table `tb_detail_trans` */

DROP TABLE IF EXISTS `tb_detail_trans`;

CREATE TABLE `tb_detail_trans` (
  `id_detail` int(3) NOT NULL AUTO_INCREMENT,
  `id_trans` int(3) DEFAULT NULL,
  `id_buku` int(3) DEFAULT NULL,
  PRIMARY KEY (`id_detail`),
  KEY `id_trans` (`id_trans`),
  KEY `id_buku` (`id_buku`),
  CONSTRAINT `tb_detail_trans_ibfk_2` FOREIGN KEY (`id_buku`) REFERENCES `tb_buku` (`id_buku`),
  CONSTRAINT `tb_detail_trans_ibfk_3` FOREIGN KEY (`id_trans`) REFERENCES `tb_transaksi` (`id_trans`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `tb_detail_trans` */

insert  into `tb_detail_trans`(`id_detail`,`id_trans`,`id_buku`) values 
(1,1,11),
(2,2,9),
(3,2,3),
(4,3,5),
(5,4,10),
(6,5,10),
(7,6,5),
(8,7,13),
(9,7,1),
(10,7,6),
(11,8,9),
(12,8,6),
(13,9,15),
(14,10,8),
(15,11,10),
(16,11,15),
(17,12,15),
(18,12,11),
(19,13,5),
(20,13,12),
(21,14,9),
(22,14,2),
(23,15,7),
(24,16,11),
(25,16,1),
(26,17,8),
(27,18,14),
(28,19,1),
(29,19,3),
(30,20,11);

/*Table structure for table `tb_member` */

DROP TABLE IF EXISTS `tb_member`;

CREATE TABLE `tb_member` (
  `id_member` int(3) NOT NULL AUTO_INCREMENT,
  `nama` varchar(25) DEFAULT NULL,
  `tlpn` char(12) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  PRIMARY KEY (`id_member`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tb_member` */

insert  into `tb_member`(`id_member`,`nama`,`tlpn`,`email`,`tgl_lahir`) values 
(1,'Kayla','084354831587','kayla@gmail.com','2009-06-09'),
(2,'Vanessa','084638414254','vanessa@gmail.com','1998-06-16'),
(3,'Lisa','087523354325','lisa@gmail.com','2004-10-01'),
(4,'Katok','087356222695','katok@gmail.com','2010-06-26'),
(5,'Scott','088455452141','scott@gmail.co','2004-06-08'),
(6,'Amelia','085366623225','amelia@gmaiil.com','1993-07-01'),
(7,'Maria','085536365415','maria@gmail.com','2011-03-03');

/*Table structure for table `tb_pegawai` */

DROP TABLE IF EXISTS `tb_pegawai`;

CREATE TABLE `tb_pegawai` (
  `id_pegawai` int(3) NOT NULL AUTO_INCREMENT,
  `id_perpus` int(11) DEFAULT NULL,
  `nama_pegawai` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `tlpn` char(12) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  PRIMARY KEY (`id_pegawai`),
  KEY `id_perpus` (`id_perpus`),
  CONSTRAINT `tb_pegawai_ibfk_1` FOREIGN KEY (`id_perpus`) REFERENCES `tb_perpus` (`id_perpus`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tb_pegawai` */

insert  into `tb_pegawai`(`id_pegawai`,`id_perpus`,`nama_pegawai`,`alamat`,`email`,`tlpn`,`tgl_lahir`) values 
(1,2,'Madelyn','Kalimantan','Madelyn@gmail.com','084658217564','1992-07-16'),
(2,1,'Poppy','Papua','Poppy2@gmail.com','085167254943','1988-07-01'),
(3,1,'Johnson','Sumatra','Johnson@mail.com','084354683513','1993-12-31'),
(4,3,'Windi','Bali','windi@mail.com','086733587313','1998-05-06'),
(5,1,'Tole','Jawa','tole@gmail.com','084661334813','1994-07-01'),
(6,2,'ROBERT','Sulawesi','robert@gmail.com','087643436469','1990-11-30'),
(7,3,'Risma','Bali','risma@gmail.com','084654317353','1998-02-20');

/*Table structure for table `tb_penerbit` */

DROP TABLE IF EXISTS `tb_penerbit`;

CREATE TABLE `tb_penerbit` (
  `id_penerbit` int(3) NOT NULL AUTO_INCREMENT,
  `nama_perusahaan` varchar(30) DEFAULT NULL,
  `alamat` varchar(20) DEFAULT NULL,
  `tgl_berdiri` date DEFAULT NULL,
  PRIMARY KEY (`id_penerbit`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_penerbit` */

insert  into `tb_penerbit`(`id_penerbit`,`nama_perusahaan`,`alamat`,`tgl_berdiri`) values 
(1,'Elexmedia Komputindo','Jakarta ','1985-07-24'),
(2,'Mandiri Dian Semesta','Bandung ','1987-03-11'),
(3,'GRAMEDIA','Surabaya','1981-07-24');

/*Table structure for table `tb_penulis` */

DROP TABLE IF EXISTS `tb_penulis`;

CREATE TABLE `tb_penulis` (
  `id_penulis` int(3) NOT NULL AUTO_INCREMENT,
  `nama_penulis` varchar(30) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `tlpn` char(12) DEFAULT NULL,
  `tgl_bergabung` date DEFAULT NULL,
  PRIMARY KEY (`id_penulis`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tb_penulis` */

insert  into `tb_penulis`(`id_penulis`,`nama_penulis`,`tgl_lahir`,`email`,`tlpn`,`tgl_bergabung`) values 
(1,'Asma Nadia','1981-06-21','nadiaasma@gmail.com','087124597895','2018-01-25'),
(2,'Andrea Hirata','1988-02-26','hirataandrea@yahoo.com','085648625648','2018-02-20'),
(3,'Tere Liye','1984-07-01','liyetere@gmail.com','081668568673','2018-05-06'),
(4,'Raditya Dika','1990-01-01','raditiya@gmail.com','087674319761','2018-07-18'),
(5,'Ika Natassa','1998-05-06','ikanatassa@gmail.com','087763264833','2018-08-22');

/*Table structure for table `tb_perpus` */

DROP TABLE IF EXISTS `tb_perpus`;

CREATE TABLE `tb_perpus` (
  `id_perpus` int(11) NOT NULL AUTO_INCREMENT,
  `nama_perpus` varchar(30) DEFAULT NULL,
  `alamat_perpus` varchar(30) DEFAULT NULL,
  `tgl_berdiri` date DEFAULT NULL,
  PRIMARY KEY (`id_perpus`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_perpus` */

insert  into `tb_perpus`(`id_perpus`,`nama_perpus`,`alamat_perpus`,`tgl_berdiri`) values 
(1,'Tianjin Binhai Library','Tianjin','2001-02-20'),
(2,'Seattle Public Library','Washington','2004-05-23'),
(3,'Library of Birmingham','Inggris','2006-11-01');

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_trans` int(3) NOT NULL AUTO_INCREMENT,
  `id_member` int(3) DEFAULT NULL,
  `id_pegawai` int(3) DEFAULT NULL,
  `tgl_pinjam` date DEFAULT NULL,
  `tgl_kembali` date DEFAULT NULL,
  PRIMARY KEY (`id_trans`),
  KEY `id_member` (`id_member`),
  KEY `id_pegawai` (`id_pegawai`),
  CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`id_member`) REFERENCES `tb_member` (`id_member`),
  CONSTRAINT `tb_transaksi_ibfk_2` FOREIGN KEY (`id_pegawai`) REFERENCES `tb_pegawai` (`id_pegawai`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `tb_transaksi` */

insert  into `tb_transaksi`(`id_trans`,`id_member`,`id_pegawai`,`tgl_pinjam`,`tgl_kembali`) values 
(1,3,5,'2017-07-11','2017-07-14'),
(2,4,7,'2017-08-08','2017-08-13'),
(3,6,6,'2017-08-11','2017-08-16'),
(4,5,2,'2017-09-07','2017-09-12'),
(5,4,6,'2017-10-11','2017-10-12'),
(6,5,5,'2017-10-12','2017-10-14'),
(7,4,2,'2017-10-19','2017-10-21'),
(8,6,3,'2017-11-23','2017-11-25'),
(9,4,7,'2017-12-14','2017-12-16'),
(10,3,6,'2018-01-08','2018-01-11'),
(11,1,2,'2018-02-07','2018-02-10'),
(12,3,2,'2018-02-15','2018-02-20'),
(13,1,3,'2018-03-08','2018-03-15'),
(14,4,6,'2018-04-05','2018-04-12'),
(15,1,5,'2018-05-06','2018-05-10'),
(16,2,7,'2018-06-12','2018-06-19'),
(17,4,5,'2018-07-15','2018-07-19'),
(18,1,4,'2018-08-16','2018-08-28'),
(19,4,3,'2018-09-04','2018-09-13'),
(20,6,2,'2018-10-20','2018-10-26');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
