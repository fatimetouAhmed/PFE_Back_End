from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker,aliased
from datetime import datetime

# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from sqlalchemy import func
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Jour,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User
scolarite_router=APIRouter()      
@scolarite_router.get("/evaluations/{level_name}")
def get_data_evaluations_for_level(level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        level = session.query(Filiere).filter(Filiere.libelle == level_name).first()
        # dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        if (level):
            data = session.query(Evaluation.id,Evaluation.type,Evaluation.date_debut,Evaluation.date_fin,Evaluation.id_mat,Evaluation.id_sal,Evaluation.id_jour,Matiere.libelle, Salle.nom,Jour.libelle.label('jour')). \
                join(Matiere, Matiere.id == Evaluation.id_mat).\
                join(Jour, Jour.id == Evaluation.id_jour).\
                join(Salle, Salle.id == Evaluation.id_sal).\
                join(Filiere, Filiere.id == Matiere.id_fil). \
                filter(Filiere.id == level.id).all()
            results = []
            for row in data:
                result = {
                        "id": row.id,
                        "type": row.type,
                        "heure_deb": row.date_debut,
                        "heure_fin": row.date_fin,
                        "id_mat": row.id_mat,
                        "id_sal": row.id_sal,
                        "id_jour": row.id_jour,
                        "matiere": row.libelle,
                            "salle": row.nom,
                            "jour": row.jour,
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()
        
@scolarite_router.get("/matieres/{level_name}")
def get_data_matieres_for_level(level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        level = session.query(Filiere).filter(Filiere.libelle == level_name).first()
        if (level):
            data = session.query(Matiere.libelle). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                filter(Filiere.id == level.id).all()
            
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
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(Salle.id, Salle.nom).all()

    results = []
    for row in result_proxy:
        result = {
            "id": row.id,
            "nom": row.nom
        }
        results.append(result)
    return results
        
@scolarite_router.get("/sal")
def get_data_salles_for_level():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        
            data = session.query(Salle.id,Salle.nom).all()
            
            results = []
            for row in data:
                result = {
                    "id":row.id,
                        "nom": row.nom
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()


@scolarite_router.post("/")
async def write_data(evaluation:Evaluations):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    eval = Evaluation(
            type=evaluation.type,
        date_debut=evaluation.date_debut,
        date_fin=evaluation.date_fin,  # Correction ici
        id_sal=evaluation.id_sal,
        id_mat=evaluation.id_mat,
        id_jour=evaluation.id_jour,
       )
    session.add(eval)
    session.commit()
    # if result.rowcount == 1:
    #     return {"message": "Insertion réussie!"}
    # else:
    #     return {"message": "Échec de l'insertion."}


@scolarite_router.put("/{id}")
async def update_data(id:int,evaluation:Evaluations,):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    print(evaluation)
    update_stmt = update(Evaluation).where(Evaluation.id == id).values(
        type=evaluation.type,
        date_debut=evaluation.date_debut,
        date_fin=evaluation.date_fin,  # Correction ici
        id_sal=evaluation.id_sal,
        id_mat=evaluation.id_mat,
         id_jour=evaluation.id_jour,
           )

        # Execute the update statement
    session.execute(update_stmt)
        # Commit the changes
    session.commit()
  

@scolarite_router.delete("/{id}")
async def delete_data(id:int,):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_stmt = delete(Evaluation).where(Evaluation.id == id)
    session.execute(delete_stmt)
        # Commit the changes
    session.commit()
  
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
    result_proxy = session.query(User.id, User.nom, User.prenom, User.photo, User.email, User.role, Surveillant.typecompte, Salle.nom.label('salle')).\
        join(Surveillant, User.id == Surveillant.user_id).\
        join(Salle, Surveillant.id_sal == Salle.id).\
        filter(User.role == 'surveillant').all()

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
            "typecompte": row.typecompte,
            "salle": row.salle,
        }
        results.append(result)
    return results

@scolarite_router.get('/pv')
async def get_pvs():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(PV.id,
                   PV.nom,
                    PV.photo,
                   PV.description,
                   PV.nni,
                    PV.tel,PV.type,PV.etat,
                   User.prenom,PV.date_pv). \
      join(Surveillant, PV.surveillant_id == Surveillant.user_id). \
            join(User, Surveillant.user_id == User.id)

    # result = session.execute(query).fetchall()
    results = []
    for row in data:
        nom_fichier = os.path.basename(row.photo)
        result = {
                  "id": row.id,
                "nom": row.nom,
                  "photo": nom_fichier,
                  "description": row.description,
                  "nni": row.nni,
                  "tel": row.tel,
                "type": row.type,
                  "etat": row.etat,
                  "surveillant": row.prenom,
                  "date_pv": row.date_pv,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results  
@scolarite_router.put("/pv/{id}")
async def update_data(id:int):
    con.execute(PV.__table__.update().values(
        etat='accepter'
    ).where(PV.__table__.c.id==id))
    return "Succees"
@scolarite_router.put("/pv/refuser/{id}")
async def update_data(id:int):
    con.execute(PV.__table__.update().values(
        etat='refuser'
    ).where(PV.__table__.c.id==id))
    return "Succees"
@scolarite_router.get("/jours")
def get_data_matieres_for_level():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
    
            data = session.query(Jour.libelle).all()
            
            results = []
            for row in data:
                result = {
                        "libelle": row.libelle
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()
@scolarite_router.get("/jour/{nom}")
async def salle_id(nom:str):
    Session = sessionmaker(bind=con)
    session = Session()

    # Effectuer la requête pour récupérer les filières avec leurs départements
    jours = session.query(Jour).filter(Jour.libelle== nom).all()
     
    # Parcourir les filières et récupérer leurs départements associés
    id=0
    for jour in jours:
        id=jour.id   
    return id
@scolarite_router.get("/salle/{nom}")
async def salle_id(nom:str):
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

@scolarite_router.get("/Surveillances/{level_name}")
def get_data_for_level(level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        level = session.query(Filiere).filter(Filiere.libelle == level_name).first()
        if level:
            data = session.query(SurveillanceSuperviseur.id, SurveillanceSuperviseur.id_sup, SurveillanceSuperviseur.id_sal, SurveillanceSuperviseur.id_eval, User.prenom, User.nom,  Evaluation.type). \
                join(Salle, Salle.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
                join(Evaluation, SurveillanceSuperviseur.id_eval == Evaluation.id). \
                join(Matiere, Evaluation.id_mat == Matiere.id). \
                join(Superviseur, Superviseur.user_id == SurveillanceSuperviseur.id_sup). \
                join(User, Superviseur.user_id == User.id). \
                join(Filiere, Filiere.id == Matiere.id_fil). \
                filter(Filiere.id == level.id, SurveillanceSuperviseur.id_sal != None).all()

            json_data = []
            
            for row1 in data:
                ids = row1.id_sal.split(';')
                salles = session.query(Salle).filter(Salle.id.in_(ids)).all()
                salle_noms = [salle.nom for salle in salles]
                json_data.append({
                    'id': row1.id,
                    'id_sup': row1.id_sup,
                    'id_sal': row1.id_sal,
                    'id_eval': row1.id_eval,
                    'superviseur': row1.prenom, 
                    'evaluation':row1.type,
                     'salle': salle_noms 
                })

            return json_data
    finally:
        session.close()

        
@scolarite_router.get('/pv/superviseur/{id}')
async def get_pvs(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle)
    salle_alias_2 = aliased(Salle)
    
    # Exécution de la requête
# Exécution de la requête avec distinct()
    data = session.query(PV.id,
                        PV.nom,
                        PV.photo,
                        PV.description,
                        PV.nni,
                        PV.tel,
                        PV.type,
                        PV.etat,
                        User.prenom,
                        PV.date_pv). \
        join(Evaluation, PV.id_eval == Evaluation.id). \
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(SurveillanceSuperviseur, SurveillanceSuperviseur.id_eval == Evaluation.id). \
        join(Superviseur, Superviseur.user_id == SurveillanceSuperviseur.id_sup). \
        filter(and_(Superviseur.user_id==id,PV.etat=='initial')). \
        group_by(PV.id)

    # result = session.execute(query).fetchall()
    results = []
    for row in data:
        nom_fichier = os.path.basename(row.photo)
        result = {
                  "id": row.id,
                "nom": row.nom,
                  "photo": nom_fichier,
                  "description": row.description,
                  "nni": row.nni,
                  "tel": row.tel,
                  "type":row.type,
                  "etat":row.etat,
                  "surveillant": row.prenom,
                  "date_pv": row.date_pv,
                  }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)
    
    return results  
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