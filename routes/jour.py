from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from schemas.jour import Jours
from models.anne import Annees,Departement,Formation,Jour,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,SurveillanceSuperviseur,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User

jour_router=APIRouter()

@jour_router.post("/")
async def write_data(jour:Jours):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    # print(surveillance)
    jour=Jour(   
        libelle=jour.libelle,
        date=jour.date,
        )
    session.add(jour)
    session.commit()



@jour_router.put("/{id}")
async def update_data(id:int,jour:Jours):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    jour= update(Jour).where(Jour.id == id).values(
        libelle=jour.libelle,
        date=jour.date,
    )
    session.execute(jour)
    session.commit()

@jour_router.delete("/{id}")
async def delete_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    jour=delete(Jour).where(Jour.id == id)
    session.execute(jour)
        # Commit the changes
    session.commit()
@jour_router.get("/")
async def read_data_users():
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    result_proxy = session.query(Jour).all()
    results = []
    for row in result_proxy:
        result = {
            "id": row.id,
            "libelle":row.libelle,
            "date":row.date
        }
        results.append(result)
    return results    
