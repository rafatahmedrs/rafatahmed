DROP TABLE heg_participe;

DROP TABLE heg_soiree;
DROP TABLE heg_personne;
DROP TABLE heg_entreprise;

CREATE TABLE heg_entreprise (
   ent_no     NUMBER(5)    CONSTRAINT pk_heg_entreprise PRIMARY KEY,
   ent_nom    VARCHAR2(20) CONSTRAINT nn_ent_nom NOT NULL CONSTRAINT uk_ent_nom UNIQUE,
   ent_mail   VARCHAR2(20),
   ent_ville  VARCHAR2(20)
);

CREATE TABLE heg_personne (
   per_no     NUMBER(5)    CONSTRAINT pk_heg_personne PRIMARY KEY,
   per_nom    VARCHAR2(20) CONSTRAINT nn_per_nom NOT NULL,
   per_prenom VARCHAR2(20),
   per_sexe   VARCHAR2(1)  CONSTRAINT ch_per_sexe CHECK(per_sexe IN ('M', 'F')),
   per_mail   VARCHAR2(20),
   per_ent_no NUMBER(5)    CONSTRAINT fk_heg_personne_entreprise REFERENCES heg_entreprise(ent_no),
   per_per_no NUMBER(5)    CONSTRAINT fk_heg_personne_conjoint REFERENCES heg_personne(per_no)
);

CREATE TABLE heg_soiree (
   soi_no     NUMBER(5)    CONSTRAINT pk_heg_soiree PRIMARY KEY,
   soi_nom    VARCHAR2(25) CONSTRAINT nn_soi_nom NOT NULL,
   soi_date   DATE,
   soi_inscr  DATE,
   soi_lieu   VARCHAR2(25),
   soi_prix   NUMBER(5,2)  CONSTRAINT ch_soi_prix CHECK(soi_prix >= 0),
   CONSTRAINT uk_soi_nom_date UNIQUE(soi_nom, soi_date),
   CONSTRAINT ch_soi_date CHECK(soi_inscr <= soi_date)
);

CREATE TABLE heg_participe (
   par_per_no NUMBER(5) CONSTRAINT fk_heg_participe_personne REFERENCES heg_personne(per_no),
   par_soi_no NUMBER(5) CONSTRAINT fk_heg_participe_soiree   REFERENCES heg_soiree(soi_no),
   CONSTRAINT pk_heg_participe PRIMARY KEY(par_per_no, par_soi_no)
);

---#TP04



