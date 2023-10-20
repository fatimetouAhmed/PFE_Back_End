-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3308
-- Généré le : dim. 15 oct. 2023 à 17:41
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `db_iscae`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateurs`
--

CREATE TABLE `administrateurs` (
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `administrateurs`
--

INSERT INTO `administrateurs` (`user_id`) VALUES
(37);

-- --------------------------------------------------------

--
-- Structure de la table `annedep`
--

CREATE TABLE `annedep` (
  `id` int(11) NOT NULL,
  `id_anne` int(11) NOT NULL,
  `id_dep` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `annees_universitaires`
--

CREATE TABLE `annees_universitaires` (
  `id` int(11) NOT NULL,
  `annee_debut` datetime NOT NULL,
  `annee_fin` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `annees_universitaires`
--

INSERT INTO `annees_universitaires` (`id`, `annee_debut`, `annee_fin`) VALUES
(1, '2023-09-01 00:00:00', '2024-05-01 00:00:00');

-- --------------------------------------------------------

--
-- Structure de la table `departements`
--

CREATE TABLE `departements` (
  `id` int(11) NOT NULL,
  `nom_departement` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `departements`
--

INSERT INTO `departements` (`id`, `nom_departement`) VALUES
(1, 'informatique');

-- --------------------------------------------------------

--
-- Structure de la table `departementssuperviseurs`
--

CREATE TABLE `departementssuperviseurs` (
  `id` int(11) NOT NULL,
  `id_sup` int(11) NOT NULL,
  `id_dep` int(11) NOT NULL,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `etudiants`
--

CREATE TABLE `etudiants` (
  `id` int(11) NOT NULL,
  `matricule` varchar(255) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `photo` varchar(555) DEFAULT NULL,
  `nni` int(11) DEFAULT NULL,
  `genre` varchar(255) NOT NULL,
  `date_inscription` datetime DEFAULT NULL,
  `lieu_n` varchar(255) DEFAULT NULL,
  `date_n` datetime DEFAULT NULL,
  `nationnalite` varchar(255) DEFAULT NULL,
  `tel` int(11) DEFAULT NULL,
  `email` varchar(500) NOT NULL,
  `id_fil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `etudiants`
--

