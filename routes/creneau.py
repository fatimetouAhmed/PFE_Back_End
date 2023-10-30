from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from schemas.creneau import Creneaus
from models.anne import Annees,Departement,Formation,Creneau,Jour,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User

creneau_router=APIRouter()

@creneau_router.post("/")
async def write_data(creneau:Creneaus):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    # print(surveillance)
    creneau=Creneau(   
         heure_debut=creneau.heure_debut,
        heure_fin=creneau.heure_fin
        )
    session.add(creneau)
    session.commit()



@creneau_router.put("/{id}")
async def update_data(id:int,creneau:Creneaus):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    creneau= update(Creneau).where(Creneau.id == id).values(
        heure_debut=creneau.heure_debut,
        heure_fin=creneau.heure_fin,
    )
    session.execute(creneau)
    session.commit()

@creneau_router.delete("/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    creneau=delete(Creneau).where(Creneau.id == id)
    session.execute(creneau)
        # Commit the changes
    session.commit()
@creneau_router.get("/")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(Creneau).all()
    results = []
    for row in result_proxy:
        result = {
            "id": row.id,
            "heure_debut":row.heure_debut,
            "heure_fin":row.heure_fin
        }
        results.append(result)
    return results    
