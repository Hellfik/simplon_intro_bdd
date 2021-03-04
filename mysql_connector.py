import mysql.connector

# Connexion à la base de données

my_db = mysql.connector.connect(
    host="localhost",
    user="mikaf",
    password ="root"
)


my_cursor = my_db.cursor(buffered=True)

# Creation de la database

my_cursor.execute("CREATE DATABASE IF NOT EXISTS agence_location_python CHARACTER SET 'utf8'")
my_cursor.execute("use agence_location_python")


# Création de la table commune
my_cursor.execute("CREATE TABLE IF NOT EXISTS commune (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, commune VARCHAR(60), nombre_habitants INT UNSIGNED, distance_agence DECIMAL(6,2)) ENGINE = INNODB;")
# Création de la table locataire
my_cursor.execute("CREATE TABLE IF NOT EXISTS locataire (id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(100), prenom VARCHAR(60), date_de_naissance DATE) ENGINE = INNODB;")
# Création de la table type de logement
my_cursor.execute("CREATE TABLE IF NOT EXISTS type_logement (type VARCHAR(20) NOT NULL PRIMARY KEY, charges DECIMAL(6,2))")
# Création de la table logement
my_cursor.execute("CREATE TABLE IF NOT EXISTS logement (id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT, adresse VARCHAR(200) NOT NULL, superficie DECIMAL(6,2), loyer DECIMAL(7,2), commune_id SMALLINT UNSIGNED, type_logement VARCHAR(20), PRIMARY KEY (id), FOREIGN KEY (commune_id) REFERENCES commune(id) ON DELETE SET NULL, FOREIGN KEY (type_logement) REFERENCES type_logement(type) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE = INNODB;")
# Création de la table telephone
my_cursor.execute("CREATE TABLE IF NOT EXISTS telephone (telephone VARCHAR(16) NOT NULL PRIMARY KEY, locataire_id MEDIUMINT UNSIGNED, FOREIGN KEY (locataire_id) REFERENCES locataire(id) ON DELETE CASCADE) ENGINE = INNODB;")
# Création de la table contrat de location
my_cursor.execute("CREATE TABLE IF NOT EXISTS contrat_location (id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, date_entree DATETIME, date_sortie DATETIME, locataire_id MEDIUMINT UNSIGNED, logement_id MEDIUMINT UNSIGNED, FOREIGN KEY (locataire_id) REFERENCES locataire(id) ON DELETE SET NULL, FOREIGN KEY (logement_id) REFERENCES logement(id) ON DELETE SET NULL) ENGINE = INNODB;")


"""

CRUD

"""


# Insertion de 5 tuples dans la table commune
insert_query_commune = "INSERT INTO commune VALUES (null, 'Lille', 1200000, 250.50),(null, 'Paris', 16000000, 5.00),(null, 'Rouen', 35000 , 185.20),(null, 'Valenciennes', 6500, 25.00),(null, 'Roubaix', 25000, 14.00);"
my_cursor.execute(insert_query_commune)

# Insertion de 5 tuples dans la table locataire
insert_query_locataire = "INSERT INTO locataire VALUES (null, 'Dupont', 'Jean', '1985-03-25'),(null, 'Adkitn', 'Pierre', '1983-04-16'),(null, 'Giopl', 'Max', '1979-12-25'),(null, 'Genja', 'Nicolas', '1902-09-02'),(null, 'Fay', 'Karine', '1995-11-29');"
my_cursor.execute(insert_query_locataire)

#Insertion de 5 tuples dans la table type de logement
insert_query_type = "INSERT INTO type_logement VALUES ('Appartement', 945.22),('T1', 652.22),('T2', 962.85),('Maison', 524.36),('Studio', 892.36);"
my_cursor.execute(insert_query_type)

# Insertion de 5 tuples dans la table logement
insert_query_logement = "INSERT INTO logement VALUES (null, '11 rue de la bastille', 25.30, 10000.00, 2, 'Appartement'),(null, '145 rue de la bastille', 15.30, 850.00, 1, 'Maison'),(null, '11 rue de la bastille', 30.20, 600.00, 3, 'T1'),(null, '11 rue de la bastille', 40.00, 500.00, 4, 'T2'),(null, '11 rue de la bastille', 19.00, 450.00, 5, 'Studio');"
my_cursor.execute(insert_query_logement)

# Insertion de 5 tuples dans la table telephone
insert_query_telephone = "INSERT INTO telephone VALUES ('06/00/00/00/00', 1),('07/00/00/00/00', 2),('09/00/00/00/00', 3),('03/00/00/00/00', 4),('02/00/00/00/00', 5);"
my_cursor.execute(insert_query_telephone)

# Insertion de 5 tuples dans la table contrat de location
insert_query_location = "INSERT INTO contrat_location VALUES (null, '2021-01-12 22:05:36', '2021-02-20 12:05:59', 1, 1),(null, '2021-01-18 00:10:50', '2021-02-21 12:05:59', 2, 2),(null, '2021-01-19 14:15:26', '2021-02-22 12:05:59', 3, 3),(null, '2021-01-20 00:00:28', '2021-02-23 12:05:59', 4, 4),(null, '2021-01-21 9:25:10', '2021-02-24 12:05:59', 5, 5);"
my_cursor.execute(insert_query_location)
my_db.commit()



# Modification d'un tuple dans la table logement
update_query_logement = "UPDATE logement SET adresse='50 rue de breuil', loyer=250 WHERE id=2;"
my_cursor.execute(update_query_logement)
# Modification d'un tuple dans la table telephone
update_query_telephone = "UPDATE telephone SET telephone='01/00/00/00/00' WHERE telephone='06/00/00/00/00';"
my_cursor.execute(update_query_telephone)
# Modification d'un tuple dans la table locataire
update_query_locataire = "UPDATE locataire SET nom='Fayeulle', prenom='Pataude', date_de_naissance='1883-06-01' WHERE id=1;"
my_cursor.execute(update_query_locataire)
# Modification d'un tuple dans la table commune
update_query_commune = "UPDATE commune SET commune='Marseille', nombre_habitants=1000000 WHERE commune='Roubaix';"
my_cursor.execute(update_query_commune)
# Modification d'un tuple dans la table contrat de location
update_query_contrat = "UPDATE contrat_location SET date_entree='2021-02-25 10:05:36', date_sortie=null WHERE id=5;"
my_cursor.execute(update_query_contrat)
# Modification d'un tuple dans la table type de logement
update_query_type = "UPDATE type_logement SET type='T3', charges=500.00 WHERE type='studio';"
my_cursor.execute(update_query_type)
my_db.commit()


# Suppression d'un tuple dans la table logement
delete_query_type = "DELETE FROM type_logement WHERE type='Appartement';"
my_cursor.execute(delete_query_type)
my_db.commit()





