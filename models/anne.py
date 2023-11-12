from sqlalchemy import Table,Column,String,Integer,DateTime,ForeignKey,Boolean,DATETIME,Time
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import  relationship

from auth.authConfig import PV,User 
from datetime import datetime,time

Base = declarative_base()

# Modèles de données (tables)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    pswd = Column(String(255))
    role = Column(String(255))
    photo = Column(String(250))

    surveillant = relationship("Surveillant", back_populates="user", uselist=False)
    administrateur = relationship("Administrateur", back_populates="user", uselist=False)
    superviseur = relationship("Superviseur", back_populates="user", uselist=False)



    
class DepartementSuperviseurs(Base):
    __tablename__ = 'departementssuperviseurs'
    id = Column(Integer, primary_key=True)
    id_sup = Column(Integer, ForeignKey("superviseurs.user_id"))
    id_dep = Column(Integer, ForeignKey("departements.id"))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    superviseur = relationship("Superviseur", back_populates="departement_superviseur", uselist=False)
    departement = relationship("Departement", back_populates="departement_superviseur", uselist=False)
    
class Annees(Base):
    __tablename__ = 'annees_universitaires'
    id = Column(Integer, primary_key=True)
    annee_debut  = Column(DateTime)
    annee_fin  = Column(DateTime)
    annedep = relationship("Annedep", back_populates="annee", uselist=False)



class Departement(Base):
    __tablename__ = 'departements'
    id = Column(Integer, primary_key=True)
    nom_departement  = Column(String(255))
    formation = relationship("Formation", back_populates="departement", uselist=False)
    annedep = relationship("Annedep", back_populates="departement", uselist=False)
    departement_superviseur = relationship("DepartementSuperviseurs", back_populates="departement", uselist=False)

class Annedep(Base):
    __tablename__ = 'annedep'
    id = Column(Integer, primary_key=True)
    id_anne  = Column(Integer, ForeignKey("annees_universitaires.id"))
    id_dep  = Column(Integer, ForeignKey("departements.id"))
    departement = relationship("Departement", back_populates="annedep", uselist=False)
    annee = relationship("Annees", back_populates="annedep", uselist=False)
    


class Formation(Base):
    __tablename__ = 'formation'
    id = Column(Integer, primary_key=True)
    nom  = Column(String(255))
    dep_id = Column(Integer, ForeignKey("departements.id"))
    departement = relationship("Departement", back_populates="formation", uselist=False)
    niveau = relationship("Niveau", back_populates="formation", uselist=False)

class Niveau(Base):
    __tablename__ = 'niveau'
    id = Column(Integer, primary_key=True)
    nom  = Column(String(255))
    formation_id=Column(Integer, ForeignKey("formation.id"))
    formation = relationship("Formation", back_populates="niveau", uselist=False)
    semestre = relationship("Semestre", back_populates="niveau", uselist=False)

class Semestre(Base):
    __tablename__ = 'semestre'
    id = Column(Integer, primary_key=True)
    libelle  = Column(String(255))
    niveau_id =Column(Integer, ForeignKey("niveau.id"))
    date_debut  = Column(DateTime)
    date_fin  = Column(DateTime)
    niveau = relationship("Niveau", back_populates="semestre", uselist=False)
    filiere = relationship("Filiere", back_populates="semestre", uselist=False)
   
       
class Filiere(Base):
    __tablename__ = 'filiere'
    id = Column(Integer, primary_key=True)
    libelle  = Column(String(255))
    abreviation  = Column(String(255))
    semestre_id=Column(Integer, ForeignKey("semestre.id"))
    etudiant= relationship("Etudiant", back_populates="filiere", uselist=False)
    semestre= relationship("Semestre", back_populates="filiere", uselist=False)
    matiere= relationship("Matiere", back_populates="filiere", uselist=False)


class Etudiant(Base):
    __tablename__ = 'etudiants'

    id = Column(Integer, primary_key=True)
    matricule=Column(String(250))
    nom = Column(String(250))
    prenom = Column(String(250))
    matricule = Column(String(250))
    photo = Column(String(250))
    nni = Column(Integer)
    genre = Column(String(250))
    date_inscription = Column(DateTime) 
    lieu_n = Column(String(250))
    date_n = Column(DateTime)
    nationnalite=Column(String(250))
    tel = Column(String(250))
    email = Column(String(250))
    id_fil = Column(Integer, ForeignKey("filiere.id"))
    filiere = relationship("Filiere", back_populates="etudiant", uselist=False)
    

   # matieres = relationship('Matiere', secondary=etudiermats, backref='etudiants')


class Matiere(Base):
    __tablename__ = 'matieres'

    id = Column(Integer, primary_key=True)
    libelle = Column(String(250))
    nbr_heure = Column(Integer)
    credit = Column(Integer)
    id_fil = Column(Integer, ForeignKey("filiere.id"))
    filiere = relationship("Filiere", back_populates="matiere", uselist=False)
    evaluation=relationship("Evaluation", back_populates="matiere", uselist=False)
    creneaujour = relationship("CreneauJours", back_populates="matiere", uselist=False)





