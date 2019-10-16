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









