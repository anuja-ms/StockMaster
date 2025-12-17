-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 17, 2025 at 08:12 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stockmaster`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_brand`
--

CREATE TABLE `adminapp_tbl_brand` (
  `brandid` int(11) NOT NULL,
  `brandname` varchar(25) NOT NULL,
  `brandimage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_brand`
--

INSERT INTO `adminapp_tbl_brand` (`brandid`, `brandname`, `brandimage`) VALUES
(3, 'Ariel', 'brand_rAYzI64.jpeg'),
(4, 'Others', 'others_seaOGZK.png'),
(6, 'Lakme', 'image.avif'),
(7, 'Himalaya Baby Products', 'himalaya.webp'),
(8, 'Vim', 'vimbrand.avif');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_category`
--

CREATE TABLE `adminapp_tbl_category` (
  `categoryid` int(11) NOT NULL,
  `categoryname` varchar(25) NOT NULL,
  `categoryimage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_category`
--

INSERT INTO `adminapp_tbl_category` (`categoryid`, `categoryname`, `categoryimage`) VALUES
(3, 'Cleaning & Household', 'dd.jpg'),
(5, 'fruits &  vegitables', 'ff_9rRQ4JO.jpeg'),
(8, 'Beauty & Hygiene', 'beautyhy.avif'),
(9, 'bakery', 'abcdcake.jpg'),
(10, 'Eggs ,Meat and Fish', 'emf.jpg'),
(11, 'Baby Care', 'babycare.jpg'),
(12, 'Electronics', 'electronics.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_dealer`
--

CREATE TABLE `adminapp_tbl_dealer` (
  `dealerid` int(11) NOT NULL,
  `dealername` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contactno` bigint(20) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_dealer`
--

INSERT INTO `adminapp_tbl_dealer` (`dealerid`, `dealername`, `email`, `contactno`, `locationid_id`, `loginid_id`) VALUES
(9, 'Midhun S', 'midhuns@gmail.com', 890456780, 10, 15),
(10, 'Aravind', 'aravind@gmail.com', 8090567890, 7, 16),
(13, 'Meena', 'anujams2002@gmail.com', 7890342572, 10, 29),
(14, 'Vishal M', 'ams816201@gmail.com', 7849307483, 7, 30),
(15, 'Gopika', 'ams816201@gmail.com', 7834564789, 7, 31),
(16, 'Adithyan', 'ams816201@gmail.com', 8745637890, 7, 32),
(18, 'Kumar', 'anujams2002@gmail.com', 7890567890, 7, 34);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

CREATE TABLE `adminapp_tbl_district` (
  `districtid` int(11) NOT NULL,
  `districtname` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`districtid`, `districtname`) VALUES
(6, 'Thiruvananthapuram'),
(8, 'Pathanamthitta'),
(9, 'Alappuzha'),
(10, 'Kottayam'),
(11, 'Idukki'),
(12, 'Ernakulam'),
(13, 'Thrissur'),
(14, 'Palakkad'),
(15, 'Malappuram'),
(16, 'Kozhikode'),
(17, 'Wayanad'),
(18, 'Kannur'),
(20, 'kollam'),
(21, 'Kasaragod');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

CREATE TABLE `adminapp_tbl_location` (
  `locationid` int(11) NOT NULL,
  `locationname` varchar(25) NOT NULL,
  `districtid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`locationid`, `locationname`, `districtid_id`) VALUES
(7, 'Muvattupuzha', 12),
(8, 'Kalady', 12),
(9, 'Kovalam', 6),
(10, 'Neyyar', 6),
(11, 'Ettumanoor', 10);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_product`
--

CREATE TABLE `adminapp_tbl_product` (
  `productid` int(11) NOT NULL,
  `productname` varchar(25) NOT NULL,
  `description` varchar(50) NOT NULL,
  `price` bigint(20) NOT NULL,
  `unit` varchar(25) NOT NULL,
  `image` varchar(100) NOT NULL,
  `dealerprice` int(11) NOT NULL,
  `brandid_id` int(11) NOT NULL,
  `subcategoryid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_product`
--

INSERT INTO `adminapp_tbl_product` (`productid`, `productname`, `description`, `price`, `unit`, `image`, `dealerprice`, `brandid_id`, `subcategoryid_id`) VALUES
(1, 'Banana ', 'Banana - Robusta', 94, '70', 'robusta.jpeg', 90, 4, 2),
(4, 'Tomato', 'tomatoes are a good source of vitamin C and the ph', 45, '50', 'tomato.jpg', 30, 4, 5),
(5, 'Ariel Matic Front Load D', 'The new and improved Ariel Matic powder detergent!', 200, '2', 'arielmaticpro.webp', 160, 3, 8),
(6, 'Vim', 'removes the toughest grease and gives a pleasant c', 60, '100', 'vim.webp', 50, 8, 9),
(7, 'Cycle Agarbathi', 'Long-lasting Aroma,Good fragrance', 40, '5', 'agarbathicycle.webp', 30, 4, 10),
(8, 'Lia', 'good fragrance', 40, '6', 'lia.webp', 35, 4, 10),
(9, 'Honey', 'Good fragrance', 45, '5', 'honey.webp', 35, 4, 10),
(10, 'Tide', 'Washing Powder', 100, '2', 'tide.jpg', 80, 4, 8),
(11, 'Exo', 'Dishwash', 120, '5', 'exo.jpg', 90, 4, 9),
(12, 'Oranges', 'fresh oranges', 90, '10', 'orange.webp', 80, 4, 2),
(13, 'Guva', 'fresh Guva', 80, '10', 'guva.webp', 70, 4, 2),
(14, 'watermelon', 'fresh fruits', 100, '5', 'water.jpg', 90, 4, 2),
(15, 'Moisturizer', 'Perfect for normal, dry, as well as combination sk', 800, '10', 'moisturizer.jpeg', 500, 6, 6),
(16, 'Sunscreen', 'protects against UVA and UVB rays', 300, '10', 'sunscreen.avif', 250, 6, 6),
(17, 'Lipstick', 'Long-lasting matte finish lipstick ', 400, '20', 'lipstick.jpg', 350, 6, 6),
(18, 'Body Lotion', 'Body lotion ', 300, '20', 'bodylotion.jpeg', 200, 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_staff`
--

CREATE TABLE `adminapp_tbl_staff` (
  `staffid` int(11) NOT NULL,
  `staffname` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contactno` bigint(20) NOT NULL,
  `categoryid_id` int(11) DEFAULT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_staff`
--

INSERT INTO `adminapp_tbl_staff` (`staffid`, `staffname`, `email`, `contactno`, `categoryid_id`, `locationid_id`, `loginid_id`) VALUES
(5, 'Amal', 'amal@gmail.com', 7845783903, 3, 7, 17),
(6, 'Akshay', 'akshay@gmail.com', 8904567890, 5, 8, 18),
(9, 'Anitta', 'malupersonal05@gmail.com', 8075512347, 8, 8, 21),
(14, 'Alphonsa james', 'anujams2002@gmail.com', 7824514567, 11, 8, 28);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_stock`
--

CREATE TABLE `adminapp_tbl_stock` (
  `stockid` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `Reorderlevel` int(11) NOT NULL,
  `productid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_stock`
--

INSERT INTO `adminapp_tbl_stock` (`stockid`, `stock`, `Reorderlevel`, `productid_id`) VALUES
(2, 75, 60, 1),
(3, 40, 50, 4),
(4, 45, 50, 6),
(5, 30, 50, 5),
(7, 10, 50, 7),
(8, 40, 50, 11),
(9, 40, 50, 8),
(10, 10, 50, 12),
(12, 20, 50, 10),
(13, 30, 50, 9),
(14, 40, 50, 17),
(15, 50, 50, 16),
(16, 40, 50, 15);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_subcategory`
--

CREATE TABLE `adminapp_tbl_subcategory` (
  `subcategoryid` int(11) NOT NULL,
  `subcategoryname` varchar(25) NOT NULL,
  `image` varchar(100) NOT NULL,
  `categoryid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminapp_tbl_subcategory`
--

INSERT INTO `adminapp_tbl_subcategory` (`subcategoryid`, `subcategoryname`, `image`, `categoryid_id`) VALUES
(2, 'Fresh fruits', 'fff.jpeg', 5),
(5, 'Fresh Vegitables', 'veg.jpg', 5),
(6, 'Makeup', 'makeup.jpg', 8),
(7, 'Oral Care', 'oral.jpg', 8),
(8, 'Washing Powder', 'detergent_djLlCXT.jpg', 3),
(9, 'Dishwash & Bars', 'houseclean.jpeg', 3),
(10, 'Pooja Needs', 'pooja.webp', 3);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_login', 7, 'add_tbl_login'),
(26, 'Can change tbl_login', 7, 'change_tbl_login'),
(27, 'Can delete tbl_login', 7, 'delete_tbl_login'),
(28, 'Can view tbl_login', 7, 'view_tbl_login'),
(29, 'Can add tbl_district', 8, 'add_tbl_district'),
(30, 'Can change tbl_district', 8, 'change_tbl_district'),
(31, 'Can delete tbl_district', 8, 'delete_tbl_district'),
(32, 'Can view tbl_district', 8, 'view_tbl_district'),
(33, 'Can add tbl_location', 9, 'add_tbl_location'),
(34, 'Can change tbl_location', 9, 'change_tbl_location'),
(35, 'Can delete tbl_location', 9, 'delete_tbl_location'),
(36, 'Can view tbl_location', 9, 'view_tbl_location'),
(37, 'Can add tbl_brand', 10, 'add_tbl_brand'),
(38, 'Can change tbl_brand', 10, 'change_tbl_brand'),
(39, 'Can delete tbl_brand', 10, 'delete_tbl_brand'),
(40, 'Can view tbl_brand', 10, 'view_tbl_brand'),
(41, 'Can add tbl_category', 11, 'add_tbl_category'),
(42, 'Can change tbl_category', 11, 'change_tbl_category'),
(43, 'Can delete tbl_category', 11, 'delete_tbl_category'),
(44, 'Can view tbl_category', 11, 'view_tbl_category'),
(45, 'Can add tbl_subcategory', 12, 'add_tbl_subcategory'),
(46, 'Can change tbl_subcategory', 12, 'change_tbl_subcategory'),
(47, 'Can delete tbl_subcategory', 12, 'delete_tbl_subcategory'),
(48, 'Can view tbl_subcategory', 12, 'view_tbl_subcategory'),
(49, 'Can add tbl_dealer', 13, 'add_tbl_dealer'),
(50, 'Can change tbl_dealer', 13, 'change_tbl_dealer'),
(51, 'Can delete tbl_dealer', 13, 'delete_tbl_dealer'),
(52, 'Can view tbl_dealer', 13, 'view_tbl_dealer'),
(53, 'Can add tbl_staff', 14, 'add_tbl_staff'),
(54, 'Can change tbl_staff', 14, 'change_tbl_staff'),
(55, 'Can delete tbl_staff', 14, 'delete_tbl_staff'),
(56, 'Can view tbl_staff', 14, 'view_tbl_staff'),
(57, 'Can add tbl_product', 15, 'add_tbl_product'),
(58, 'Can change tbl_product', 15, 'change_tbl_product'),
(59, 'Can delete tbl_product', 15, 'delete_tbl_product'),
(60, 'Can view tbl_product', 15, 'view_tbl_product'),
(61, 'Can add tbl_stock', 16, 'add_tbl_stock'),
(62, 'Can change tbl_stock', 16, 'change_tbl_stock'),
(63, 'Can delete tbl_stock', 16, 'delete_tbl_stock'),
(64, 'Can view tbl_stock', 16, 'view_tbl_stock'),
(65, 'Can add tbl_requestmaster', 17, 'add_tbl_requestmaster'),
(66, 'Can change tbl_requestmaster', 17, 'change_tbl_requestmaster'),
(67, 'Can delete tbl_requestmaster', 17, 'delete_tbl_requestmaster'),
(68, 'Can view tbl_requestmaster', 17, 'view_tbl_requestmaster'),
(69, 'Can add tbl_requestdetails', 18, 'add_tbl_requestdetails'),
(70, 'Can change tbl_requestdetails', 18, 'change_tbl_requestdetails'),
(71, 'Can delete tbl_requestdetails', 18, 'delete_tbl_requestdetails'),
(72, 'Can view tbl_requestdetails', 18, 'view_tbl_requestdetails'),
(73, 'Can add tbl_salesmaster', 19, 'add_tbl_salesmaster'),
(74, 'Can change tbl_salesmaster', 19, 'change_tbl_salesmaster'),
(75, 'Can delete tbl_salesmaster', 19, 'delete_tbl_salesmaster'),
(76, 'Can view tbl_salesmaster', 19, 'view_tbl_salesmaster'),
(77, 'Can add tbl_salesdetails', 20, 'add_tbl_salesdetails'),
(78, 'Can change tbl_salesdetails', 20, 'change_tbl_salesdetails'),
(79, 'Can delete tbl_salesdetails', 20, 'delete_tbl_salesdetails'),
(80, 'Can view tbl_salesdetails', 20, 'view_tbl_salesdetails'),
(81, 'Can add tbl_purchasemaster', 21, 'add_tbl_purchasemaster'),
(82, 'Can change tbl_purchasemaster', 21, 'change_tbl_purchasemaster'),
(83, 'Can delete tbl_purchasemaster', 21, 'delete_tbl_purchasemaster'),
(84, 'Can view tbl_purchasemaster', 21, 'view_tbl_purchasemaster'),
(85, 'Can add tbl_purchasedetails', 22, 'add_tbl_purchasedetails'),
(86, 'Can change tbl_purchasedetails', 22, 'change_tbl_purchasedetails'),
(87, 'Can delete tbl_purchasedetails', 22, 'delete_tbl_purchasedetails'),
(88, 'Can view tbl_purchasedetails', 22, 'view_tbl_purchasedetails'),
(89, 'Can add tbl_payment', 23, 'add_tbl_payment'),
(90, 'Can change tbl_payment', 23, 'change_tbl_payment'),
(91, 'Can delete tbl_payment', 23, 'delete_tbl_payment'),
(92, 'Can view tbl_payment', 23, 'view_tbl_payment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'AdminApp', 'tbl_brand'),
(11, 'AdminApp', 'tbl_category'),
(13, 'AdminApp', 'tbl_dealer'),
(8, 'AdminApp', 'tbl_district'),
(9, 'AdminApp', 'tbl_location'),
(15, 'AdminApp', 'tbl_product'),
(14, 'AdminApp', 'tbl_staff'),
(16, 'AdminApp', 'tbl_stock'),
(12, 'AdminApp', 'tbl_subcategory'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'GuestApp', 'tbl_login'),
(6, 'sessions', 'session'),
(23, 'StaffApp', 'tbl_payment'),
(22, 'StaffApp', 'tbl_purchasedetails'),
(21, 'StaffApp', 'tbl_purchasemaster'),
(18, 'StaffApp', 'tbl_requestdetails'),
(17, 'StaffApp', 'tbl_requestmaster'),
(20, 'StaffApp', 'tbl_salesdetails'),
(19, 'StaffApp', 'tbl_salesmaster');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-02-16 11:15:46.173264'),
(2, 'auth', '0001_initial', '2025-02-16 11:15:46.897594'),
(3, 'admin', '0001_initial', '2025-02-16 11:15:47.016965'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-02-16 11:15:47.047880'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-16 11:15:47.047880'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-02-16 11:15:47.129049'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-02-16 11:15:47.185750'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-02-16 11:15:47.206670'),
(9, 'auth', '0004_alter_user_username_opts', '2025-02-16 11:15:47.206670'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-02-16 11:15:47.270662'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-02-16 11:15:47.270662'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-02-16 11:15:47.288968'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-02-16 11:15:47.301823'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-02-16 11:15:47.305261'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-02-16 11:15:47.328997'),
(16, 'auth', '0011_update_proxy_permissions', '2025-02-16 11:15:47.333520'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-02-16 11:15:47.349576'),
(18, 'sessions', '0001_initial', '2025-02-16 11:15:47.389359'),
(19, 'GuestApp', '0001_initial', '2025-02-16 11:16:03.618362'),
(20, 'AdminApp', '0001_initial', '2025-02-16 12:25:21.375347'),
(21, 'AdminApp', '0002_tbl_location', '2025-02-16 12:40:38.618781'),
(22, 'AdminApp', '0003_tbl_brand', '2025-02-16 15:31:03.001780'),
(23, 'AdminApp', '0004_tbl_category', '2025-02-16 15:44:03.630594'),
(24, 'AdminApp', '0005_tbl_subcategory', '2025-02-16 15:45:08.114776'),
(25, 'AdminApp', '0006_tbl_dealer', '2025-02-17 17:02:49.124606'),
(26, 'AdminApp', '0007_tbl_staff', '2025-02-19 06:21:47.214037'),
(27, 'AdminApp', '0008_tbl_product', '2025-02-19 06:35:35.737570'),
(28, 'AdminApp', '0009_tbl_stock', '2025-02-19 07:07:47.473985'),
(29, 'StaffApp', '0001_initial', '2025-02-23 10:12:25.242745'),
(30, 'StaffApp', '0002_tbl_requestdetails', '2025-02-23 10:13:17.961511'),
(31, 'StaffApp', '0003_tbl_salesmaster', '2025-02-23 11:26:58.895753'),
(32, 'StaffApp', '0004_tbl_salesdetails', '2025-02-23 11:27:41.932907'),
(33, 'StaffApp', '0005_tbl_purchasemaster', '2025-02-23 11:28:10.475725'),
(34, 'StaffApp', '0006_tbl_purchasedetails', '2025-02-23 11:29:11.720234'),
(35, 'StaffApp', '0007_tbl_payment', '2025-03-08 06:37:51.734117');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1p99jcsrt3fslffi5erhno7j8cy2l6vm', 'eyJsb2dpbklkIjoxfQ:1tknzO:p0XdmEOL5-Ib2FDOk5xaOkQN8fAkZkIq4sDFnFOmpTM', '2025-03-05 17:36:02.206020'),
('2plpahnb87jvd164qpv0w9gccv5f8q1a', 'eyJsb2dpbklkIjo4fQ:1tlUD7:cThfohtr0guV4msvLX5Zs2R29xfJXuwWQeAFKm7K1aY', '2025-03-07 14:41:01.550947'),
('7a3bjy9t2lf9e7nxwj7rq7msdp1szt6x', 'eyJsb2dpbklkIjoxMX0:1tnFug:rLRt7fVtD0qtIR32T6J018WJkYlkUT6Cq-yRzLPTGrc', '2025-03-12 11:49:18.149550'),
('cyqqftse2zhua591vdxse3gezlbrdbsr', 'eyJsb2dpbklkIjoxfQ:1tje76:Rgx1TAXZ41V0Ax2jr2RFATyKPIF2sanRx7-r1iGOgyg', '2025-03-02 12:51:12.105967'),
('foeeifnz7zm94rran5ty112ohazcw4vf', 'eyJsb2dpbklkIjo4fQ:1tlC3R:o9iZRoiV7yruSoZwQmy7CFWxwEKjhVcYQ6WRJALRJFs', '2025-03-06 19:17:49.810748'),
('kb8mcgs0vswbajjvc88pxp53e14zp3q8', 'eyJsb2dpbklkIjoxfQ:1tkclG:b3RdfWM2r-CokkP5ETBPuf4e1ZS0cGwzSCJeF1F1QzU', '2025-03-05 05:36:42.351305'),
('ohi5m7cnfyhrludczgww6oa0ojh01oni', 'eyJsb2dpbklkIjoxfQ:1vB4b1:Tg_h_6BuNLE3bFxKdEqZ3A7O_KdO2gBNvJvVwuVwQ8A', '2025-11-04 05:07:43.014981'),
('qgw3nd10ffged1xs3kouxcd7u4lrwbaq', 'eyJsb2dpbklkIjoxfQ:1tokiB:Ws9Z1FNO8xHVzH2bJYzkSF9-jXdrctJ3_fINwqeRUDY', '2025-03-16 14:54:35.388147'),
('s56jz1m61s9awotho1h0rlvhvzifzmgt', 'eyJsb2dpbklkIjoxfQ:1tkIDE:ZgfRspcOt_hVUyudBZA1LaoPrUTsj4c_pL7nG4GcQd0', '2025-03-04 07:40:12.984623'),
('s9moypg4r89xpjuz13da6qlj3kmm3ikd', 'eyJsb2dpbklkIjoxfQ:1u6mXU:bCUCl8mXLtV-drkufpD4PptDjFVavTjOoPVhRSzulVA', '2025-05-05 08:30:04.830979'),
('t833lgh7b96gefd6pchfrpa9l3q7evwl', 'eyJsb2dpbklkIjo4fQ:1tl8w8:vFyyb350hI3ZQxpp-FS44Mar_dBwvohhKJEaophfIBE', '2025-03-06 15:58:04.161050'),
('w3p7she92ek1vpx1645s9wd5sn5bdy7q', 'eyJsb2dpbklkIjoxfQ:1tm5nZ:StAZ4zD_pAJVUiqX2CsiHyRHeiRu1ZgmfVDbu_wm7nI', '2025-03-09 06:49:09.251138'),
('yrm2ka7rd10uu5efurhvx8vll4o8zc4d', 'eyJsb2dpbklkIjo4fQ:1tn7fc:NmD3iTIeP5ARZ-Ge68917EOjatBfoEblYDuqEB-vJFk', '2025-03-12 03:01:12.451652');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

CREATE TABLE `guestapp_tbl_login` (
  `loginid` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`) VALUES
(1, 'Admin', 'Admin', 'Admin'),
(15, 'midhun', 'midhun', 'dealer'),
(16, 'aravind', 'aravind', 'dealer'),
(17, 'amal', 'amal', 'staff'),
(18, 'akshay', 'akshay', 'staff'),
(21, 'anit', 'anit', 'staff'),
(25, 'madhu', 'madhu123', 'dealer'),
(28, 'alphonsa', 'oGZ78Km4', 'staff'),
(29, 'meena', 'fBU5YUO9', 'dealer'),
(30, 'vishal', 'vishal', 'dealer'),
(31, 'gopika', 'gopika', 'dealer'),
(32, 'adithyan', 'adithyan', 'dealer'),
(34, 'kumar', 'LD8KlAiv', 'dealer');

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_payment`
--

CREATE TABLE `staffapp_tbl_payment` (
  `paymentid` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(25) NOT NULL,
  `purchasemasterid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_payment`
--

INSERT INTO `staffapp_tbl_payment` (`paymentid`, `Amount`, `date`, `status`, `purchasemasterid_id`) VALUES
(1, 4800, '2025-03-08', 'Paid', 3),
(2, 4700, '2025-03-26', 'Paid', 7),
(3, 2500, '2025-03-27', 'Paid', 8),
(4, 11500, '2025-04-15', 'Paid', 11);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_purchasedetails`
--

CREATE TABLE `staffapp_tbl_purchasedetails` (
  `purchasedetailsid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `productprice` int(11) NOT NULL,
  `productid_id` int(11) NOT NULL,
  `purchasemasterid_id` int(11) DEFAULT NULL,
  `staffid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_purchasedetails`
--

INSERT INTO `staffapp_tbl_purchasedetails` (`purchasedetailsid`, `quantity`, `productprice`, `productid_id`, `purchasemasterid_id`, `staffid_id`) VALUES
(6, 30, 4800, 5, 3, 5),
(9, 10, 300, 7, 5, 5),
(10, 10, 1600, 5, 5, 5),
(11, 10, 1600, 5, 6, 5),
(12, 10, 900, 11, 6, 5),
(13, 10, 1600, 5, 7, 5),
(14, 20, 1800, 11, 7, 5),
(15, 20, 600, 7, 7, 5),
(16, 20, 700, 8, 7, 5),
(17, 10, 1600, 5, 8, 5),
(18, 10, 900, 11, 8, 5),
(21, 5, 800, 5, 10, 5),
(22, 5, 400, 10, 10, 5),
(25, 10, 5000, 15, 11, 6),
(26, 10, 2500, 16, 11, 6),
(27, 10, 3500, 17, 11, 6),
(28, 10, 500, 6, 11, 6);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_purchasemaster`
--

CREATE TABLE `staffapp_tbl_purchasemaster` (
  `purchasemasterid` int(11) NOT NULL,
  `purchasedate` date NOT NULL,
  `totalamount` int(11) NOT NULL,
  `billno` int(11) NOT NULL,
  `dealerid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_purchasemaster`
--

INSERT INTO `staffapp_tbl_purchasemaster` (`purchasemasterid`, `purchasedate`, `totalamount`, `billno`, `dealerid_id`) VALUES
(3, '2025-03-08', 4800, 2, 9),
(5, '2025-03-23', 1900, 1000, 9),
(6, '2025-03-26', 2500, 1000, 10),
(7, '2025-03-26', 4700, 1001, 10),
(8, '2025-03-27', 2500, 1005, 10),
(10, '2025-04-21', 1200, 1007, 10),
(11, '2025-04-19', 11500, 2000, 10);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_requestdetails`
--

CREATE TABLE `staffapp_tbl_requestdetails` (
  `requestid` int(11) NOT NULL,
  `requestdate` date NOT NULL,
  `remark` varchar(25) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `status` varchar(25) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `dealerquantity` int(11) DEFAULT NULL,
  `productid_id` int(11) NOT NULL,
  `requestmasterid_id` int(11) DEFAULT NULL,
  `staffid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_requestdetails`
--

INSERT INTO `staffapp_tbl_requestdetails` (`requestid`, `requestdate`, `remark`, `price`, `status`, `quantity`, `dealerquantity`, `productid_id`, `requestmasterid_id`, `staffid_id`) VALUES
(4, '2025-03-08', 'products', 4800, 'Completed', 50, 30, 5, 2, 5),
(5, '2025-03-14', 'products', 500, 'Completed', 30, 10, 6, 3, 5),
(6, '2025-03-14', 'products', 600, 'Completed', 30, 20, 7, 3, 5),
(11, '2025-03-24', '', 250, 'Completed', 10, 5, 6, 4, 5),
(12, '2025-03-25', 'purchase', 1600, 'Completed', 10, 10, 5, 5, 5),
(13, '2025-03-25', 'purchase', 1800, 'Completed', 30, 20, 11, 5, 5),
(14, '2025-03-25', 'purchase', 600, 'Completed', 20, 20, 7, 5, 5),
(15, '2025-03-25', 'purchase', 700, 'Completed', 20, 20, 8, 5, 5),
(20, '2025-03-27', 'need supply', 1600, 'Completed', 20, 10, 5, 6, 5),
(21, '2025-03-27', 'need supply', 900, 'Completed', 20, 10, 11, 6, 5),
(25, '2025-03-27', 'need product', 1600, 'Completed', 10, 10, 5, 12, 5),
(26, '2025-03-27', 'need product', 160, 'Completed', 2, 2, 12, 12, 6),
(27, '2025-03-27', 'need product', 700, 'Completed', 10, 10, 13, 12, 6),
(37, '2025-04-08', 'need items', 800, 'Completed', 5, 5, 5, 19, 5),
(38, '2025-04-08', 'need items', 400, 'Completed', 5, 5, 10, 19, 5),
(39, '2025-04-15', 'Need products', 5000, 'Completed', 10, 10, 15, 20, 9),
(40, '2025-04-15', 'Need products', 2500, 'Completed', 10, 10, 16, 20, 9),
(41, '2025-04-15', 'Need products', 3500, 'Completed', 20, 10, 17, 20, 9),
(42, '2025-04-15', 'need product', 500, 'Completed', 20, 10, 6, 21, 5),
(43, '2025-04-21', 'need products', 1600, 'Completed', 20, 10, 5, 22, 5),
(44, '2025-04-21', 'need products', 3500, 'Completed', 30, 10, 17, 22, 9);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_requestmaster`
--

CREATE TABLE `staffapp_tbl_requestmaster` (
  `requestmasterid` int(11) NOT NULL,
  `deliverydate` date DEFAULT NULL,
  `totalamount` int(11) NOT NULL,
  `status` varchar(25) NOT NULL,
  `dealerid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_requestmaster`
--

INSERT INTO `staffapp_tbl_requestmaster` (`requestmasterid`, `deliverydate`, `totalamount`, `status`, `dealerid_id`) VALUES
(2, '2025-03-18', 4800, 'Completed', 9),
(3, '2025-03-19', 1100, 'Completed', 9),
(4, '2025-03-26', 250, 'Completed', 9),
(5, '2025-03-28', 4700, 'Completed', 10),
(6, '2025-03-30', 2500, 'Completed', 10),
(12, '2025-03-29', 2460, 'Completed', 9),
(19, '2025-04-23', 1200, 'Completed', 10),
(20, '2025-04-19', 11000, 'Completed', 10),
(21, '2025-04-19', 500, 'Completed', 10),
(22, '2025-04-30', 5100, 'Completed', 10);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_salesdetails`
--

CREATE TABLE `staffapp_tbl_salesdetails` (
  `salesdetailsid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `productamount` int(11) NOT NULL,
  `productid_id` int(11) NOT NULL,
  `salesmasterid_id` int(11) DEFAULT NULL,
  `staffid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_salesdetails`
--

INSERT INTO `staffapp_tbl_salesdetails` (`salesdetailsid`, `quantity`, `productamount`, `productid_id`, `salesmasterid_id`, `staffid_id`) VALUES
(5, 10, 400, 7, 2, 5),
(6, 50, 10000, 5, 2, 5),
(8, 2, 80, 7, 3, 5),
(10, 10, 2000, 5, 3, 5),
(11, 10, 2000, 5, 4, 5),
(12, 10, 1200, 11, 4, 5),
(13, 20, 800, 7, 5, 5),
(14, 10, 1200, 11, 6, 5),
(15, 10, 400, 7, 6, 5),
(16, 10, 940, 1, NULL, NULL),
(17, 20, 1800, 12, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `staffapp_tbl_salesmaster`
--

CREATE TABLE `staffapp_tbl_salesmaster` (
  `salesmasterid` int(11) NOT NULL,
  `salesdate` date NOT NULL,
  `totalamount` int(11) NOT NULL,
  `billingno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffapp_tbl_salesmaster`
--

INSERT INTO `staffapp_tbl_salesmaster` (`salesmasterid`, `salesdate`, `totalamount`, `billingno`) VALUES
(1, '2025-02-23', 1165, 1000),
(2, '2025-03-14', 10400, 1000),
(3, '2025-03-23', 2080, 1000),
(4, '2025-03-26', 3200, 2000),
(5, '2025-03-27', 800, 1001),
(6, '2025-04-08', 1600, 1000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminapp_tbl_brand`
--
ALTER TABLE `adminapp_tbl_brand`
  ADD PRIMARY KEY (`brandid`);

--
-- Indexes for table `adminapp_tbl_category`
--
ALTER TABLE `adminapp_tbl_category`
  ADD PRIMARY KEY (`categoryid`);

--
-- Indexes for table `adminapp_tbl_dealer`
--
ALTER TABLE `adminapp_tbl_dealer`
  ADD PRIMARY KEY (`dealerid`),
  ADD KEY `AdminApp_tbl_dealer_locationid_id_1fe5dbab_fk_AdminApp_` (`locationid_id`),
  ADD KEY `AdminApp_tbl_dealer_loginid_id_0620e816_fk_GuestApp_` (`loginid_id`);

--
-- Indexes for table `adminapp_tbl_district`
--
ALTER TABLE `adminapp_tbl_district`
  ADD PRIMARY KEY (`districtid`);

--
-- Indexes for table `adminapp_tbl_location`
--
ALTER TABLE `adminapp_tbl_location`
  ADD PRIMARY KEY (`locationid`),
  ADD KEY `AdminApp_tbl_locatio_districtid_id_629ca474_fk_AdminApp_` (`districtid_id`);

--
-- Indexes for table `adminapp_tbl_product`
--
ALTER TABLE `adminapp_tbl_product`
  ADD PRIMARY KEY (`productid`),
  ADD KEY `AdminApp_tbl_product_brandid_id_ae386c5b_fk_AdminApp_` (`brandid_id`),
  ADD KEY `AdminApp_tbl_product_subcategoryid_id_d19e35dd_fk_AdminApp_` (`subcategoryid_id`);

--
-- Indexes for table `adminapp_tbl_staff`
--
ALTER TABLE `adminapp_tbl_staff`
  ADD PRIMARY KEY (`staffid`),
  ADD KEY `AdminApp_tbl_staff_categoryid_id_31da06b9_fk_AdminApp_` (`categoryid_id`),
  ADD KEY `AdminApp_tbl_staff_locationid_id_5b1c1df0_fk_AdminApp_` (`locationid_id`),
  ADD KEY `AdminApp_tbl_staff_loginid_id_a6b82236_fk_GuestApp_` (`loginid_id`);

--
-- Indexes for table `adminapp_tbl_stock`
--
ALTER TABLE `adminapp_tbl_stock`
  ADD PRIMARY KEY (`stockid`),
  ADD KEY `AdminApp_tbl_stock_productid_id_1a67ce74_fk_AdminApp_` (`productid_id`);

--
-- Indexes for table `adminapp_tbl_subcategory`
--
ALTER TABLE `adminapp_tbl_subcategory`
  ADD PRIMARY KEY (`subcategoryid`),
  ADD KEY `AdminApp_tbl_subcate_categoryid_id_c99984df_fk_AdminApp_` (`categoryid_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `guestapp_tbl_login`
--
ALTER TABLE `guestapp_tbl_login`
  ADD PRIMARY KEY (`loginid`);

--
-- Indexes for table `staffapp_tbl_payment`
--
ALTER TABLE `staffapp_tbl_payment`
  ADD PRIMARY KEY (`paymentid`),
  ADD KEY `StaffApp_tbl_payment_purchasemasterid_id_5caf299f_fk_StaffApp_` (`purchasemasterid_id`);

--
-- Indexes for table `staffapp_tbl_purchasedetails`
--
ALTER TABLE `staffapp_tbl_purchasedetails`
  ADD PRIMARY KEY (`purchasedetailsid`),
  ADD KEY `StaffApp_tbl_purchas_productid_id_329a2cba_fk_AdminApp_` (`productid_id`),
  ADD KEY `StaffApp_tbl_purchas_purchasemasterid_id_94e433c7_fk_StaffApp_` (`purchasemasterid_id`),
  ADD KEY `StaffApp_tbl_purchas_staffid_id_af756e32_fk_AdminApp_` (`staffid_id`);

--
-- Indexes for table `staffapp_tbl_purchasemaster`
--
ALTER TABLE `staffapp_tbl_purchasemaster`
  ADD PRIMARY KEY (`purchasemasterid`),
  ADD KEY `StaffApp_tbl_purchas_dealerid_id_b911a543_fk_AdminApp_` (`dealerid_id`);

--
-- Indexes for table `staffapp_tbl_requestdetails`
--
ALTER TABLE `staffapp_tbl_requestdetails`
  ADD PRIMARY KEY (`requestid`),
  ADD KEY `StaffApp_tbl_request_productid_id_9d16edf4_fk_AdminApp_` (`productid_id`),
  ADD KEY `StaffApp_tbl_request_requestmasterid_id_e335506a_fk_StaffApp_` (`requestmasterid_id`),
  ADD KEY `StaffApp_tbl_request_staffid_id_b275704a_fk_AdminApp_` (`staffid_id`);

--
-- Indexes for table `staffapp_tbl_requestmaster`
--
ALTER TABLE `staffapp_tbl_requestmaster`
  ADD PRIMARY KEY (`requestmasterid`),
  ADD KEY `StaffApp_tbl_request_dealerid_id_a2d50fcc_fk_AdminApp_` (`dealerid_id`);

--
-- Indexes for table `staffapp_tbl_salesdetails`
--
ALTER TABLE `staffapp_tbl_salesdetails`
  ADD PRIMARY KEY (`salesdetailsid`),
  ADD KEY `StaffApp_tbl_salesde_productid_id_60a09d9c_fk_AdminApp_` (`productid_id`),
  ADD KEY `StaffApp_tbl_salesde_salesmasterid_id_53bc93d0_fk_StaffApp_` (`salesmasterid_id`),
  ADD KEY `StaffApp_tbl_salesde_staffid_id_9d1bdf76_fk_AdminApp_` (`staffid_id`);

--
-- Indexes for table `staffapp_tbl_salesmaster`
--
ALTER TABLE `staffapp_tbl_salesmaster`
  ADD PRIMARY KEY (`salesmasterid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminapp_tbl_brand`
--
ALTER TABLE `adminapp_tbl_brand`
  MODIFY `brandid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `adminapp_tbl_category`
--
ALTER TABLE `adminapp_tbl_category`
  MODIFY `categoryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `adminapp_tbl_dealer`
--
ALTER TABLE `adminapp_tbl_dealer`
  MODIFY `dealerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `adminapp_tbl_district`
--
ALTER TABLE `adminapp_tbl_district`
  MODIFY `districtid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `adminapp_tbl_location`
--
ALTER TABLE `adminapp_tbl_location`
  MODIFY `locationid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `adminapp_tbl_product`
--
ALTER TABLE `adminapp_tbl_product`
  MODIFY `productid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `adminapp_tbl_staff`
--
ALTER TABLE `adminapp_tbl_staff`
  MODIFY `staffid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `adminapp_tbl_stock`
--
ALTER TABLE `adminapp_tbl_stock`
  MODIFY `stockid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `adminapp_tbl_subcategory`
--
ALTER TABLE `adminapp_tbl_subcategory`
  MODIFY `subcategoryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `guestapp_tbl_login`
--
ALTER TABLE `guestapp_tbl_login`
  MODIFY `loginid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `staffapp_tbl_payment`
--
ALTER TABLE `staffapp_tbl_payment`
  MODIFY `paymentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `staffapp_tbl_purchasedetails`
--
ALTER TABLE `staffapp_tbl_purchasedetails`
  MODIFY `purchasedetailsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `staffapp_tbl_purchasemaster`
--
ALTER TABLE `staffapp_tbl_purchasemaster`
  MODIFY `purchasemasterid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `staffapp_tbl_requestdetails`
--
ALTER TABLE `staffapp_tbl_requestdetails`
  MODIFY `requestid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `staffapp_tbl_requestmaster`
--
ALTER TABLE `staffapp_tbl_requestmaster`
  MODIFY `requestmasterid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `staffapp_tbl_salesdetails`
--
ALTER TABLE `staffapp_tbl_salesdetails`
  MODIFY `salesdetailsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `staffapp_tbl_salesmaster`
--
ALTER TABLE `staffapp_tbl_salesmaster`
  MODIFY `salesmasterid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adminapp_tbl_dealer`
--
ALTER TABLE `adminapp_tbl_dealer`
  ADD CONSTRAINT `AdminApp_tbl_dealer_locationid_id_1fe5dbab_fk_AdminApp_` FOREIGN KEY (`locationid_id`) REFERENCES `adminapp_tbl_location` (`locationid`),
  ADD CONSTRAINT `AdminApp_tbl_dealer_loginid_id_0620e816_fk_GuestApp_` FOREIGN KEY (`loginid_id`) REFERENCES `guestapp_tbl_login` (`loginid`);

--
-- Constraints for table `adminapp_tbl_location`
--
ALTER TABLE `adminapp_tbl_location`
  ADD CONSTRAINT `AdminApp_tbl_locatio_districtid_id_629ca474_fk_AdminApp_` FOREIGN KEY (`districtid_id`) REFERENCES `adminapp_tbl_district` (`districtid`);

--
-- Constraints for table `adminapp_tbl_product`
--
ALTER TABLE `adminapp_tbl_product`
  ADD CONSTRAINT `AdminApp_tbl_product_brandid_id_ae386c5b_fk_AdminApp_` FOREIGN KEY (`brandid_id`) REFERENCES `adminapp_tbl_brand` (`brandid`),
  ADD CONSTRAINT `AdminApp_tbl_product_subcategoryid_id_d19e35dd_fk_AdminApp_` FOREIGN KEY (`subcategoryid_id`) REFERENCES `adminapp_tbl_subcategory` (`subcategoryid`);

--
-- Constraints for table `adminapp_tbl_staff`
--
ALTER TABLE `adminapp_tbl_staff`
  ADD CONSTRAINT `AdminApp_tbl_staff_categoryid_id_31da06b9_fk_AdminApp_` FOREIGN KEY (`categoryid_id`) REFERENCES `adminapp_tbl_category` (`categoryid`),
  ADD CONSTRAINT `AdminApp_tbl_staff_locationid_id_5b1c1df0_fk_AdminApp_` FOREIGN KEY (`locationid_id`) REFERENCES `adminapp_tbl_location` (`locationid`),
  ADD CONSTRAINT `AdminApp_tbl_staff_loginid_id_a6b82236_fk_GuestApp_` FOREIGN KEY (`loginid_id`) REFERENCES `guestapp_tbl_login` (`loginid`);

--
-- Constraints for table `adminapp_tbl_stock`
--
ALTER TABLE `adminapp_tbl_stock`
  ADD CONSTRAINT `AdminApp_tbl_stock_productid_id_1a67ce74_fk_AdminApp_` FOREIGN KEY (`productid_id`) REFERENCES `adminapp_tbl_product` (`productid`);

--
-- Constraints for table `adminapp_tbl_subcategory`
--
ALTER TABLE `adminapp_tbl_subcategory`
  ADD CONSTRAINT `AdminApp_tbl_subcate_categoryid_id_c99984df_fk_AdminApp_` FOREIGN KEY (`categoryid_id`) REFERENCES `adminapp_tbl_category` (`categoryid`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `staffapp_tbl_payment`
--
ALTER TABLE `staffapp_tbl_payment`
  ADD CONSTRAINT `StaffApp_tbl_payment_purchasemasterid_id_5caf299f_fk_StaffApp_` FOREIGN KEY (`purchasemasterid_id`) REFERENCES `staffapp_tbl_purchasemaster` (`purchasemasterid`);

--
-- Constraints for table `staffapp_tbl_purchasedetails`
--
ALTER TABLE `staffapp_tbl_purchasedetails`
  ADD CONSTRAINT `StaffApp_tbl_purchas_productid_id_329a2cba_fk_AdminApp_` FOREIGN KEY (`productid_id`) REFERENCES `adminapp_tbl_product` (`productid`),
  ADD CONSTRAINT `StaffApp_tbl_purchas_purchasemasterid_id_94e433c7_fk_StaffApp_` FOREIGN KEY (`purchasemasterid_id`) REFERENCES `staffapp_tbl_purchasemaster` (`purchasemasterid`),
  ADD CONSTRAINT `StaffApp_tbl_purchas_staffid_id_af756e32_fk_AdminApp_` FOREIGN KEY (`staffid_id`) REFERENCES `adminapp_tbl_staff` (`staffid`);

--
-- Constraints for table `staffapp_tbl_purchasemaster`
--
ALTER TABLE `staffapp_tbl_purchasemaster`
  ADD CONSTRAINT `StaffApp_tbl_purchas_dealerid_id_b911a543_fk_AdminApp_` FOREIGN KEY (`dealerid_id`) REFERENCES `adminapp_tbl_dealer` (`dealerid`);

--
-- Constraints for table `staffapp_tbl_requestdetails`
--
ALTER TABLE `staffapp_tbl_requestdetails`
  ADD CONSTRAINT `StaffApp_tbl_request_productid_id_9d16edf4_fk_AdminApp_` FOREIGN KEY (`productid_id`) REFERENCES `adminapp_tbl_product` (`productid`),
  ADD CONSTRAINT `StaffApp_tbl_request_requestmasterid_id_e335506a_fk_StaffApp_` FOREIGN KEY (`requestmasterid_id`) REFERENCES `staffapp_tbl_requestmaster` (`requestmasterid`),
  ADD CONSTRAINT `StaffApp_tbl_request_staffid_id_b275704a_fk_AdminApp_` FOREIGN KEY (`staffid_id`) REFERENCES `adminapp_tbl_staff` (`staffid`);

--
-- Constraints for table `staffapp_tbl_requestmaster`
--
ALTER TABLE `staffapp_tbl_requestmaster`
  ADD CONSTRAINT `StaffApp_tbl_request_dealerid_id_a2d50fcc_fk_AdminApp_` FOREIGN KEY (`dealerid_id`) REFERENCES `adminapp_tbl_dealer` (`dealerid`);

--
-- Constraints for table `staffapp_tbl_salesdetails`
--
ALTER TABLE `staffapp_tbl_salesdetails`
  ADD CONSTRAINT `StaffApp_tbl_salesde_productid_id_60a09d9c_fk_AdminApp_` FOREIGN KEY (`productid_id`) REFERENCES `adminapp_tbl_product` (`productid`),
  ADD CONSTRAINT `StaffApp_tbl_salesde_salesmasterid_id_53bc93d0_fk_StaffApp_` FOREIGN KEY (`salesmasterid_id`) REFERENCES `staffapp_tbl_salesmaster` (`salesmasterid`),
  ADD CONSTRAINT `StaffApp_tbl_salesde_staffid_id_9d1bdf76_fk_AdminApp_` FOREIGN KEY (`staffid_id`) REFERENCES `adminapp_tbl_staff` (`staffid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
