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
scolarite_router=APIRouter()
@scolarite_router.get("/informations")
def get_data_for_level():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()

    level_name = 'L1'
    dep_name = 'informatique'

    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()
        dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        if (level and dep):
            data = session.query(Evaluation, Surveillance, Superviseur, Surveillant). \
                join(Matiere, Evaluation.id_mat == Matiere.id). \
                join(Surveillance, Surveillance.id_sal == Evaluation.id_sal). \
                join(Surveillant, Surveillant.user_id == Surveillance.id_surv). \
                join(Superviseur, Superviseur.user_id == Surveillant.superviseur_id). \
                join(DepartementSuperviseurs, and_(DepartementSuperviseurs.id_sup == Superviseur.user_id,
                                                DepartementSuperviseurs.id_dep == dep.id)). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Niveau, Niveau.id == Semestre.niveau_id). \
                filter(Niveau.id == level.id).all()

            # Convert the data to a JSON-serializable format
            json_data = []
            for evaluation, surveillance, superviseur, surveillant in data:
                json_data.append({
                    "Evaluation": evaluation.__dict__,
                    "Surveillance": surveillance.__dict__,
                    "Superviseur": superviseur.__dict__,
                    "Surveillant": surveillant.__dict__
                })

            return json_data
    finally:
        session.close()
        