INSERT INTO heg_personne  VALUES (1,'Yves','REMORD','M',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (2,'Hillary','VANBUS','F',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (3,'Otto','CARRE','F',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (4,'Aude','VAISSELLE','M',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (5,'Alex','TERIEUR','M',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (6,'Paul','HOCHON', 'M',NULL,NULL,NULL);
INSERT INTO heg_personne  VALUES (7,'Elsa','DORSA','F',NULL,NULL,NULL);

COMMIT;

--------
INSERT INTO heg_entreprise VALUES (1,'Sun',NULL,NULL);
INSERT INTO heg_entreprise VALUES (2,'IBM',NULL,NULL);
INSERT INTO heg_entreprise VALUES (3,'Sans emploi',NULL,NULL);
INSERT INTO heg_entreprise VALUES (4,'Dell',NULL,NULL);
INSERT INTO heg_entreprise VALUES (5,'IBM',NULL,NULL);
INSERT INTO heg_entreprise VALUES (6,'Dell',NULL,NULL);
INSERT INTO heg_entreprise VALUES (7,'Sun', NULL, NULL);


COMMIT;
------

INSERT INTO heg_entreprise VALUES (1,'Sun',sun@gmail.ch,NULL);
INSERT INTO heg_entreprise VALUES (2,'IBM',ibm@gmail.ch,NULL);
INSERT INTO heg_entreprise VALUES (3,'Sans emploie',NULL,NULL);
INSERT INTO heg_entreprise VALUES (4,'Sun',dell@gmail.ch,NULL);
INSERT INTO heg_entreprise VALUES (5,'Sun',sun@gmail.ch,NULL);
INSERT INTO heg_entreprise VALUES (6,'Sun',dell@gmail.ch,NULL);
INSERT INTO heg_entreprise VALUES (7,'Sun',sun@gmail.ch,NULL);


-------------------------------------------Corection
-------------1) insertion des numéro et nom des entreprise

INSERT INTO heg_entreprise VALUES (1,'Acer','acer@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (2,'Dell','dell@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (3,'Sun','sun@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (4,'Oracle','oracle@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (5,'IBM','ibm@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (6,'IBM','ibm@gmail.com',NULL);
INSERT INTO heg_entreprise VALUES (7,'APPEL','appel@gmail.com',NULL);

----------1) Ou deuxième possiblité" lorsque c'est un chiffre on doit pas mettre des appostrofs
INSERT INTO heg_entreprise (ent_no, ent_mail, et_nom)
       VALUES (8,'toto@gmail.com','toto');


------------2) insertion des personnes numéro, nom, prénom, sex, couple, lieu de travail

INSERT INTO heg_personne VALUES   (1,'REMORD'  ,'Yves','M',NULL,3,NULL);
INSERT INTO heg_personne VALUES   (2,'VANBUS'  ,'Hillary','F',NULL,5,NULL);
INSERT INTO heg_personne VALUES   (3,'CARRE'   ,'otto','M',NULL,NULL,NULL);
INSERT INTO heg_personne VALUES   (4,'VALISSELLE'  ,'AUDE','F',NULL,2,NULL);
INSERT INTO heg_personne VALUES   (5,'TERIEUR'  ,'Alex','M',null,3,NULL);
INSERT INTO heg_personne VALUES   (6,'HOCHON'  ,'Paul','M',null,2,NULL);
INSERT INTO heg_personne VALUES   (7,'REMORD'  ,'Elsa','F',NULL,3,NULL);

--------------------------3) insertion des dates des soirée

INSERT INTO heg_soiree VALUES (1,'Soirée IGS0', to_date ('28.09.2019','dd.mm.yyy'),to_date('26.09.2019','dd.mm.yyy','Battelle');
INSERT INTO heg_soiree VALUES (2,'Soirée IGS0', to_date ('26.10.2019','dd.mm.yyy'),to_date('26.09.2019','dd.mm.yyy','Battelle');
INSERT INTO heg_soiree VALUES (3,'Soirée Profs', to_date ('26.10.2019','dd.mm.yyy'),to_date('26.09.2019','dd.mm.yyy','Carouge');


-------------------Couple John et Aude

INSERT INTO heg_personne VALUES (8,'Doeuf','John','M',NULL,3,NULL);
INSERT INTO heg_personne VALUES (9,'ITION','Aude','F',NULL,3,8);

--------------------Mettre en couple numéro 8

UPDATE heg_personne
       SET per_per_no = 9
WHERE per_nom = 8;         -----Where per_nom = 'Doeuf



------------Alex a pariticpé aux trois soire
INSERT INTO heg_participe VALUES (5,1);
INSERT INTO heg_participe VALUES (5,2);
INSERT INTO heg_participe VALUES (5,3);

--------------Paul
INSERT INTO heg_participe VALUES (6,1);


-----------------John Doeuf et Aude Ition soirées profs

INSERT INTO heg_participe VALUES (8,3);
INSERT INTO heg_participe VALUES (9,3);

-----Alex travaille chez Dell

UPDATE heg_personne
       SET per_per_no = 2
WHERE per_no = 5;

--------Elsa s'est mariée avec Yves

UPDATE heg_personne
       SET per_nom = 'REMORD-DORSA',
           per_per_no = 1
WHERE per_no = 7;


UPDATE heg_personne
       SET per_per_no = 7
WHERE per_no = 1;

-------------3.- de plus pour les soiréé Battelle
UPDATE heg_soiréé
       SET soi_prix = soi_prix + 3 
WHERE soi_lieu = 'Battelle';

------------John Doeuf n'a pas participé à la Soiréé Profs mais Soirée IFS du 26.10.2019

UPDATE heg_participe
      SET par _soi_no = 2
WHERE per_per_no = 8 --- John Doeuf
      AND par_soi_no = 3, ------ Soiréé Profs
                                                           ------------ Si John a participé à deux soiréés
                                                            ------------ Si John a participé à une soiréé, on pas besoin de mettre le AND Plus on est préci, c'est mieux
------------------Test des contrantes d'intégrité
----pk
INSERT INTO heg_personne VALUES   (1,'REMORD'  ,'Yves','M',NULL,3,NULL);   
----FK
INSERT INTO heg_participe VALUES  (6,4),
-----NN
INSERT INTO heg_entreprise VALUES (10,NULL,NULL,NULL);
-----UK
INSERT INTO heg_soiree VALUES (4,'Soirée IGS', to_date('28.09.2019','dd.mm.yyy'), to_date ('26.09.2019','dd.mm.yyy'),,'Battelle')

-----Check
INSERT INTO heg_personne VALUES (10,'TOTO','Tata','R',NULL,3 , NULL );                           
                                                            
                                                            
                                                            
                                                           


