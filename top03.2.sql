OP TABLE exe_employe;
OP TABLE exe_dept;

---Création des tables

CREATE TABLE exe_dept (
dep_no       NUMBER (5) CONSTRAINT pk_exe_dept PRIMARY KEY,
dep_nom      VARCHAR2(28)
);

CREATE TABLE exe_employe (
   emp_no    NUMBER (5) CONSTRAINT PK_exe_employe PRIMARY KEY,
   emp_prenom       VARCHAR2 (20) CONSTRAINT emp_prenom NOT NULL,
   emp_nom          VARCHAR2 (20) CONSTRAINT nn_emp_nom NOT NULL,
   emp_email        VARCHAR (20) CONSTRAINT uk_emp_email UNIQUE,
   emp_embuche      DATE CONSTRAINT nn_emp_embuche NOT NULL,
   emp_salaire      NUMBER (8,2)CONSTRAINT ch_emp_salaire CHECK (emp_salaire > 0),
   emp_emp_no       NUMBER (5) CONSTRAINT fk_exe_employe_chef REFERENCES exe_employe (emp_no),
   emp_dep_no      NUMBER (5) CONSTRAINT fk_exe_employe_dept REFERENCES exe_dept (emp_no),
   CONSTRAINT uk_emp_nom_prenom UNIQUE (emp_nom, emp_prenom)
);
ALTER TABLE exe_dept ADD (dep_lieu VARCHAR (20));
ALTER TABLE exe_dept ADD (CONSTRAINT uk_dep_nom UNIQUE(dep_nom);
ALTER TABLE exe_employe ADD (
      CONSTRAINT ch_emp_salaire CHECK(emp_salaire >=0)
      CONSTRAINT uk_emp_nom CHECK (emp_nom,emp_prenom)
