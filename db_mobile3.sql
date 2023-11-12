-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 12 nov. 2023 à 22:07
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `db_mobile3`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateurs`
--

DROP TABLE IF EXISTS `administrateurs`;
CREATE TABLE IF NOT EXISTS `administrateurs` (
  `user_id` int NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `administrateurs`
--

INSERT INTO `administrateurs` (`user_id`) VALUES
(37);

-- --------------------------------------------------------

--
-- Structure de la table `annedep`
--

DROP TABLE IF EXISTS `annedep`;
CREATE TABLE IF NOT EXISTS `annedep` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_anne` int NOT NULL,
  `id_dep` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_anne` (`id_anne`),
  KEY `id_dep` (`id_dep`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `annedep`
--

INSERT INTO `annedep` (`id`, `id_anne`, `id_dep`) VALUES
(1, 9, 1),
(2, 9, 2),
(3, 8, 3),
(4, 8, 2);

-- --------------------------------------------------------

--
-- Structure de la table `annees_universitaires`
--

DROP TABLE IF EXISTS `annees_universitaires`;
CREATE TABLE IF NOT EXISTS `annees_universitaires` (
  `id` int NOT NULL AUTO_INCREMENT,
  `annee_debut` datetime NOT NULL,
  `annee_fin` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `annees_universitaires`
--

INSERT INTO `annees_universitaires` (`id`, `annee_debut`, `annee_fin`) VALUES
(1, '2014-09-01 00:00:00', '2015-05-01 00:00:00'),
(2, '2015-10-01 00:00:00', '2016-05-25 00:00:00'),
(3, '2016-10-01 00:00:00', '2017-05-25 00:00:00'),
(4, '2017-10-10 00:00:00', '2018-06-25 00:00:00'),
(5, '2018-10-10 00:00:00', '2019-06-25 00:00:00'),
(6, '2019-10-10 00:00:00', '2020-06-25 00:00:00'),
(7, '2020-10-10 00:00:00', '2021-06-25 00:00:00'),
(8, '2021-10-10 00:00:00', '2022-06-25 00:00:00'),
(9, '2022-10-10 00:00:00', '2023-06-25 00:00:00');

-- --------------------------------------------------------

--
-- Structure de la table `creneaux`
--

DROP TABLE IF EXISTS `creneaux`;
CREATE TABLE IF NOT EXISTS `creneaux` (
  `id` int NOT NULL AUTO_INCREMENT,
  `heure_debut` time NOT NULL,
  `heure_fin` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `creneaux`
--

INSERT INTO `creneaux` (`id`, `heure_debut`, `heure_fin`) VALUES
(1, '08:30:01', '10:30:01'),
(2, '10:30:01', '12:30:01'),
(3, '15:00:01', '17:00:01'),
(4, '17:00:01', '19:00:01');

-- --------------------------------------------------------

--
-- Structure de la table `creneau_jour`
--

DROP TABLE IF EXISTS `creneau_jour`;
CREATE TABLE IF NOT EXISTS `creneau_jour` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_jour` int NOT NULL,
  `id_creneau` int NOT NULL,
  `id_mat` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_jour` (`id_jour`),
  KEY `id_creneau` (`id_creneau`),
  KEY `id_mat` (`id_mat`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `creneau_jour`
--

INSERT INTO `creneau_jour` (`id`, `id_jour`, `id_creneau`, `id_mat`) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2),
(3, 2, 2, 5),
(4, 2, 3, 6),
(5, 3, 3, 7),
(6, 3, 4, 8);

-- --------------------------------------------------------

--
-- Structure de la table `departements`
--

DROP TABLE IF EXISTS `departements`;
CREATE TABLE IF NOT EXISTS `departements` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_departement` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `departements`
--

INSERT INTO `departements` (`id`, `nom_departement`) VALUES
(1, 'informatique'),
(2, 'Gestion'),
(3, 'Strategique');

-- --------------------------------------------------------

--
-- Structure de la table `departementssuperviseurs`
--

