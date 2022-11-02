-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 17, 2022 at 07:40 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistema_bancario_prod`
--

-- --------------------------------------------------------

--
-- Table structure for table `cuenta`
--

CREATE TABLE `cuenta` (
  `id` int(11) NOT NULL,
  `numero_cuenta` int(25) NOT NULL,
  `nombre_titular` varchar(100) NOT NULL,
  `primer_apellido_titular` varchar(100) NOT NULL,
  `segundo_apellido_titular` varchar(100) NOT NULL,
  `balance` double NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `moneda` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cuenta`
--

INSERT INTO `cuenta` (`id`, `numero_cuenta`, `nombre_titular`, `primer_apellido_titular`, `segundo_apellido_titular`, `balance`, `estado`, `moneda`) VALUES
(1, 3254653, 'JUanitO', 'Marmoles', 'Perez', 2000.152, 1, 'Colones'),
(2, 123456, 'Pedro', 'Marmol', 'Perez', 2000.1, 1, 'Dolares'),
(3, 7891011, 'Maria', 'Data', 'Base', 2020.152, 1, 'Dolares'),
(4, 1235684, 'Barry', 'Allen', 'Santamaria', 2020.152, 1, 'Coloness');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cuenta`
--
ALTER TABLE `cuenta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_cuenta` (`numero_cuenta`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cuenta`
--
ALTER TABLE `cuenta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
