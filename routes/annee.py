from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy import create_engine
from models.anne import Annees,Departement,Formation,Niveau,Annedep,Filiere,Matiere,Etudiant,Salle,Surveillance,Semestre
annee_router=APIRouter()
@annee_router.get("/")
async def read_data():
    query = Annees.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"id": row.id,
                  "annee_debut": row.annee_debut,
                  "annee_fin": row.annee_fin}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results

@annee_router.get("/annee_universitaire")
async def read_data():
    query = Annees.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        # Assurez-vous que row.annee_debut et row.annee_fin sont des objets datetime
        annee_debut = row.annee_debut if isinstance(row.annee_debut, datetime) else datetime.strptime(row.annee_debut, "%Y-%m-%dT%H:%M:%S")
        annee_fin = row.annee_fin if isinstance(row.annee_fin, datetime) else datetime.strptime(row.annee_fin, "%Y-%m-%dT%H:%M:%S")
        
        result = {
            "annee_debut": datetime.strftime(annee_debut, "%Y"),  # Convertit la date en année
            "annee_fin": datetime.strftime(annee_fin, "%Y")  # Convertit la date en année
        }
        results.append(result)
    
    return results
@annee_router.get("/annee_universitaire_by_id/{annee_debut}/{annee_fin}")
async def read_data(annee_debut:str, annee_fin:str):
    id=0
    query = Annees.__table__.select()
    result_proxy = con.execute(query)   
    for row in result_proxy:
        # Assurez-vous que row.annee_debut et row.annee_fin sont des objets datetime
        annee_debut1 = row.annee_debut if isinstance(row.annee_debut, datetime) else datetime.strptime(row.annee_debut, "%Y-%m-%dT%H:%M:%S")
        annee_fin1 = row.annee_fin if isinstance(row.annee_fin, datetime) else datetime.strptime(row.annee_fin, "%Y-%m-%dT%H:%M:%S")
        dateannee_debut=datetime.strftime(annee_debut1, "%Y")
        dateannee_fin=datetime.strftime(annee_fin1, "%Y")
        if(dateannee_debut==annee_debut and dateannee_fin ==annee_fin):
            id=row.id
            return id
    
    return id



@annee_router.get("/departements/{id}")
async def read_data(id: int):
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les départements pour une année donnée
    result_proxy = session.query(Departement.nom_departement) \
        .join(Annedep, Annedep.id_dep == Departement.id) \
        .join(Annees, Annees.id == Annedep.id_anne) \
        .filter(Annees.id == id)

    results = []
    for row in result_proxy:
        result = row.nom_departement  # Correction: Removed curly braces {}
        results.append(result)
    
    return results
@annee_router.get("/departements/nom")
def get_departement_id(nom_departement):
    Session = sessionmaker(bind=con)
    session = Session()()

    # Requête pour récupérer l'ID du département en fonction de son nom
    departement = session.query(Departement).filter(Departement.nom_departement == nom_departement).first()

    if departement is not None:
        return departement.id
    else:
        return None


@annee_router.get("/formations/{nom}")
async def read_data_by_id(nom:str,):
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les étudiants avec leurs matières
    result_proxy = session.query(Formation.nom)\
               .join(Departement, Departement.id == Formation.dep_id)\
               .filter(Departement.nom_departement==nom)
    results = []
    for row in result_proxy:
        result = row.nom  # Correction: Removed curly braces {}
        results.append(result)
    
    return results

@annee_router.get("/niveaus/{nom}")
async def read_data_by_id(nom:str,):
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les étudiants avec leurs matières
    result_proxy = session.query(Niveau.nom)\
               .join(Formation, Formation.id == Niveau.formation_id)\
               .filter(Formation.nom==nom)
    results = []
    for row in result_proxy:
        result = row.nom  # Correction: Removed curly braces {}
        results.append(result)
    
    return results
@annee_router.get("/informations")
def get_data_for_level():
    Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
    session = Session()

    level_name = 'L1'

    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()

        if level:
            data = session.query(Semestre, Filiere, Matiere, Etudiant, Salle). \
                join(Filiere, Filiere.semestre_id == Semestre.id). \
                join(Matiere, Matiere.id_fil == Filiere.id). \
                join(Etudiant, Etudiant.id_fil == Filiere.id). \
                join(Salle, Salle.id == Matiere.id_fil). \
                filter(Semestre.niveau_id == level.id).all()

            # Convert the data to a JSON-serializable format
            json_data = []
            for semestre, filiere, matiere, etudiant, salle in data:
                json_data.append({
                    "Semestre": semestre.__dict__,
                    "Filiere": filiere.__dict__,
                    "Matiere": matiere.__dict__,
                    "Etudiant": etudiant.__dict__,
                    "Salle": salle.__dict__
                })

            return json_data

    finally:
        session.close()
        
