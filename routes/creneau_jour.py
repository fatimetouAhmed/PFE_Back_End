from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker,aliased
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from schemas.creneau_jour import Creneau_jours
from models.anne import Annees,Departement,Formation,Creneau,CreneauJours,Jour,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User

creneaujour_router=APIRouter()

@creneaujour_router.post("/")
async def write_data(creneau_jours:Creneau_jours):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    # print(surveillance)
    creneau_jou=CreneauJours(  
        id_jour=creneau_jours.id_jour,
        id_creneau=creneau_jours.id_creneau,
        id_mat=creneau_jours.id_mat
        )
    session.add(creneau_jou)
    session.commit()



@creneaujour_router.put("/{id}")
async def update_data(id:int,creneau_jour:Creneau_jours):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    creneau_jour= update(CreneauJours).where(Creneau.id == id).values(
         id_jour=creneau_jour.id_jour,
        id_creneau=creneau_jour.id_creneau,
        id_mat=creneau_jour.id_mat
    )
    session.execute(creneau_jour)
    session.commit()

@creneaujour_router.delete("/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    creneau=delete(CreneauJours).where(Creneau.id == id)
    session.execute(CreneauJours)
        # Commit the changes
    session.commit()
@creneaujour_router.get("/")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(CreneauJours).all()
    results = []
    for row in result_proxy:
        result = {
            "id": row.id,
            "id_jour":row.id_jour,
            "id_creneau":row.id_creneau,
            "id_mat":row.id_mat
        }
        results.append(result)
    return results 
@creneaujour_router.get("/jour/{libelle}/{id}")   
async def read_data_users(libelle:str,id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    creneau_jour_alias_1 = aliased(CreneauJours) 
    data = session.query(Matiere.libelle,Creneau.heure_debut,Creneau.heure_fin).\
        join(CreneauJours,Creneau.id == CreneauJours.id_creneau).\
        join(Matiere,CreneauJours.id_mat == Matiere.id).\
        join(Jour,CreneauJours.id_jour== Jour.id).\
        join(Evaluation,Evaluation.id_jour== Jour.id).\
        filter(and_(Jour.libelle ==libelle ,Evaluation.id_sal==id)).group_by(Matiere.libelle)
    results = []
    for row in data:
        result = {
            "libelle": row.libelle,
            "heure_debut":row.heure_debut,
            "heure_fin":row.heure_fin
        }
        results.append(result)
    return results
@creneaujour_router.get("/joureupreve/{type}")   
async def read_data_users(type:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session() 
    data = session.query(Jour.libelle).\
        join(Evaluation,Jour.id == Evaluation.id_jour).\
        filter(and_(Evaluation.type==type )).group_by(Jour.libelle)
    results = []
    for row in data:
        result = {
            "libelle": row.libelle,
        }
        results.append(result)
    return results
@creneaujour_router.get("/epreuve")   
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session() 
    data = session.query(Evaluation.type).group_by(Evaluation.type)
    results = []
    for row in data:
        result = {
            "type": row.type,
        }
        results.append(result)
    return results