from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
import re
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select
from sqlalchemy import create_engine
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User,Notifications
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
    count = session.query(PV).filter(PV.id_eval == id).count() 
    return count
@statis_router.get("/historique/matieres/{id}")
async def historique_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            filter(Matiere.id == id).count()
    return count

@statis_router.get("/etudiants/genre")
async def etudiant_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Etudiant.id,Etudiant.genre).group_by(Etudiant.genre).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    etudiant = []
    for ex in exs:
        noms = {
            # "id":ex.id,
            "genre": ex.genre
        }
        etudiant.append(noms)
    return etudiant

@statis_router.get("/filieres/nom")
async def filiere_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Filiere.id,Filiere.abreviation).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    filiere = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "abreviation": ex.abreviation
        }
        filiere.append(noms)
    return filiere
@statis_router.get("/semestres/nom")
async def semestre_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Semestre.id,Semestre.libelle).group_by(Semestre.libelle).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    semestre = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.libelle 
        }
        semestre.append(noms)
    return semestre
@statis_router.get("/formations/nom")
async def semestre_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Formation.id,Formation.nom).group_by(Formation.nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    semestre = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.nom
        }
        semestre.append(noms)
    return semestre
@statis_router.get("/niveaus/nom")
async def semestre_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Niveau.id,Niveau.nom).group_by(Niveau.nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    semestre = []
    for ex in exs:
        noms = {
            "id":ex.id,
            "libelle": ex.nom
        }
        semestre.append(noms)
    return semestre
@statis_router.get("/salles/nom")
async def salle_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    salles = session.query(Salle.id, Salle.nom).all()

    # Parcourir les salles et extraire les chiffres du nom
    salles_formattees = []
    for salle in salles:
        match = re.search(r'\d+', salle.nom)
        numero_salle = match.group() if match else None

        salle_formatee = {
            "id": salle.id,
            "nom": numero_salle
        }
        salles_formattees.append(salle_formatee)

    return salles_formattees

@statis_router.get("/annees/nom")
async def annee_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Annees.id,  Annees.annee_fin).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    annee = []
    for ex in exs:
        noms = {
            "id": ex.id,
              "annee": ex.annee_fin.strftime("%Y")
        }
        annee.append(noms)
    return annee
@statis_router.get("/notification/content")
async def semestre_nom():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    exs = session.query(Notifications.content).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    semestre = []
    for ex in exs:
        noms = {     
            "content": json.loads(ex.content)["matricule"]
        }
        semestre.append(noms)
    return semestre

@statis_router.get("/historique/etudiants/{genre}")
async def historique_etudiant_id(genre: str):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    count= session.query(PV).\
                join(Etudiant, PV.id_etud == Etudiant.id).\
                filter(and_(Etudiant.genre == genre,)).count()
    return count
    # exs = session.query(Notifications.content).all()

    # # Initialiser la liste 'semestre'
    # semestre = []

    # Parcourir les notifications et récupérer les matricules
   
# ...

    # ...
    # counttotal=0
    # for ex in exs:
    #     content = json.loads(ex.content)
    #     matricule = content.get("matricule")
    #     if matricule and matricule != 'Inconue':
    #         print(matricule)
    #         semestre.append({"matricule": matricule})

    #         # Ajouter une impression pour déboguer
    #         print(f"Recherche de notifications pour le matricule {matricule} et le genre {genre}")

    #         # Afficher les résultats de la requête
    #         notifications = session.query(Notifications).\
    #             join(Evaluation, Notifications.id_exam == Evaluation.id).\
    #             join(Matiere, Evaluation.id_mat == Matiere.id).\
    #             join(Filiere, Matiere.id_fil == Filiere.id).\
    #             join(Etudiant, Filiere.id == Etudiant.id_fil).\
    #             filter(and_(Etudiant.genre == genre, Etudiant.matricule == matricule)).all()
    #         count = len(notifications)
    #         if(count!=0):
    #             counttotal+=1
    #         # print(f"Nombre de notifications pour le matricule {matricule} et le genre {genre}: {count}")

    # return counttotal


@statis_router.get("/historique/semestres/{id}")
async def historique_semestre_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Semestre, Filiere.semestre_id == Semestre.id).\
            filter(Semestre.id == id).count()
    
    return count
@statis_router.get("/historique/formations/{id}")
async def historique_semestre_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Semestre, Filiere.semestre_id == Semestre.id).\
            join(Niveau, Semestre.niveau_id == Niveau.id).\
            join(Formation, Niveau.formation_id == Formation.id).\
            filter(Formation.id == id).count()
    
    return count
@statis_router.get("/historique/niveaus/{id}")
async def historique_semestre_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
            join(Matiere, Evaluation.id_mat == Matiere.id).\
            join(Filiere, Matiere.id_fil == Filiere.id).\
            join(Semestre, Filiere.semestre_id == Semestre.id).\
            join(Niveau, Semestre.niveau_id == Niveau.id).\
            filter(Niveau.id == id).count()
    
    return count
@statis_router.get("/historique/filieres/{id}")
async def historique_filiere_id(id:int):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()
    
    # Effectuer la requête en utilisant les relations définies dans vos modèles
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
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
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
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
    count = session.query(PV).\
            join(Evaluation, PV.id_eval == Evaluation.id).\
            join(Salle, Evaluation.id_sal == Salle.id).\
            filter(Salle.id == id).count()
    return count