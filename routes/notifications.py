from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select
from sqlalchemy import create_engine
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,Notifications,PV,DepartementSuperviseurs,Niveau,Historiques,Annedep,Surveillance,Filiere,Matiere,Etudiant,Salle,Surveillance,Semestre,Evaluation,Superviseur,Surveillant,User
notification_router=APIRouter()
@notification_router.get("/")
async def read_data(user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    q3 = session.query(Notifications.id,Notifications.content,Notifications.date,Notifications.image).\
            join(Superviseur,Notifications.superviseur_id==Superviseur.user_id).\
            join(Surveillant, Superviseur.user_id == Surveillance.id_surv). \
            filter(Surveillant.user_id == user_id)
    r3 = q3.all()
    results = []
    for row in r3:
        result = {
            "id": row[0],
            "content": row[1],
             "date": row[2],
            "image": row[3],
        }
        results.append(result) 
    return results