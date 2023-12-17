from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime

# from auth.authConfig import create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker,aliased
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from sqlalchemy import func,or_
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User
data_router=APIRouter()  
now = datetime.now()    
@data_router.get("/evaluations/{id}")
def get_data_evaluations_for_level(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # level = session.query(Filiere).filter(Filiere.libelle == level_name).first()
        # dep = session.query(Departement).filter(Departement.nom_departement == dep_name).first()
        # if (level):
            data = session.query(Evaluation.id,Evaluation.type,Evaluation.date_debut,Evaluation.date_fin,Evaluation.id_mat,Evaluation.id_sal,Matiere.libelle, Salle.nom). \
                join(Matiere, Matiere.id == Evaluation.id_mat).\
                join(Salle, Salle.id == Evaluation.id_sal).\
                join(Surveillant, Salle.id == Surveillant.id_sal). \
                filter(and_(Surveillant.user_id == id,now >= Evaluation.date_debut, now <= Evaluation.date_fin)).all()
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
        
# @data_router.get('/salle/{id}')
# async def get_salles(id:int):
#     engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
#     Session = sessionmaker(bind=engine)
#     session = Session()
    
#     # Création d'alias pour la table Salle
#     salle_alias_1 = aliased(Salle)
#     surveillant_alias = aliased(Surveillant)
    
#     # Exécution de la requête
#     data = session.query(Salle.id,
#                         Salle.nom,). \
#         join(Evaluation, Salle.id == Evaluation.id_sal). \
#         join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
#         join(SurveillanceSuperviseur, SurveillanceSuperviseur.id_eval == Evaluation.id). \
#         join(surveillant_alias, surveillant_alias.id_sal == salle_alias_1.id). \
#         join(User, User.id == surveillant_alias.user_id). \
#         filter(Superviseur.user_id == id)

#     results = []
#     for row in data:
#         result = {
#             "id": row.id,
#             "nom": row.nom,
#             "surveillant": row.prenom+' '+row.nom_surveillant,
#         }
#         results.append(result)

#     return results


@data_router.get('/salle/{id}')
async def get_salles(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle)
    # Exécution de la requête
    data = session.query(Salle.id,
                        Salle.nom,
                        User.prenom,
                        User.nom.label('nom_surveillant')). \
        join(Evaluation, Salle.id == Evaluation.id_sal). \
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(SurveillanceSuperviseur, SurveillanceSuperviseur.id_eval == Evaluation.id). \
        join(Surveillant, Surveillant.id_sal == Salle.id). \
        join(User, User.id == Surveillant.user_id). \
        filter(Superviseur.user_id == id).group_by(Salle.nom)

    results = []
    for row in data:
        result = {
            "id": row.id,
             "nom": row.nom,
            "surveillant": row.prenom + ' ' + row.nom_surveillant,
        }
        results.append(result)

    return results

@data_router.get('/matieres/{id}')
async def get_salles(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle) 
    # Exécution de la requête
    data = session.query(Matiere.id, Matiere.libelle, Matiere.nbr_heure, Matiere.credit, Filiere.libelle.label('filiere')). \
        join(Filiere, Filiere.id == Matiere.id_fil). \
        join(Evaluation, Matiere.id == Evaluation.id_mat). \
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(SurveillanceSuperviseur, SurveillanceSuperviseur.id_eval == Evaluation.id). \
        filter(Superviseur.user_id == id)

    results = []
    for matiere in data:
        result = {
             "id": matiere.id,
                "libelle": matiere.libelle,
                "nbr_heure": matiere.nbr_heure,
                "credit": matiere.credit,
                "filiere": matiere.filiere,
        }
        results.append(result)

    return results

@data_router.get('/etudiants/{id_user}/{id}')
async def get_salles(id_user:int,id: int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle) 
    data = session.query( Etudiant.id,Etudiant.nom,Etudiant.prenom,Etudiant.photo,Etudiant.matricule,Etudiant.genre,Etudiant.date_n,Etudiant.date_inscription,Etudiant.lieu_n,Etudiant.email,Etudiant.tel,Etudiant.nationnalite,Etudiant.id_fil,Filiere.abreviation.label('filiere_libelle')).\
        join(Filiere,Filiere.id == Etudiant.id_fil).\
        join(Matiere,Matiere.id_fil == Filiere.id).\
        join(Evaluation,Evaluation.id_mat == Matiere.id).\
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(SurveillanceSuperviseur,Evaluation.id == SurveillanceSuperviseur.id_eval).\
        join(Superviseur,Superviseur.user_id == SurveillanceSuperviseur.id_sup).\
        filter(and_(Superviseur.user_id ==id_user ,Evaluation.id_sal==id)).group_by(Etudiant.id)

    results = []
    for row in data:
        nom_fichier = os.path.basename(row.photo)
        result = {
            "id": row.id,
            "nom": row.nom,
            "prenom": row.prenom,
            "photo": nom_fichier,
            "matricule": row.matricule,
            "genre": row.genre,
            "date_N": row.date_n,
            "lieu_n": row.lieu_n,
            "email": row.email,
            "telephone": row.tel,
            "nationalite": row.nationnalite,
            "date_inscription": row.date_inscription,
            "id_fil": row.id_fil,
            "filiere": row.filiere_libelle
        }
        results.append(result)

    return results

@data_router.get('/filieres/{id}')
async def get_salles(id: int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle) 
    data = session.query(Filiere.id,Filiere.libelle,Semestre.libelle.label('semestre_libelle')).\
        join(Semestre,Semestre.id == Filiere.semestre_id).\
        join(Matiere,Matiere.id_fil == Filiere.id).\
        join(Evaluation,Evaluation.id_mat == Matiere.id).\
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(SurveillanceSuperviseur,Evaluation.id == SurveillanceSuperviseur.id_eval).\
        join(Superviseur,Superviseur.user_id == SurveillanceSuperviseur.id_sup).\
        filter(Superviseur.user_id == id).group_by(Filiere.id)

    results = []
    for row in data:
        result = {
            "id": row.id,
            "libelle": row.libelle,
            "semestre": row.semestre_libelle
        }
        results.append(result)

    return results
