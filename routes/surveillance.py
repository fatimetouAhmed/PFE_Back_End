from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from schemas.surveillance import Surveillances
from models.anne import Annees,Departement,Formation,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User

surveillance_router=APIRouter()
# @surveillance_router.get("/")
# async def read_data():  
#     # return results
#     Session = sessionmaker(bind=con)
#     session = Session()
#     query = select(Surveillance.id,
#                    Surveillance.date_debut,
#                    Surveillance.date_fin,
#                    Surveillance.id_surv,
#                     Surveillance.id_sal,
#                    Salle.nom,
#                    User.prenom). \
#         join(Salle, Salle.id == Surveillance.id_sal). \
#         join(Surveillant, Surveillant.user_id == Surveillance.id_surv). \
#         join(User, Surveillant.user_id == User.id)

#     result = session.execute(query).fetchall()
#     formatted_data = [{'id': row.id,
#                         'date_debut': row.date_debut, 
#                        'date_fin': row.date_fin,
#                        'surveillant_id': row.id_surv,
#                        'salle_id': row.id_sal,
#                        'superviseur': row.prenom, 
#                        'departement': row.nom, 

#                        } for row in result]
#     return formatted_data
    # return con.execute(surveillances.select().fetchall())
@surveillance_router.get("/surveillances/nom")
async def read_data():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    query = session.query(User.prenom).join(Superviseur).all()
    results = []
    for row in query:
        result = {
            "prenom": row[0],
        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)

    return results
@surveillance_router.get("/surveillances/{nom}")
async def read_data(nom:str,):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    query = session.query(Superviseur).join(User).filter(User.prenom==nom).all()
    id=0
    for surveillance in query:
        id=surveillance.user_id  
    return id

@surveillance_router.get("/surveillances/evaluations/nom")
async def read_data():
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    query = session.query(Evaluation.type).all()
    results = []
    for row in query:
        result = {
            "type": row[0],
        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
        results.append(result)

    return results

@surveillance_router.get("/surveillances/evaluations/{nom}")
async def read_data(nom:str,):
    # Créer une session
    Session = sessionmaker(bind=con)
    session = Session()

    query = session.query(Evaluation.id).filter(Evaluation.type==nom).all()
    id=0
    for surveillance in query:
        id=surveillance.id  
    return id
    # return results
# @surveillance_router.get("/surveillance")
# async def read_data(user_id: int = Depends(recupere_userid), ):
#     # Créer une session
#     Session = sessionmaker(bind=con)
#     session = Session()
#     query = session.query(Surveillant.user_id).join(Superviseur).filter(Surveillant.superviseur_id == user_id).all()

#     ids = [row[0] for row in query]  # Extract the list of IDs from the query results

#     query1 = session.query(Surveillances).join(Surveillant).filter(Surveillant.user_id.in_(ids)).all()
#     results = []
#     for row in query1:
#         result = {
#             "id": row.id,
#             "date_debut": row.date_debut,
#             "date_fin": row.date_fin,
#             "surveillant_id": row.id_surv,
#             "salle_id": row.id_sal,
#         }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
#         results.append(result)

#     return results


# @surveillance_router.get("/{id}")
# async def read_data(id:int):  
#     # return results
#     Session = sessionmaker(bind=con)
#     session = Session()
#     query = select(Surveillance.id,
#                    Surveillance.date_debut,
#                    Surveillance.date_fin,
#                    Surveillance.id_surv,
#                     Surveillance.id_sal,
#                    Salle.nom,
#                    User.prenom). \
#         join(Salle, Salle.id == Surveillance.id_sal). \
#         join(Surveillant, Surveillant.user_id == Surveillance.id_surv). \
#         join(User, Surveillant.user_id == User.id).filter(Surveillance.id==id)

#     result = session.execute(query).fetchall()
#     formatted_data = [{'id': row.id,
#                         'date_debut': row.date_debut, 
#                        'date_fin': row.date_fin,
#                        'surveillant_id': row.id_surv,
#                        'salle_id': row.id_sal,
#                        'superviseur': row.prenom, 
#                        'departement': row.nom, 

#                        } for row in result]
#     return formatted_data
#     # return con.execute(surveillances.select().where(Surveillance.id==id)).fetchall()


@surveillance_router.post("/")
async def write_data(surveillance:Surveillances):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    # print(surveillance)
    surveillance=SurveillanceSuperviseur(   
        id_sup=surveillance.id_sup,
        id_sal=surveillance.id_sal,
        id_eval=surveillance.id_eval,
        )
    session.add(surveillance)
    session.commit()



@surveillance_router.put("/{id}")
async def update_data(id:int,surveillance:Surveillances):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    surveillance= update(SurveillanceSuperviseur).where(SurveillanceSuperviseur.id == id).values(
        id_sup=surveillance.id_sup,
        id_sal=surveillance.id_sal,
        id_eval=surveillance.id_eval,
    )
    session.execute(surveillance)
    session.commit()

@surveillance_router.delete("/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    surveillance=delete(SurveillanceSuperviseur).where(SurveillanceSuperviseur.id == id)
    session.execute(surveillance)
        # Commit the changes
    session.commit()
@surveillance_router.get("/user_data/surveillant/nom")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(User.prenom).filter(User.role=='superviseur').all()
    results = []
    for row in result_proxy:
        result = {
            "prenom": row.prenom,
        }
        results.append(result)
    return results    
@surveillance_router.get("/salles/nom")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(Salle.nom).filter().all()
    results = []
    for row in result_proxy:
        result = {
            "nom": row.nom,
        }
        results.append(result)
    return results