@scolarite_router.get("/evaluations/{dep_name}/{level_name}")
def get_data_evaluations_for_level(dep_name:str,level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()
        dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        if (level and dep):
            data = session.query(Evaluation.id,Evaluation.type,Evaluation.date_debut,Evaluation.date_fin,Evaluation.id_mat,Evaluation.id_sal,Matiere.libelle, Salle.nom). \
                join(Matiere, Matiere.id == Evaluation.id_mat).\
                join(Salle, Salle.id == Evaluation.id_sal).\
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Niveau, Niveau.id == Semestre.niveau_id). \
                filter(Niveau.id == level.id).all()
            
            results = []
            for row in data:
                result = {
                        "id": row.id,
                        "type": row.type,
                        "heure_deb": row.date_debut,
                        "heure_fin": row.date_fin,
                        "id_mat": row.id_mat,
                        "id_sal": row.id_sal,
                        "matiere": row.libelle,
                            "salle": row.nom,
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()
        
@scolarite_router.get("/matieres/{dep_name}/{level_name}")
def get_data_matieres_for_level(dep_name:str,level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()
        dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        if (level and dep):
            data = session.query(Matiere.libelle). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Niveau, Niveau.id == Semestre.niveau_id). \
                filter(Niveau.id == level.id).all()
            
            results = []
            for row in data:
                result = {
                        "libelle": row.libelle
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()

@scolarite_router.get("/salles/")
def get_data_salles_for_level():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        
            data = session.query(Salle.nom).all()
            
            results = []
            for row in data:
                result = {
                        "nom": row.nom
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()

@scolarite_router.post("/")
async def write_data(evaluation:Evaluations):
    result = con.execute(Evaluation.__table__.insert().values(
        type=evaluation.type,
        date_debut=evaluation.date_debut,
        date_fin=evaluation.date_fin,
        id_sal=evaluation.id_sal,
        id_mat=evaluation.id_mat,
    ))

    if result.rowcount == 1:
        return {"message": "Insertion réussie!"}
    else:
        return {"message": "Échec de l'insertion."}


@scolarite_router.put("/{id}")
async def update_data(id:int,evaluation:Evaluations,):
    result=con.execute(Evaluation.__table__.update().values(
        type=evaluation.type,
        date_debut=evaluation.date_debut,
        date_fin=evaluation.date_fin,  # Correction ici
        id_sal=evaluation.id_sal,
        id_mat=evaluation.id_mat,
    ).where(Evaluation.__table__.c.id==id))
    if result.rowcount == 1:
        return {"message": "Modification réussie!"}
    else:
        return {"message": "Échec de la modification."}

@scolarite_router.delete("/{id}")
async def delete_data(id:int,):
    result=con.execute(Evaluation.__table__.delete().where(Evaluation.__table__.c.id==id))
    if result.rowcount == 1:
        return {"message": "Supression réussie!"}
    else:
        return {"message": "Échec de la supression."}
    
@scolarite_router.get("/user_data/")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(User.id,User.nom,User.prenom,User.photo,User.email,User.role).filter(User.role=='superviseur').all()
    results = []
    for row in result_proxy:
        nom_fichier = os.path.basename(row.photo)
        result = {
            "id": row.id,
            "nom": row.nom,
            "prenom": row.prenom,
            "email": row.email,
            "role": row.role,
            "photo": nom_fichier,
        }
        results.append(result)
    return results    
    
@scolarite_router.get("/user_data/surveillant")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(User.id,User.nom,User.prenom,User.photo,User.email,User.role).filter(User.role=='surveillant').all()
    results = []
    for row in result_proxy:
        nom_fichier = os.path.basename(row.photo)
        result = {
            "id": row.id,
            "nom": row.nom,
            "prenom": row.prenom,
            "email": row.email,
            "role": row.role,
            "photo": nom_fichier,
        }
        results.append(result)
    return results    
  
@scolarite_router.get('/pv')
async def get_pvs():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = select(PV.__table__.c.id,
                   PV.__table__.c.photo,
                   PV.__table__.c.description,
                   PV.__table__.c.nni,
                    PV.__table__.c.tel,
                   User.prenom,PV.__table__.c.date_pv)
    # . \
    #     join(Surveillant, Surveillant.user_id == PV.__table__.c.surveillant_id). \
    #     join(User, Surveillant.user_id == User.id).filter(PV.__table__.c.id==id)

    result = session.execute(query).fetchall()
    results = []
    for row in result:
        nom_fichier = os.path.basename(row.photo)
        result = {
                  "id": row.id,
                  "photo": nom_fichier,
                  "description": row.description,
                  "nni": row.nni,
                  "tel": row.tel,
                  "surveillant": row.prenom,
                  "date_pv": row.date_pv,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results  

@scolarite_router.get("/salle/{nom}")
async def salle_id(nom:str):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    salles = session.query(Salle).filter(Salle.nom == nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    id=0
    for salle in salles:
        id=salle.id   
    return id
@scolarite_router.get("/matiere/{nom}")
async def matiere_id(nom:str):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    matieres = session.query(Matiere).filter(Matiere.libelle == nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    id=0
    for matiere in matieres:
        id=matiere.id   
    return id

@scolarite_router.get("/Surveillances/{dep_name}/{level_name}")
def get_data_for_level(dep_name:str,level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        level = session.query(Niveau).filter(Niveau.nom == level_name).first()
        dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        if (level and dep):
            data = session.query(Surveillance.id,Surveillance.date_debut,Surveillance.date_fin,Surveillance.id_surv,Surveillance.id_sal,User.prenom,Salle.nom). \
                join(Salle, Salle.id == Surveillance.id_sal). \
                join(Surveillant, Surveillant.user_id == Surveillance.id_surv). \
                join(User, Surveillant.user_id == User.id).\
                join(Matiere, Matiere.id == Matiere.id). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                join(Semestre, Semestre.id == Filiere.semestre_id). \
                join(Niveau, Niveau.id == Semestre.niveau_id). \
                filter(Niveau.id == level.id).all()

            # Convert the data to a JSON-serializable format
            json_data = []
            for row in data:
                json_data.append({
                   'id': row.id,
                        'date_debut': row.date_debut, 
                       'date_fin': row.date_fin,
                       'id_surv': row.id_surv,
                       'id_sal': row.id_sal,
                       'superviseur': row.prenom, 
                       'salle': row.nom,
                })

            return json_data
    finally:
        session.close()
        

# @scolarite_router.get("/superviseurs/")
# def get_data_evaluations_for_level():
#     engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     try:
#         level = session.query(Niveau).filter(Niveau.nom == level_name).first()
#         dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
#         if (level and dep):
#             data = session.query(User.id,User.nom,User.prenom,User.photo,User.email,User.role)
#             # . \
#             #     join(Superviseur, Superviseur.user_id == User.id). \
#             #     join(DepartementSuperviseurs, and_(DepartementSuperviseurs.id_sup == Superviseur.user_id,
#             #                                     DepartementSuperviseurs.id_dep == dep.id)). \
#             #     join(Semestre, Semestre.id == Filiere.semestre_id). \
#             #     join(Niveau, Niveau.id == Semestre.niveau_id). \
#             #     filter(Niveau.id == level.id and User.role=='superviseur').all()
            
#             results = []
#             for row in data:
#                 result = {
#                        "id": row.id,
#                   "nom": row.nom,
#                    "prenom": row.prenom,
#                   "photo": row.photo,
#                    "email": row.email,
#                    "role": row.role,
#                         }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
#                 results.append(result)
            
#             return results
#     finally:
#         session.close()