INSERT INTO `etudiants` (`id`, `matricule`, `nom`, `prenom`, `photo`, `nni`, `genre`, `date_inscription`, `lieu_n`, `date_n`, `nationnalite`, `tel`, `email`, `id_fil`) VALUES
(1, 'IE19255', 'khadije', 'med', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/etudiants/37_1696956019.378726.jpg', 2255852, 'f', '2023-10-15 12:43:50', 'nktt', '2023-10-15 12:43:50', 'mr', 25896314, 'khadije@gmail.com', 1),
(2, 'ie19255', 'beibety', 'med', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/etudiants/beybeti.jpeg', 22589631, 'f', '2023-10-15 12:43:50', 'nktt', '2023-10-15 12:43:50', 'mr', 22589631, 'beibety@gmail.com', 1);

-- --------------------------------------------------------

--
-- Structure de la table `evaluation`
--

CREATE TABLE `evaluation` (
  `id` int(11) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `date_debut` datetime DEFAULT NULL,
  `date_fin` datetime DEFAULT NULL,
  `id_sal` int(11) DEFAULT NULL,
  `id_mat` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `evaluation`
--

INSERT INTO `evaluation` (`id`, `type`, `date_debut`, `date_fin`, `id_sal`, `id_mat`) VALUES
(1, 'normale', '2023-10-15 17:06:13', '2023-11-30 15:06:14', 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `filiere`
--

CREATE TABLE `filiere` (
  `id` int(11) NOT NULL,
  `libelle` varchar(255) NOT NULL,
  `semestre_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `filiere`
--

INSERT INTO `filiere` (`id`, `libelle`, `semestre_id`) VALUES
(1, 'informatique ges', 1);

-- --------------------------------------------------------

--
-- Structure de la table `formation`
--

CREATE TABLE `formation` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `dep_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `formation`
--

INSERT INTO `formation` (`id`, `nom`, `dep_id`) VALUES
(1, 'licence', 1);

-- --------------------------------------------------------

--
-- Structure de la table `historiques`
--

CREATE TABLE `historiques` (
  `id` int(11) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id_exam` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

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
(16, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:09:01.663447, le surveillant 32 de la salle N°3', 2),
(17, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:11:00.430738, le surveillant 32 de la salle N°3', 2),
(18, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:14:43.140985, le surveillant 32 de la salle N°3', 2),
(19, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:17:43.771852, le surveillant 32 de la salle N°3', 2),
(20, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:18.378530, le surveillant 32 de la salle N°3', 2),
(21, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:40.553881, le surveillant 32 de la salle N°3', 2),
(22, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:20:46.269362, le surveillant 32 de la salle N°3', 2),
(23, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:22:40.833943, le surveillant 32 de la salle N°3', 2),
(24, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:23:15.145559, le surveillant 32 de la salle N°3', 2),
(25, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:26:31.561962, le surveillant 32 de la salle N°3', 2),
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
(85, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:55:08.235245, le surveillant 36 de la salle N°5', 4);

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

CREATE TABLE `matieres` (
  `id` int(11) NOT NULL,
  `libelle` varchar(255) DEFAULT NULL,
  `nbr_heure` int(11) DEFAULT NULL,
  `credit` int(11) DEFAULT NULL,
  `id_fil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`id`, `libelle`, `nbr_heure`, `credit`, `id_fil`) VALUES
(1, 'IA', 40, 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `niveau`
--

CREATE TABLE `niveau` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `formation_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `niveau`
--

INSERT INTO `niveau` (`id`, `nom`, `formation_id`) VALUES
(1, 'l1', 1);

-- --------------------------------------------------------

--
-- Structure de la table `notifications`
--

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `content` varchar(250) NOT NULL,
  `date` datetime NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `superviseur_id` int(11) DEFAULT NULL,
  `id_exam` int(11) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `notifications`
--

INSERT INTO `notifications` (`id`, `content`, `date`, `is_read`, `superviseur_id`, `id_exam`, `image`) VALUES
(2, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:32:33.952372, le surveillant 32 de la salle N°2', '2023-07-04 16:32:34', 1, 31, 0, 'images/medos.jpeg'),
(3, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:35:32.633656, le surveillant 32 de la salle N°2', '2023-07-04 16:35:33', 0, 31, 5, 'images/chou3ayb.jpeg'),
(4, 'Attention étudiant ali ahmed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:36:58.725182, le surveillant 32 de la salle N°2', '2023-07-04 16:36:59', 0, 31, 5, 'images/mbare.jpeg'),
(5, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:40:30.469222, le surveillant 32 de la salle N°2', '2023-07-04 16:40:30', 0, 31, 5, 'images/user.jpg'),
(6, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle1 pour passer l\'examen session dans la matière java au moment 2023-07-04 16:43:45.275643, le surveillant 32 de la salle N°2', '2023-07-04 16:43:45', 0, 31, 5, 'images/jorjina.jpg'),
(7, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:03:19.159628, le surveillant 32 de la salle N°3', '2023-08-02 21:03:19', 0, 31, 5, 'images/elone1.jpg'),
(8, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:09:01.663447, le surveillant 32 de la salle N°3', '2023-08-02 21:09:02', 1, 31, 0, ''),
(9, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:11:00.430738, le surveillant 32 de la salle N°3', '2023-08-02 21:11:00', 1, 31, 0, ''),
(10, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:14:43.140985, le surveillant 32 de la salle N°3', '2023-08-02 21:14:43', 1, 31, 0, ''),
(11, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:17:43.771852, le surveillant 32 de la salle N°3', '2023-08-02 21:17:44', 1, 31, 0, ''),
(12, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:18.378530, le surveillant 32 de la salle N°3', '2023-08-02 21:18:18', 1, 31, 0, ''),
(13, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:18:40.553881, le surveillant 32 de la salle N°3', '2023-08-02 21:18:41', 1, 31, 0, ''),
(14, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:20:46.269362, le surveillant 32 de la salle N°3', '2023-08-02 21:20:46', 1, 31, 0, ''),
(15, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:22:40.833943, le surveillant 32 de la salle N°3', '2023-08-02 21:22:41', 1, 31, 0, ''),
(16, 'Attention étudiant sidi mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:23:15.145559, le surveillant 32 de la salle N°3', '2023-08-02 21:23:15', 1, 31, 0, ''),
(17, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:26:31.561962, le surveillant 32 de la salle N°3', '2023-08-02 21:26:32', 1, 31, 0, ''),
(18, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-02 21:27:49.736628, le surveillant 32 de la salle N°3', '2023-08-02 21:27:50', 1, 31, 0, ''),
(19, 'Attention étudiant Emin ahmed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-03 01:07:10.856004, le surveillant 32 de la salle N°3', '2023-08-03 01:07:11', 1, 31, 0, ''),
(20, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-08-03 01:07:49.620570, le surveillant 32 de la salle N°3', '2023-08-03 01:07:50', 1, 31, 0, ''),
(21, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:39:09.928598, le surveillant 37 de la salle N°5', '2023-08-22 12:39:09', 0, 31, 0, ''),
(22, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:39:39.593400, le surveillant 37 de la salle N°5', '2023-08-22 12:39:39', 0, 31, 0, ''),
(23, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-22 12:40:39.473049, le surveillant 37 de la salle N°5', '2023-08-22 12:40:39', 0, 31, 0, ''),
(24, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-30 17:11:05.343736, le surveillant 37 de la salle N°5', '2023-08-30 17:11:05', 0, 31, 4, ''),
(25, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 17:42:54.556470, le surveillant 37 de la salle N°5', '2023-08-31 17:42:54', 0, 31, 4, ''),
(26, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 20:41:50.909441, le surveillant 37 de la salle N°5', '2023-08-31 20:41:50', 0, 31, 4, ''),
(27, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-08-31 20:43:19.468344, le surveillant 37 de la salle N°5', '2023-08-31 20:43:19', 0, 31, 4, ''),
(28, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:11:14.459752, le surveillant 37 de la salle N°5', '2023-09-01 15:11:14', 0, 31, 4, ''),
(29, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:18:19.012035, le surveillant 37 de la salle N°5', '2023-09-01 15:18:19', 0, 31, 4, ''),
(30, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:29:20.341565, le surveillant 37 de la salle N°5', '2023-09-01 15:29:20', 0, 31, 4, ''),
(31, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-09-01 15:29:24.443679, le surveillant 37 de la salle N°5', '2023-09-01 15:29:24', 0, 31, 4, ''),
(32, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:45:07.840257, le surveillant 36 de la salle N°3', '2023-09-25 17:45:07', 0, 31, 2, ''),
(33, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:46:50.259064, le surveillant 36 de la salle N°3', '2023-09-25 17:46:50', 0, 31, 2, ''),
(34, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:48:03.577913, le surveillant 36 de la salle N°3', '2023-09-25 17:48:03', 0, 31, 2, ''),
(35, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:48:57.768148, le surveillant 36 de la salle N°3', '2023-09-25 17:48:57', 0, 31, 2, ''),
(36, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-25 17:50:51.535906, le surveillant 36 de la salle N°3', '2023-09-25 17:50:51', 0, 31, 2, ''),
(37, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:31:05.135475, le surveillant 36 de la salle N°3', '2023-09-26 09:31:05', 0, 31, 2, ''),
(38, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:45:32.857887, le surveillant 36 de la salle N°3', '2023-09-26 09:45:32', 0, 31, 2, ''),
(39, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:49:39.524261, le surveillant 36 de la salle N°3', '2023-09-26 09:49:39', 0, 31, 2, ''),
(40, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 09:50:11.259844, le surveillant 36 de la salle N°3', '2023-09-26 09:50:11', 0, 31, 2, ''),
(41, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:16:52.079849, le surveillant 36 de la salle N°3', '2023-09-26 10:16:52', 0, 31, 2, ''),
(42, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:32:33.554230, le surveillant 36 de la salle N°3', '2023-09-26 10:32:33', 0, 31, 2, ''),
(43, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:33:09.759720, le surveillant 36 de la salle N°3', '2023-09-26 10:33:09', 0, 31, 2, ''),
(44, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:35:24.648864, le surveillant 36 de la salle N°3', '2023-09-26 10:35:24', 0, 31, 2, ''),
(45, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-26 10:36:47.791711, le surveillant 36 de la salle N°3', '2023-09-26 10:36:47', 0, 31, 2, ''),
(46, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-09-30 11:57:01.829005, le surveillant 36 de la salle N°3', '2023-09-30 11:57:01', 0, 31, 2, ''),
(47, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:37:20.707924, le surveillant 36 de la salle N°3', '2023-10-01 19:37:20', 0, 31, 2, ''),
(48, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:38:18.970402, le surveillant 36 de la salle N°3', '2023-10-01 19:38:18', 0, 31, 2, ''),
(49, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:39:35.113329, le surveillant 36 de la salle N°3', '2023-10-01 19:39:35', 0, 31, 2, ''),
(50, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-01 19:39:57.466514, le surveillant 36 de la salle N°3', '2023-10-01 19:39:57', 0, 31, 2, ''),
(51, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 14:03:56.022183, le surveillant 36 de la salle N°3', '2023-10-02 14:03:56', 0, 31, 2, ''),
(52, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 15:36:04.975987, le surveillant 36 de la salle N°3', '2023-10-02 15:36:04', 0, 31, 2, ''),
(53, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-02 15:42:56.442516, le surveillant 36 de la salle N°3', '2023-10-02 15:42:56', 0, 31, 2, ''),
(54, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 11:23:16.658515, le surveillant 36 de la salle N°3', '2023-10-03 11:23:16', 0, 31, 2, ''),
(55, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 11:38:04.834614, le surveillant 36 de la salle N°3', '2023-10-03 11:38:04', 0, 31, 2, ''),
(56, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:37:32.799379, le surveillant 36 de la salle N°3', '2023-10-03 15:37:32', 0, 31, 2, ''),
(57, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:39:04.643223, le surveillant 36 de la salle N°3', '2023-10-03 15:39:04', 0, 31, 2, ''),
(58, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 15:59:57.622982, le surveillant 36 de la salle N°3', '2023-10-03 15:59:57', 0, 31, 2, ''),
(59, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 16:16:09.190800, le surveillant 36 de la salle N°3', '2023-10-03 16:16:09', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696349769.188806.jpg'),
(60, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 16:40:52.124425, le surveillant 36 de la salle N°3', '2023-10-03 16:40:52', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696351252.122656.jpg'),
(61, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 17:05:45.911814, le surveillant 36 de la salle N°3', '2023-10-03 17:05:45', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696352745.910817.jpg'),
(62, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 17:21:43.712506, le surveillant 36 de la salle N°3', '2023-10-03 17:21:43', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696353703.711476.jpg'),
(63, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:10:36.538122, le surveillant 36 de la salle N°3', '2023-10-03 19:10:36', 0, 31, 2, '46_1693646873.786814.jpg'),
(64, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:43:26.776415, le surveillant 36 de la salle N°3', '2023-10-03 19:43:26', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696362206.773428.jpg'),
(65, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-03 19:47:02.026651, le surveillant 36 de la salle N°3', '2023-10-03 19:47:02', 0, 31, 2, '46_1693646873.786814.jpg'),
(66, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 09:53:25.828878, le surveillant 36 de la salle N°3', '2023-10-04 09:53:25', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696413205.827873.jpg'),
(67, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 09:56:10.294605, le surveillant 36 de la salle N°3', '2023-10-04 09:56:10', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696413370.293603.jpg'),
(68, 'Attention étudiant Mbare mouhamed n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 10:28:07.586710, le surveillant 36 de la salle N°3', '2023-10-04 10:28:07', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696415287.585715.jpg'),
(69, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 10:28:26.107016, le surveillant 36 de la salle N°3', '2023-10-04 10:28:26', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696415306.106019.jpg'),
(70, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 12:04:57.327299, le surveillant 36 de la salle N°3', '2023-10-04 12:04:57', 0, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696421097.326303.jpg'),
(71, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle2 pour passer l\'examen session dans la matière jee au moment 2023-10-04 12:40:29.675705, le surveillant 36 de la salle N°3', '2023-10-04 12:40:29', 1, 31, 2, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696423229.673711.jpg'),
(72, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:30:07.126878, le surveillant 36 de la salle N°5', '2023-10-06 10:30:07', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696588207.12488.jpg'),
(73, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:31:27.130483, le surveillant 36 de la salle N°5', '2023-10-06 10:31:27', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696588287.128485.jpg'),
(74, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:41:50.483829, le surveillant 36 de la salle N°5', '2023-10-06 10:41:50', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696588910.482832.jpg'),
(75, 'Attention étudiant seytoba seytobe n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:43:34.431034, le surveillant 36 de la salle N°5', '2023-10-06 10:43:34', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696589014.430034.jpg'),
(76, 'Attention étudiant medelhanevy khadije n\'a pas d\'examen en ce moment et tente d\'entrer dans la salle salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:53:32.760995, le surveillant 36 de la salle N°5', '2023-10-06 10:53:32', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696589612.760995.jpg'),
(77, 'Attention, quelqu\'un n\'est pas reconnu par l\'application, et cette personne essaie d\'entrer dans salle4 pour passer l\'examen normal dans la matière java au moment 2023-10-06 10:55:08.235245, le surveillant 36 de la salle N°5', '2023-10-06 10:55:08', 0, 31, 4, 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications/1696589708.234245.jpg');

-- --------------------------------------------------------

--
-- Structure de la table `pv`
--

CREATE TABLE `pv` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `nni` varchar(20) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `date_pv` datetime DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `tel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `salles`
--

CREATE TABLE `salles` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `salles`
--

INSERT INTO `salles` (`id`, `nom`) VALUES
(1, 'salle1');

-- --------------------------------------------------------

--
-- Structure de la table `semestre`
--

CREATE TABLE `semestre` (
  `id` int(11) NOT NULL,
  `libelle` varchar(255) NOT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL,
  `niveau_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `semestre`
--

INSERT INTO `semestre` (`id`, `libelle`, `date_debut`, `date_fin`, `niveau_id`) VALUES
(1, 'S1', '2023-10-01', '2023-12-30', 1);

-- --------------------------------------------------------

--
-- Structure de la table `superviseurs`
--

CREATE TABLE `superviseurs` (
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `superviseurs`
--

INSERT INTO `superviseurs` (`user_id`) VALUES
(31),
(55);

-- --------------------------------------------------------

--
-- Structure de la table `surveillances`
--

CREATE TABLE `surveillances` (
  `id` int(11) NOT NULL,
  `id_sal` int(11) DEFAULT NULL,
  `id_surv` int(11) DEFAULT NULL,
  `date_debut` datetime DEFAULT NULL,
  `date_fin` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `surveillances`
--

INSERT INTO `surveillances` (`id`, `id_sal`, `id_surv`, `date_debut`, `date_fin`) VALUES
(1, 1, 36, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `surveillants`
--

CREATE TABLE `surveillants` (
  `user_id` int(11) NOT NULL,
  `superviseur_id` int(11) DEFAULT NULL,
  `typecompte` varchar(255) NOT NULL DEFAULT 'principale'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `surveillants`
--

INSERT INTO `surveillants` (`user_id`, `superviseur_id`, `typecompte`) VALUES
(36, 31, 'principale'),
(60, 31, 'principale');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pswd` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `photo` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom`, `prenom`, `email`, `pswd`, `role`, `photo`) VALUES
(31, 'iman', 'Mouhamed', 'amina@gmail.com', '$2b$12$cSqXtKMC642k.1VkHAFjW.q/VYMJq.zSBzbDdOM4Sm.NNAfc.oCMS', 'superviseur', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/1696939221.056708.jpg'),
(36, 'user', 'user', 'user@gmail.com', '$2b$12$w8W1lM0oz98sHQvKGgm9FeC1wcmsX3q6NDjYktZeHycYnyVobxo9u', 'surveillant', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/user.jpg'),
(37, 'admin', 'admin', 'admin@gmail.com', '$2b$12$wSM3of2sH6TfOhBvr8mTiutg98xXjHy98aHM7w/gl5Y5XsJhFwnb6', 'admin', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/admin.jpg'),
(55, 'oussama', 'issa', 'issa@gmail.com', '$2b$12$lKCYFDQvJGIZ2l.b52aQuuBn5ksH3W4m7JGIB.SrRZbBQWYLHqRXO', 'superviseur', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/1696508698.565203.jpg'),
(59, 'aziza', 'aziz', 'aziza@gmail.com', '$2b$12$mpo23SVBF03mJ9Cf7K.0L.hSBYFdAn.VDcwKdalVzgVWrvlIj7tGO', 'surveillant ', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/1697195966.407218.jpg'),
(60, 'surv', 'surv', 'surv@gmail.com', '$2b$12$K6lxP8BxLMsM3HipTJGHieS7H.reU7tgIXKsdl6kRiOewenM14h76', 'surveillant', 'C:/Users/hp/Desktop/PFE/PFE_FRONT/images/users/1697200987.362018.jpg');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD PRIMARY KEY (`user_id`);

--
-- Index pour la table `annedep`
--
ALTER TABLE `annedep`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_anne` (`id_anne`),
  ADD KEY `id_dep` (`id_dep`);

--
-- Index pour la table `annees_universitaires`
--
ALTER TABLE `annees_universitaires`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `departements`
--
ALTER TABLE `departements`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `departementssuperviseurs`
--
ALTER TABLE `departementssuperviseurs`
  ADD PRIMARY KEY (`id`,`id_sup`,`id_dep`,`date_debut`,`date_fin`) USING BTREE,
  ADD KEY `fketu` (`id_sup`),
  ADD KEY `FKMAT` (`id_dep`);

--
-- Index pour la table `etudiants`
--
ALTER TABLE `etudiants`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_fil` (`id_fil`);

--
-- Index pour la table `evaluation`
--
ALTER TABLE `evaluation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_sal` (`id_sal`),
  ADD KEY `id_mat` (`id_mat`);

--
-- Index pour la table `filiere`
--
ALTER TABLE `filiere`
  ADD PRIMARY KEY (`id`),
  ADD KEY `semestre_id` (`semestre_id`);

--
-- Index pour la table `formation`
--
ALTER TABLE `formation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dep_id` (`dep_id`);

--
-- Index pour la table `historiques`
--
ALTER TABLE `historiques`
  ADD PRIMARY KEY (`id`),
  ADD KEY `historique_ibfk_1` (`id_exam`);

--
-- Index pour la table `matieres`
--
ALTER TABLE `matieres`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_fil` (`id_fil`);

--
-- Index pour la table `niveau`
--
ALTER TABLE `niveau`
  ADD PRIMARY KEY (`id`),
  ADD KEY `formation_id` (`formation_id`);

--
-- Index pour la table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `superviseur_id` (`superviseur_id`),
  ADD KEY `id_exam` (`id_exam`);

--
-- Index pour la table `pv`
--
ALTER TABLE `pv`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `salles`
--
ALTER TABLE `salles`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `semestre`
--
ALTER TABLE `semestre`
  ADD PRIMARY KEY (`id`),
  ADD KEY `niveau_id` (`niveau_id`);

--
-- Index pour la table `superviseurs`
--
ALTER TABLE `superviseurs`
  ADD PRIMARY KEY (`user_id`);

--
-- Index pour la table `surveillances`
--
ALTER TABLE `surveillances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_sal` (`id_sal`),
  ADD KEY `id_surv` (`id_surv`);

--
-- Index pour la table `surveillants`
--
ALTER TABLE `surveillants`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `superviseur_id` (`superviseur_id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UC_users_email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `annedep`
--
ALTER TABLE `annedep`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `annees_universitaires`
--
ALTER TABLE `annees_universitaires`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `departements`
--
ALTER TABLE `departements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `departementssuperviseurs`
--
ALTER TABLE `departementssuperviseurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `etudiants`
--
ALTER TABLE `etudiants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `evaluation`
--
ALTER TABLE `evaluation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `filiere`
--
ALTER TABLE `filiere`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `formation`
--
ALTER TABLE `formation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `historiques`
--
ALTER TABLE `historiques`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT pour la table `matieres`
--
ALTER TABLE `matieres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `niveau`
--
ALTER TABLE `niveau`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT pour la table `salles`
--
ALTER TABLE `salles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `semestre`
--
ALTER TABLE `semestre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `surveillances`
--
ALTER TABLE `surveillances`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

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
-- Contraintes pour la table `evaluation`
--
ALTER TABLE `evaluation`
  ADD CONSTRAINT `evaluation_ibfk_1` FOREIGN KEY (`id_sal`) REFERENCES `salles` (`id`),
  ADD CONSTRAINT `evaluation_ibfk_2` FOREIGN KEY (`id_mat`) REFERENCES `matieres` (`id`);

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

--
-- Contraintes pour la table `surveillances`
--
ALTER TABLE `surveillances`
  ADD CONSTRAINT `surveillances_ibfk_1` FOREIGN KEY (`id_sal`) REFERENCES `salles` (`id`),
  ADD CONSTRAINT `surveillances_ibfk_2` FOREIGN KEY (`id_surv`) REFERENCES `surveillants` (`user_id`);

--
-- Contraintes pour la table `surveillants`
--
ALTER TABLE `surveillants`
  ADD CONSTRAINT `surveillants_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `surveillants_ibfk_2` FOREIGN KEY (`superviseur_id`) REFERENCES `superviseurs` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
