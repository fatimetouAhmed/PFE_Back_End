from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select
from sqlalchemy import create_engine
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,Surveillance,Filiere,Matiere,Etudiant,Salle,Surveillance,Semestre,Evaluation,Superviseur,Surveillant,User
statis_router=APIRouter()
@statis_router.get("/examun/nom")
async def examun_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Evaluation.__table__.c.id,Evaluation.__table__.c.type).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    examun = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "type": ex.type  
        }
        examun.append(noms)
    return examun
@statis_router.get("/matieres/nom")
async def examun_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Matiere.id,Matiere.libelle).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    examun = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.libelle  
        }
        examun.append(noms)
    return examun
@statis_router.get("/historique/{id}")
async def historique_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    count = session.query(Historiques).filter(Historiques.id_exam == id).count() 
    return count
@statis_router.get("/historique/matieres/{id}")
async def historique_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            filter(Matiere.id == id).count()
    return count

@statis_router.get("/etudiants/nom")
async def etudiant_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Etudiant.id,Etudiant.prenom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    examun = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "prenom": ex.prenom 
        }
        examun.append(noms)
    return examun

@statis_router.get("/filieres/nom")
async def filiere_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Filiere.id,Filiere.libelle).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    filiere = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.libelle 
        }
        filiere.append(noms)
    return filiere
@statis_router.get("/semestres/nom")
async def semestre_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Semestre.id,Semestre.libelle).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    semestre = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.libelle 
        }
        semestre.append(noms)
    return semestre

@statis_router.get("/salles/nom")
async def salle_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Salle.id,Salle.nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    salle = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "nom": ex.nom 
        }
        salle.append(noms)
    return salle

@statis_router.get("/annees/nom")
async def annee_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Annees.id, Annees.annee_debut, Annees.annee_fin).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    annee = []
    for ex in exs:
        noms = {
            "id": ex.id,
            "annee": ex.annee_debut.strftime("%Y") + " - " + ex.annee_fin.strftime("%Y")
        }
        annee.append(noms)
    return annee

@statis_router.get("/historique/etudiants/{id}")
async def historique_etudiant_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Etudiant, Filiere.id == Etudiant.id_fil).\
            filter(Etudiant.id == id).count()
    
    return count

@statis_router.get("/historique/semestres/{id}")
async def historique_semestre_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Semestre, Filiere.semestre_id == Semestre.id).\
            filter(Semestre.id == id).count()
    
    return count

@statis_router.get("/historique/filieres/{id}")
async def historique_filiere_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            filter(Filiere.id == id).count()
    
    return count

@statis_router.get("/historique/annees/{id}")
async def historique_semestre_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Semestre, Filiere.semestre_id == Semestre.id).\
            join(Niveau, Semestre.niveau_id== Niveau.id).\
            join(Formation, Niveau.formation_id==Formation.id).\
            join(Departement, Formation.dep_id==Departement.id).\
            join(Annedep, Departement.id==Annedep.id_dep).\
            join(Annees, Annedep.id_anne==Annees.id).\
            filter(Annees.id == id).count()
    return count

@statis_router.get("/historique/salles/{id}")
async def historique_salle_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    count = session.query(Historiques).\
            join(Evaluation, Historiques.id_exam == Evaluation.id).\
            join(Salle, Evaluation.id_sal == Salle.id).\
            filter(Salle.id == id).count()
    return count