DROP TABLE IF EXISTS `departementssuperviseurs`;
CREATE TABLE IF NOT EXISTS `departementssuperviseurs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sup` int NOT NULL,
  `id_dep` int NOT NULL,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL,
  PRIMARY KEY (`id`,`id_sup`,`id_dep`,`date_debut`,`date_fin`) USING BTREE,
  KEY `fketu` (`id_sup`),
  KEY `FKMAT` (`id_dep`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `departementssuperviseurs`
--

INSERT INTO `departementssuperviseurs` (`id`, `id_sup`, `id_dep`, `date_debut`, `date_fin`) VALUES
(5, 31, 1, '2022-10-05', '2023-10-31'),
(6, 31, 1, '2022-10-05', '2023-10-31');

-- --------------------------------------------------------

--
-- Structure de la table `etudiants`
--

DROP TABLE IF EXISTS `etudiants`;
CREATE TABLE IF NOT EXISTS `etudiants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matricule` varchar(255) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `photo` varchar(555) DEFAULT NULL,
  `nni` int DEFAULT NULL,
  `genre` varchar(255) NOT NULL,
  `date_inscription` datetime DEFAULT NULL,
  `lieu_n` varchar(255) DEFAULT NULL,
  `date_n` datetime DEFAULT NULL,
  `nationnalite` varchar(255) DEFAULT NULL,
  `tel` int DEFAULT NULL,
  `email` varchar(500) NOT NULL,
  `id_fil` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_fil` (`id_fil`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `etudiants`
--

INSERT INTO `etudiants` (`id`, `matricule`, `nom`, `prenom`, `photo`, `nni`, `genre`, `date_inscription`, `lieu_n`, `date_n`, `nationnalite`, `tel`, `email`, `id_fil`) VALUES
(1, 'IE19253', 'Ahmed', 'Fatimetou', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/etudiants/beybeti.jpg', 2255852, 'f', '2023-10-15 12:43:50', 'btt', '2023-10-15 12:43:50', 'mr', 25896314, 'ie19253.etu@iscae.mr', 1),
(2, 'IE19255', 'El hanevi', 'Kadijeh', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/etudiants/35_1696963528.980369.jpg', 22589631, 'f', '2023-10-15 12:43:50', 'nktt', '2023-10-15 12:43:50', 'mr', 22589631, 'ie19255.etu@iscae.mr', 1),
(3, 'IE19255', 'Beirouk', 'Mohamed', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/etudiants/46_1693646843.588415.jpg', 78787887, 'm', '2023-10-03 18:32:14', 'mnmnmn', '2023-10-02 18:32:14', 'rim', 7878778, 'ie19258.etu@iscae.mr', 1);

-- --------------------------------------------------------

--
-- Structure de la table `evaluation`
--

DROP TABLE IF EXISTS `evaluation`;
CREATE TABLE IF NOT EXISTS `evaluation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(255) DEFAULT NULL,
  `date_debut` datetime DEFAULT NULL,
  `date_fin` datetime DEFAULT NULL,
  `id_sal` int DEFAULT NULL,
  `id_mat` int DEFAULT NULL,
  `id_jour` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_sal` (`id_sal`),
  KEY `id_jour` (`id_jour`),
  KEY `id_mat` (`id_mat`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `evaluation`
--

INSERT INTO `evaluation` (`id`, `type`, `date_debut`, `date_fin`, `id_sal`, `id_mat`, `id_jour`) VALUES
(1, 'Devoir', '2023-10-26 18:25:09', '2023-11-05 18:25:09', 1, 1, 1),
(2, 'Examun', '2023-11-01 15:11:24', '2023-11-12 15:11:24', 2, 2, 1),
(3, 'Session', '2023-10-18 15:16:58', '2023-10-19 15:16:58', 3, 4, 1),
(4, 'Devoir', '2023-10-26 18:25:09', '2023-10-30 18:25:09', 1, 2, 1),
(5, 'Examun', '2023-10-17 15:11:24', '2023-10-29 15:11:24', 2, 1, 1),
(6, 'Session', '2023-10-18 15:16:58', '2023-10-19 15:16:58', 3, 3, 1),
(7, 'Devoir', '2023-10-26 18:25:09', '2023-10-30 18:25:09', 1, 5, 2),
(8, 'Devoir', '2023-10-26 18:25:09', '2023-10-30 18:25:09', 1, 6, 2),
(9, 'Devoir', '2023-10-26 18:25:09', '2023-10-30 18:25:09', 1, 7, 3),
(10, 'Devoir', '2023-10-26 18:25:09', '2023-10-30 18:25:09', 1, 8, 3),
(12, 'Session', '2023-10-26 19:52:00', '2023-10-27 19:52:00', 3, 5, 3);

-- --------------------------------------------------------

--
-- Structure de la table `filiere`
--

DROP TABLE IF EXISTS `filiere`;
CREATE TABLE IF NOT EXISTS `filiere` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(255) NOT NULL,
  `abreviation` varchar(50) DEFAULT NULL,
  `semestre_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `semestre_id` (`semestre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `filiere`
--

INSERT INTO `filiere` (`id`, `libelle`, `abreviation`, `semestre_id`) VALUES
(1, 'Informatique de gestion', 'IG', 1),
(2, 'Developpement informatique', 'DI', 1);

-- --------------------------------------------------------

--
-- Structure de la table `formation`
--

DROP TABLE IF EXISTS `formation`;
CREATE TABLE IF NOT EXISTS `formation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `dep_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dep_id` (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `formation`
--

INSERT INTO `formation` (`id`, `nom`, `dep_id`) VALUES
(1, 'Licence', 1),
(2, 'Master', 1);

-- --------------------------------------------------------

--
-- Structure de la table `historiques`
--

DROP TABLE IF EXISTS `historiques`;
CREATE TABLE IF NOT EXISTS `historiques` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `id_exam` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `historique_ibfk_1` (`id_exam`)
) ENGINE=MyISAM AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `historiques`
--

INSERT INTO `historiques` (`id`, `description`, `id_exam`) VALUES
(7, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle1 pour passer l\'examen session dans la matière java au moment 2023-06-23 23:07:53.386714, le surveillant 11 de la salle N°2', 2),
(8, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-06-23 23:21:19.729734, le surveillant 11 de la salle N°2', 2),
(9, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:28:43.690475, le surveillant 32 de la salle N°2', 2),
(10, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:32:33.952372, le surveillant 32 de la salle N°2', 2),
(11, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:35:32.633656, le surveillant 32 de la salle N°2', 2),
(12, 'Attention étudiant ali ahmed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:36:58.725182, le surveillant 32 de la salle N°2', 2),
(13, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:40:30.469222, le surveillant 32 de la salle N°2', 2),
(14, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:43:45.275643, le surveillant 32 de la salle N°2', 2),
(15, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:03:19.159628, le surveillant 32 de la salle N°3', 2),
(16, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:09:01.663447, le surveillant 32 de la salle N°3', 1),
(17, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:11:00.430738, le surveillant 32 de la salle N°3', 1),
(18, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:14:43.140985, le surveillant 32 de la salle N°3', 2),
(19, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:17:43.771852, le surveillant 32 de la salle N°3', 1),
(20, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:18.378530, le surveillant 32 de la salle N°3', 1),
(21, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:40.553881, le surveillant 32 de la salle N°3', 1),
(22, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:20:46.269362, le surveillant 32 de la salle N°3', 1),
(23, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:22:40.833943, le surveillant 32 de la salle N°3', 1),
(24, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:23:15.145559, le surveillant 32 de la salle N°3', 1),
(25, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:26:31.561962, le surveillant 32 de la salle N°3', 1),
(26, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:27:49.736628, le surveillant 32 de la salle N°3', 2),
(27, 'Attention étudiant Emin ahmed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-03 01:07:10.856004, le surveillant 32 de la salle N°3', 2),
(28, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-03 01:07:49.620570, le surveillant 32 de la salle N°3', 2),
(29, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:39:09.928598, le surveillant 37 de la salle N°5', 4),
(30, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:39:39.593400, le surveillant 37 de la salle N°5', 4),
(31, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:40:39.473049, le surveillant 37 de la salle N°5', 4),
(32, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-30 17:11:05.343736, le surveillant 37 de la salle N°5', 4),
(33, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 17:42:54.556470, le surveillant 37 de la salle N°5', 4),
(34, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 20:41:50.909441, le surveillant 37 de la salle N°5', 4),
(35, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 20:43:19.468344, le surveillant 37 de la salle N°5', 4),
(36, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:11:14.459752, le surveillant 37 de la salle N°5', 4),
(37, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:18:19.012035, le surveillant 37 de la salle N°5', 4),
(38, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:29:20.341565, le surveillant 37 de la salle N°5', 4),
(39, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:29:24.443679, le surveillant 37 de la salle N°5', 4),
(40, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:45:07.840257, le surveillant 36 de la salle N°3', 2),
(41, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:46:50.259064, le surveillant 36 de la salle N°3', 2),
(42, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:48:03.577913, le surveillant 36 de la salle N°3', 2),
(43, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:48:57.768148, le surveillant 36 de la salle N°3', 2),
(44, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:50:51.535906, le surveillant 36 de la salle N°3', 2),
(45, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:31:05.135475, le surveillant 36 de la salle N°3', 2),
(46, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:45:32.857887, le surveillant 36 de la salle N°3', 2),
(47, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:49:39.524261, le surveillant 36 de la salle N°3', 2),
(48, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:50:11.259844, le surveillant 36 de la salle N°3', 2),
(49, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:16:52.079849, le surveillant 36 de la salle N°3', 2),
(50, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:32:33.554230, le surveillant 36 de la salle N°3', 2),
(51, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:33:09.759720, le surveillant 36 de la salle N°3', 2),
(52, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:35:24.648864, le surveillant 36 de la salle N°3', 2),
(53, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:36:47.791711, le surveillant 36 de la salle N°3', 2),
(54, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-30 11:57:01.829005, le surveillant 36 de la salle N°3', 2),
(55, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:37:20.707924, le surveillant 36 de la salle N°3', 2),
(56, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:38:18.970402, le surveillant 36 de la salle N°3', 2),
(57, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:39:35.113329, le surveillant 36 de la salle N°3', 2),
(58, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:39:57.466514, le surveillant 36 de la salle N°3', 2),
(59, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 14:03:56.022183, le surveillant 36 de la salle N°3', 2),
(60, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 15:36:04.975987, le surveillant 36 de la salle N°3', 2),
(61, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 15:42:56.442516, le surveillant 36 de la salle N°3', 2),
(62, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 11:23:16.658515, le surveillant 36 de la salle N°3', 2),
(63, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 11:38:04.834614, le surveillant 36 de la salle N°3', 2),
(64, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:37:32.799379, le surveillant 36 de la salle N°3', 2),
(65, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:39:04.643223, le surveillant 36 de la salle N°3', 2),
(66, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:59:57.622982, le surveillant 36 de la salle N°3', 2),
(67, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 16:16:09.190800, le surveillant 36 de la salle N°3', 2),
(68, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 16:40:52.124425, le surveillant 36 de la salle N°3', 2),
(69, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 17:05:45.911814, le surveillant 36 de la salle N°3', 2),
(70, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 17:21:43.712506, le surveillant 36 de la salle N°3', 2),
(71, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:10:36.538122, le surveillant 36 de la salle N°3', 2),
(72, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:43:26.776415, le surveillant 36 de la salle N°3', 2),
(73, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:47:02.026651, le surveillant 36 de la salle N°3', 2),
(74, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 09:53:25.828878, le surveillant 36 de la salle N°3', 2),
(75, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 09:56:10.294605, le surveillant 36 de la salle N°3', 2),
(76, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 10:28:07.586710, le surveillant 36 de la salle N°3', 2),
(77, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 10:28:26.107016, le surveillant 36 de la salle N°3', 2),
(78, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 12:04:57.327299, le surveillant 36 de la salle N°3', 2),
(79, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 12:40:29.675705, le surveillant 36 de la salle N°3', 2),
(80, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:30:07.126878, le surveillant 36 de la salle N°5', 4),
(81, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:31:27.130483, le surveillant 36 de la salle N°5', 4),
(82, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:41:50.483829, le surveillant 36 de la salle N°5', 4),
(83, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:43:34.431034, le surveillant 36 de la salle N°5', 4),
(84, 'Attention étudiant medelhanevy khadije n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:53:32.760995, le surveillant 36 de la salle N°5', 4),
(85, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:55:08.235245, le surveillant 36 de la salle N°5', 4),
(86, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:05:41.982160, le surveillant 36 de la salle N°1', 1),
(87, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:22:07.506178, le surveillant 36 de la salle N°1', 1),
(88, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:23:28.309295, le surveillant 36 de la salle N°1', 1),
(89, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:52:36.504286, le surveillant 36 de la salle N°1', 1),
(90, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:54:39.243350, le surveillant 36 de la salle N°1', 1),
(91, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:56:03.636784, le surveillant 36 de la salle N°1', 1),
(92, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:58:25.088339, le surveillant 36 de la salle N°1', 1),
(93, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 18:59:33.047552, le surveillant 36 de la salle N°1', 1),
(94, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:01:22.040167, le surveillant 36 de la salle N°1', 1),
(95, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:03:27.057560, le surveillant 36 de la salle N°1', 1),
(96, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:07:15.519047, le surveillant 36 de la salle N°1', 1),
(97, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:08:32.079024, le surveillant 36 de la salle N°1', 1),
(98, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:52:02.800267, le surveillant 36 de la salle N°1', 1),
(99, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:53:34.090506, le surveillant 36 de la salle N°1', 1),
(100, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:55:14.049821, le surveillant 36 de la salle N°1', 1),
(101, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 19:57:28.703094, le surveillant 36 de la salle N°1', 1),
(102, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:00:13.833325, le surveillant 36 de la salle N°1', 1),
(103, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:01:49.215709, le surveillant 36 de la salle N°1', 1),
(104, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:05:17.905016, le surveillant 36 de la salle N°1', 1),
(105, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:07:19.451713, le surveillant 36 de la salle N°1', 1),
(106, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:22:44.258155, le surveillant 36 de la salle N°1', 1),
(107, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 20:29:59.935609, le surveillant 36 de la salle N°1', 1),
(108, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:04:27.227049, le surveillant 36 de la salle N°1', 1),
(109, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:09:42.703371, le surveillant 36 de la salle N°1', 1),
(110, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:14:06.144342, le surveillant 36 de la salle N°1', 1),
(111, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:18:36.496611, le surveillant 36 de la salle N°1', 1),
(112, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:27:51.574598, le surveillant 36 de la salle N°1', 1),
(113, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:30:42.721349, le surveillant 36 de la salle N°1', 1),
(114, 'Attention étudiant Ahmed Fatimetou n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:36:07.697252, le surveillant 36 de la salle N°0', 1),
(115, 'Attention étudiant med Medos n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:37:07.784230, le surveillant 36 de la salle N°0', 1),
(116, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:38:39.146123, le surveillant 36 de la salle N°1', 1),
(117, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:39:10.700823, le surveillant 36 de la salle N°1', 1),
(118, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:42:24.141397, le surveillant 36 de la salle N°1', 1),
(119, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 21:58:55.503737, le surveillant 36 de la salle N°1', 1),
(120, 'Attention étudiant Ahmed Fatimetou n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:09:21.548893, le surveillant 36 de la salle N°0', 1),
(121, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:10:13.607478, le surveillant 36 de la salle N°1', 1),
(122, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:16:02.319661, le surveillant 36 de la salle N°1', 1),
(123, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:17:54.988994, le surveillant 36 de la salle N°1', 1),
(124, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:24:25.203967, le surveillant 36 de la salle N°1', 1),
(125, 'Attention étudiant Ahmed Fatimetou n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:25:15.636219, le surveillant 36 de la salle N°0', 1),
(126, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:27:18.871096, le surveillant 36 de la salle N°1', 1),
(127, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 22:38:13.763867, le surveillant 36 de la salle N°1', 1),
(128, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 23:05:28.193602, le surveillant 36 de la salle N°1', 1),
(129, 'Attention étudiant El hanevi Kadijeh n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 23:19:00.037505, le surveillant 36 de la salle N°0', 1),
(130, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-24 00:09:53.789902, le surveillant 36 de la salle N°1', 1),
(131, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-24 00:13:59.039223, le surveillant 36 de la salle N°1', 1),
(132, 'Attention étudiant Kadijeh El hanevi n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle 2 pour passer  Examun dans la matière python au moment 2023-11-07 14:48:14.692002, le surveillant Depends(recupere_userid) de la salle N°0', 2);

-- --------------------------------------------------------

--
-- Structure de la table `jours`
--

DROP TABLE IF EXISTS `jours`;
CREATE TABLE IF NOT EXISTS `jours` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `jours`
--

INSERT INTO `jours` (`id`, `libelle`, `date`) VALUES
(1, 'Dimanche', '2023-10-29 18:30:21'),
(2, 'Lundi', '2023-10-30 18:00:49'),
(3, 'Mardi', '2023-10-31 18:00:49'),
(4, 'Mercredi', '2023-11-01 18:00:49'),
(5, 'Jeudi', '2023-11-02 18:00:49'),
(6, 'Vendredi', '2023-11-03 18:00:49'),
(7, 'Samedi', '2023-11-04 18:00:49');

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
CREATE TABLE IF NOT EXISTS `matieres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(255) DEFAULT NULL,
  `nbr_heure` int DEFAULT NULL,
  `credit` int DEFAULT NULL,
  `id_fil` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_fil` (`id_fil`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`id`, `libelle`, `nbr_heure`, `credit`, `id_fil`) VALUES
(1, 'Intelligence artificielle', 40, 4, 1),
(2, 'Python', 40, 5, 1),
(3, 'Strategique', 40, 5, 2),
(4, 'Strategique', 40, 5, 2),
(5, 'Compilation', 20, 2, 1),
(6, 'Java', 50, 4, 1),
(7, 'C++', 20, 2, 1),
(8, 'C#', 50, 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `niveau`
--

DROP TABLE IF EXISTS `niveau`;
CREATE TABLE IF NOT EXISTS `niveau` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `formation_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `formation_id` (`formation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `niveau`
--

INSERT INTO `niveau` (`id`, `nom`, `formation_id`) VALUES
(1, 'L1', 1),
(2, 'L2', 1),
(3, 'L3', 1);

-- --------------------------------------------------------

--
-- Structure de la table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
CREATE TABLE IF NOT EXISTS `notifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(250) NOT NULL,
  `date` datetime NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `surveillant_id` int DEFAULT NULL,
  `id_exam` int NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_exam` (`id_exam`),
  KEY `surveillant_id` (`surveillant_id`)
) ENGINE=MyISAM AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `notifications`
--

INSERT INTO `notifications` (`id`, `content`, `date`, `is_read`, `surveillant_id`, `id_exam`, `image`) VALUES
(2, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:32:33.952372, le surveillant 32 de la salle N°2', '2023-07-04 16:32:34', 1, 67, 0, 'images/medos.jpeg'),
(3, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:35:32.633656, le surveillant 32 de la salle N°2', '2023-07-04 16:35:33', 1, 67, 5, 'images/chou3ayb.jpeg'),
(4, 'Attention étudiant ali ahmed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:36:58.725182, le surveillant 32 de la salle N°2', '2023-07-04 16:36:59', 1, 67, 5, 'images/mbare.jpeg'),
(5, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:40:30.469222, le surveillant 32 de la salle N°2', '2023-07-04 16:40:30', 1, 67, 5, 'images/user.jpg'),
(6, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:43:45.275643, le surveillant 32 de la salle N°2', '2023-07-04 16:43:45', 1, 67, 5, 'images/jorjina.jpg'),
(7, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:03:19.159628, le surveillant 32 de la salle N°3', '2023-08-02 21:03:19', 1, 67, 5, 'images/elone1.jpg'),
(65, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:47:02.026651, le surveillant 36 de la salle N°3', '2023-10-03 19:47:02', 1, 67, 2, 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications/1696419756.868977.jpg'),
(121, 'Attention étudiant El hanevi sidi n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-23 23:19:00.037505, le surveillant 36 de la salle N°0', '2023-10-23 23:19:00', 0, 67, 1, 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications/1696410791.995372.jpg'),
(123, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen Devoir dans la matière IA au moment 2023-10-24 00:13:59.039223, le surveillant 36 de la salle N°1', '2023-10-24 00:13:59', 0, 67, 1, 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/notifications/1693669503.817441.jpg'),
(124, 'Attention étudiant Kadijeh El hanevi n\'a pas d\'examen en ce moment  et tente d\'entrer dans la salle 2 pour passer  Examun dans la matière python au moment 2023-11-07 14:48:14.692002, le surveillant Depends(recupere_userid) de la salle N°0', '2023-11-07 14:48:15', 0, 0, 2, 'hjhhh');

-- --------------------------------------------------------

--
-- Structure de la table `pv`
--

DROP TABLE IF EXISTS `pv`;
CREATE TABLE IF NOT EXISTS `pv` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `nni` varchar(20) DEFAULT NULL,
  `description` text,
  `photo` varchar(255) DEFAULT NULL,
  `date_pv` datetime DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `tel` int DEFAULT NULL,
  `surveillant_id` int NOT NULL,
  `etat` varchar(50) NOT NULL,
  `id_eval` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_surv` (`surveillant_id`),
  KEY `id_eval` (`id_eval`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `pv`
--

INSERT INTO `pv` (`id`, `nom`, `nni`, `description`, `photo`, `date_pv`, `type`, `tel`, `surveillant_id`, `etat`, `id_eval`) VALUES
(9, 'bvhhjjh', '66676', 'hjhjhjjh', 'C:\\Users\\pc\\StudioProjects\\pfe\\PFE_FRONT\\images\\pv\\1698517465.515398.jpg', '2023-10-28 20:24:26', 'jhhjhjhj', 2147483647, 68, 'accepter', 2),
(1, 'bnbnbb', '4433443', 'nbnbbnbnnb', 'C:\\Users\\pc\\StudioProjects\\pfe\\PFE_FRONT\\images\\pv\\1698513988.825405.jpg', '2023-10-28 19:26:29', 'bnbbnnb', 23323332, 67, 'initial', 1);

-- --------------------------------------------------------

--
-- Structure de la table `salles`
--

DROP TABLE IF EXISTS `salles`;
CREATE TABLE IF NOT EXISTS `salles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `salles`
--

INSERT INTO `salles` (`id`, `nom`) VALUES
(1, 'Salle 01'),
(2, 'Salle 02'),
(3, 'Salle 03');

-- --------------------------------------------------------

--
-- Structure de la table `semestre`
--

DROP TABLE IF EXISTS `semestre`;
CREATE TABLE IF NOT EXISTS `semestre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(255) NOT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `niveau_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `niveau_id` (`niveau_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `semestre`
--

INSERT INTO `semestre` (`id`, `libelle`, `date_debut`, `date_fin`, `niveau_id`) VALUES
(1, 'S1', '2023-10-01', '2023-12-30', 1),
(2, 'S4', '2023-10-02', '2023-10-01', 2),
(3, 'S2', '2023-10-03', '2023-10-12', 1);

-- --------------------------------------------------------

--
-- Structure de la table `superviseurs`
--

DROP TABLE IF EXISTS `superviseurs`;
CREATE TABLE IF NOT EXISTS `superviseurs` (
  `user_id` int NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `superviseurs`
--

INSERT INTO `superviseurs` (`user_id`) VALUES
(31),
(55);

-- --------------------------------------------------------

--
-- Structure de la table `surveillancesuperviseur`
--

DROP TABLE IF EXISTS `surveillancesuperviseur`;
CREATE TABLE IF NOT EXISTS `surveillancesuperviseur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sup` int NOT NULL,
  `id_sal` varchar(50) NOT NULL,
  `id_eval` int NOT NULL,
  PRIMARY KEY (`id`,`id_sup`,`id_sal`,`id_eval`),
  KEY `id_sup` (`id_sup`),
  KEY `id_sal` (`id_sal`),
  KEY `id_eval` (`id_eval`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `surveillancesuperviseur`
--

INSERT INTO `surveillancesuperviseur` (`id`, `id_sup`, `id_sal`, `id_eval`) VALUES
(4, 31, '1;2', 1),
(11, 31, '1;2', 2),
(13, 55, '2,3', 6),
(14, 55, '2,3', 6),
(15, 0, '2;3', 0),
(16, 55, '1;2', 12);

-- --------------------------------------------------------

--
-- Structure de la table `surveillants`
--

DROP TABLE IF EXISTS `surveillants`;
CREATE TABLE IF NOT EXISTS `surveillants` (
  `user_id` int NOT NULL,
  `id_sal` int DEFAULT NULL,
  `typecompte` varchar(255) NOT NULL DEFAULT 'principale',
  PRIMARY KEY (`user_id`),
  KEY `id_sal` (`id_sal`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `surveillants`
--

INSERT INTO `surveillants` (`user_id`, `id_sal`, `typecompte`) VALUES
(67, 1, 'principale'),
(68, 2, 'salle');

-- --------------------------------------------------------

--
-- Structure de la table `types`
--

DROP TABLE IF EXISTS `types`;
CREATE TABLE IF NOT EXISTS `types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `id_surv` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_surv` (`id_surv`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pswd` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `photo` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UC_users_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom`, `prenom`, `email`, `pswd`, `role`, `photo`) VALUES
(31, 'mouhamed', 'amina', 'amina@gmail.com', '$2b$12$cSqXtKMC642k.1VkHAFjW.q/VYMJq.zSBzbDdOM4Sm.NNAfc.oCMS', 'superviseur', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/users/1695212600.736195.jpg'),
(37, 'M beirik', 'Mouhamed', 'admin@gmail.com', '$2b$12$wSM3of2sH6TfOhBvr8mTiutg98xXjHy98aHM7w/gl5Y5XsJhFwnb6', 'admin', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/users/1693669503.817441.jpg'),
(55, 'oussama', 'issa', 'issa@gmail.com', '$2b$12$lKCYFDQvJGIZ2l.b52aQuuBn5ksH3W4m7JGIB.SrRZbBQWYLHqRXO', 'superviseur', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/1693669843.300792.jpg'),
(67, 'Beirouk', 'Mouhamed', 'user@gmail.com', '$2b$12$oClY7rnZBubOVCM31ZjdJ.lhaiR1CVdw9KSp96o8PxgzJKvWaHTya', 'surveillant', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/users/1698341766.659319.jpg'),
(68, 'Youssif', 'Sami', 'user2@gmail.com', '$2b$12$N57gaF4IJR7X.FORopS5Du3jEDQafb.i/VgMvrUTb6F/.IqIVMkji', 'surveillant', 'C:/Users/pc/StudioProjects/pfe/PFE_FRONT/images/users/1698489204.45896.jpg');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD CONSTRAINT `administrateurs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Contraintes pour la table `annedep`
--
ALTER TABLE `annedep`
  ADD CONSTRAINT `annedep_ibfk_1` FOREIGN KEY (`id_anne`) REFERENCES `annees_universitaires` (`id`),
  ADD CONSTRAINT `annedep_ibfk_2` FOREIGN KEY (`id_dep`) REFERENCES `departements` (`id`);

--
-- Contraintes pour la table `etudiants`
--
ALTER TABLE `etudiants`
  ADD CONSTRAINT `etudiants_ibfk_1` FOREIGN KEY (`id_fil`) REFERENCES `filiere` (`id`);

--
-- Contraintes pour la table `filiere`
--
ALTER TABLE `filiere`
  ADD CONSTRAINT `filiere_ibfk_1` FOREIGN KEY (`semestre_id`) REFERENCES `semestre` (`id`);

--
-- Contraintes pour la table `formation`
--
ALTER TABLE `formation`
  ADD CONSTRAINT `formation_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `departements` (`id`);

--
-- Contraintes pour la table `matieres`
--
ALTER TABLE `matieres`
  ADD CONSTRAINT `matieres_ibfk_1` FOREIGN KEY (`id_fil`) REFERENCES `filiere` (`id`);

--
-- Contraintes pour la table `niveau`
--
ALTER TABLE `niveau`
  ADD CONSTRAINT `niveau_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formation` (`id`);

--
-- Contraintes pour la table `semestre`
--
ALTER TABLE `semestre`
  ADD CONSTRAINT `semestre_ibfk_1` FOREIGN KEY (`niveau_id`) REFERENCES `niveau` (`id`);

--
-- Contraintes pour la table `superviseurs`
--
ALTER TABLE `superviseurs`
  ADD CONSTRAINT `superviseurs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
