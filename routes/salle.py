from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,update,delete
from sqlalchemy import create_engine
from schemas.salle import SalleBase
from models.anne import Annees,Departement,Formation,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User
salle_router=APIRouter()

@salle_router.post("/")
async def write_data(salle:SalleBase,):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=Salle(
        nom=salle.nom
        )
    session.add(salle)
    session.commit()

@salle_router.put("/{id}")
async def update_data(id:int,salle:SalleBase,):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle= update(Salle).where(Salle.id == id).values(
        nom=salle.nom
    )
    session.execute(salle)
    session.commit()

@salle_router.delete("/{id}")
async def delete_data(id:int,):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle=delete(Salle).where(Salle.id==id)
    session.execute(salle)
        # Commit the changes
    session.commit()

  