class Evaluation(Base):
    __tablename__ = 'evaluation'

    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    date_debut  = Column(DateTime)
    date_fin  = Column(DateTime)
    id_sal = Column(Integer, ForeignKey("salles.id"))
    id_mat = Column(Integer, ForeignKey("matieres.id"))
    id_jour = Column(Integer, ForeignKey("jours.id"))
    salle = relationship("Salle", back_populates="evaluation", uselist=False)
    matiere=relationship("Matiere", back_populates="evaluation", uselist=False)    
    historique=relationship("Historiques", back_populates="evaluation", uselist=False)
    notification=relationship("Notifications", back_populates="evaluation", uselist=False)
    surveillancesuperviseur = relationship("SurveillanceSuperviseur", back_populates="evaluation", uselist=False)
    pv = relationship("PV", back_populates="evaluation", uselist=False) 
    jour = relationship("Jour", back_populates="evaluation", uselist=False)
class Jour(Base):
    __tablename__ = 'jours'

    id = Column(Integer, primary_key=True)
    libelle= Column(String(250))
    date  = Column(DateTime)
    evaluation = relationship("Evaluation", back_populates="jour")
    creneaujour = relationship("CreneauJours", back_populates="jour", uselist=False)
class CreneauJours(Base):
    __tablename__ = 'creneau_jour'
    id = Column(Integer, primary_key=True)
    id_jour = Column(Integer, ForeignKey("jours.id"))
    id_creneau= Column(Integer, ForeignKey("creneaux.id"))
    id_mat= Column(Integer, ForeignKey("matieres.id"))
    jour = relationship("Jour", back_populates="creneaujour", uselist=False)
    creneau = relationship("Creneau", back_populates="creneaujour", uselist=False)
    matiere = relationship("Matiere", back_populates="creneaujour", uselist=False)
class Creneau(Base):
    __tablename__ = 'creneaux'

    id = Column(Integer, primary_key=True)
    heure_debut= Column(Time)
    heure_fin  = Column(Time)  
    creneaujour = relationship("CreneauJours", back_populates="creneau", uselist=False)
class Surveillant(Base):
    __tablename__ = "surveillants"

    #id = Column(Integer, pr
    # imary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    # superviseur_id = Column(Integer, ForeignKey("superviseurs.user_id"))
    id_sal=Column(Integer, ForeignKey("salles.id"))
    typecompte=Column(String(255), nullable=False,default="principale")
    user= relationship("User", back_populates="surveillant", uselist=False)
    # superviseur = relationship("Superviseur", back_populates="surveillant", uselist=False)
    salle = relationship("Salle", back_populates="surveillant", uselist=False)
    pv = relationship("PV", back_populates="surveillant", uselist=False)
    notification=relationship("Notifications", back_populates="surveillant", uselist=False)
class PV(Base):
    __tablename__ = "pv"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    nni = Column(String(255), nullable=True)
    surveillant_id = Column(Integer, ForeignKey("surveillants.user_id"))
    photo = Column(String(255), nullable=True)
    tel = Column(Integer, nullable=True)
    type = Column(String(255), nullable=True)
    date_pv = Column(DateTime, default=datetime.now)  # Ajout du champ type
    etat = Column(String(50), nullable=True)
    id_eval = Column(Integer, ForeignKey("evaluation.id"))
    surveillant = relationship("Surveillant", back_populates="pv")
    evaluation = relationship("Evaluation", back_populates="pv")


class Salle(Base):
    __tablename__ = 'salles'
    id = Column(Integer, primary_key=True)
    nom  = Column(String(255))
    surveillant = relationship("Surveillant", back_populates="salle", uselist=False)
    evaluation=relationship("Evaluation", back_populates="salle", uselist=False)
    surveillancesuperviseur=relationship("SurveillanceSuperviseur", back_populates="salle", uselist=False)

class Superviseur(Base):
    __tablename__ = "superviseurs"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    #sureveillant_id = Column(Integer, ForeignKey("surveillants.user_id"))

    user = relationship("User", back_populates="superviseur", uselist=False)
    # surveillant = relationship("Surveillant", back_populates="superviseur", uselist=False)
    departement_superviseur = relationship("DepartementSuperviseurs", back_populates="superviseur", uselist=False)
    surveillancesuperviseur = relationship("SurveillanceSuperviseur", back_populates="superviseur", uselist=False)
class SurveillanceSuperviseur(Base):
    __tablename__ = 'surveillancesuperviseur'
    id = Column(Integer, primary_key=True)
    id_sup = Column(Integer, ForeignKey("superviseurs.user_id"))
    id_sal = Column(Integer, ForeignKey("salles.id"))
    id_eval = Column(Integer, ForeignKey("evaluation.id"))
    salle = relationship("Salle", back_populates="surveillancesuperviseur", uselist=False)
    superviseur=relationship("Superviseur", back_populates="surveillancesuperviseur", uselist=False)
    evaluation=relationship("Evaluation", back_populates="surveillancesuperviseur", uselist=False)
class Historiques(Base):
    __tablename__ = 'historiques'

    id = Column(Integer, primary_key=True)
    description = Column(String(255))
    id_exam = Column(Integer, ForeignKey('evaluation.id'))
    evaluation=relationship("Evaluation", back_populates="historique", uselist=False)
class Notifications(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    date = Column(DATETIME,default=datetime.now)
    surveillant_id = Column(Integer, ForeignKey('surveillants.user_id'))
    is_read = Column(Boolean)
    id_exam = Column(Integer, ForeignKey('evaluation.id'))
    image = Column(String(255))
    evaluation=relationship("Evaluation", back_populates="notification", uselist=False)
    surveillant=relationship("Surveillant", back_populates="notification", uselist=False)


    # examuns = relationship("Examuns", primaryjoin="Notifications.id_exam == examuns.id")
    # examuns = relationship("Examuns")
class Administrateur(Base):
    __tablename__ = "administrateurs"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="administrateur", uselist=False)
    