@annee_router.get("/etudiants/{level_name}")
def get_data_etudiants_for_level(level_name:str):
    try:
        Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
        session = Session()
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()

        if level:
            data = session.query(Etudiant). \
                join(Filiere, Filiere.id == Etudiant.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Matiere, Matiere.id_fil == Filiere.id). \
                filter(Semestre.niveau_id == level.id).all()

            results = []
            for row in data:
                nom_fichier = os.path.basename(row.photo)
                result = {
                    "id": row.id,
                        "nom": row.nom,
                        "prenom": row.prenom,
                        "photo": nom_fichier,
                        "genre": row.genre,
                        "date_N": row.date_n,
                        "lieu_n": row.lieu_n,
                        "email": row.email,
                        "telephone": row.tel,
                        "nationalite": row.nationnalite,
                        "date_insecription": row.date_inscription,
                        "id_fil":row.id_fil
                }
                results.append(result)
            
            return results
    #     else:
    #         return {"message": "Niveau non trouvé."}

    # except Exception as e:
    #     return {"message": str(e)}

    finally:
        session.close()

@annee_router.get("/etudiants/{level_name}/{id}")
def get_data_etudiants_for_level(level_name:str,id:int):
    try:
        Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
        session = Session()
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()

        if level:
            data = session.query(Etudiant). \
                join(Filiere, Filiere.id == Etudiant.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Matiere, Matiere.id_fil == Filiere.id). \
                filter(Semestre.niveau_id == level.id and Etudiant.id==id).all()

            results = []
            for row in data:
                nom_fichier = os.path.basename(row.photo)
                result = {
                    "id": row.id,
                        "nom": row.nom,
                        "prenom": row.prenom,
                        "photo": nom_fichier,
                        "genre": row.genre,
                        "date_N": row.date_n,
                        "lieu_n": row.lieu_n,
                        "email": row.email,
                        "telephone": row.tel,
                        "nationalite": row.nationnalite,
                        "date_insecription": row.date_inscription,
                        "id_fil":row.id_fil
                }
                results.append(result)
            
            return results
    #     else:
    #         return {"message": "Niveau non trouvé."}

    # except Exception as e:
    #     return {"message": str(e)}

    finally:
        session.close()
@annee_router.get("/matieres/{level_name}")
def get_data_matieres_for_level(level_name:str):
    Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
    session = Session()
    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()

        if level:
            data = session.query(Matiere.id, Matiere.libelle, Matiere.nbr_heure, Matiere.credit, Filiere.libelle.label('filiere')). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                filter(Semestre.niveau_id == level.id).all()


        results = []
        for matiere in data:
            results.append({
                "id": matiere.id,
                "libelle": matiere.libelle,
                "nbr_heure": matiere.nbr_heure,
                "credit": matiere.credit,
                "filiere": matiere.filiere,
            })


        return results

    finally:
        session.close()
@annee_router.get("/matieres/{level_name}/{id}")
def get_data_matieres_for_level(level_name:str,id:int):
    Session = sessionmaker(bind=create_engine("mysql+pymysql://root@localhost:3306/db_mobile3").connect())
    session = Session()
    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()

        if level:
            data = session.query(Matiere.id, Matiere.libelle, Matiere.nbr_heure, Matiere.credit, Filiere.libelle.label('filiere')). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                filter(Semestre.niveau_id == level.id and Matiere.id==id).all()


        results = []
        for matiere in data:
            results.append({
                "id": matiere.id,
                "libelle": matiere.libelle,
                "nbr_heure": matiere.nbr_heure,
                "credit": matiere.credit,
                "id_fil": matiere.filiere,
            })


        return results

    finally:
        session.close()
@annee_router.get("/salles/")
async def read_data():
    query = Salle.__table__.select()
    result_proxy = con.execute(query)   
    results = []
    for row in result_proxy:
        result = {"id": row.id,
                  "nom": row.nom}  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results
