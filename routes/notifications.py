from fastapi import APIRouter,Depends
from sqlalchemy.orm import selectinload,joinedload,sessionmaker
from datetime import datetime
# from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from config.db import con
import os
from sqlalchemy.orm import aliased
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,select,func
from sqlalchemy import create_engine
from schemas.examun import Evaluations
from models.anne import Annees,Departement,Formation,Notifications,PV,SurveillanceSuperviseur,Niveau,Historiques,Annedep,Filiere,Matiere,Etudiant,Salle,Semestre,Evaluation,Superviseur,Surveillant,User
notification_router=APIRouter()
@notification_router.get("/notificationsurveillant/{id}")
async def read_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    q3 = session.query(Notifications.id,Notifications.content,Notifications.date,Notifications.image).\
            join(Surveillant,Notifications.surveillant_id==Surveillant.user_id).\
            filter(and_(Surveillant.user_id ==id , Notifications.is_read==False))
    r3 = q3.all()
    results = []
    for row in r3:
        nom_fichier = os.path.basename(row[3])
        result = {
            "id": row[0],
            "content": row[1],
             "date": row[2],
            "image":nom_fichier,
        }
        results.append(result) 
    return results
@notification_router.get("/notificationsuperviseur/{id}")
async def read_data(id:int):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    salle_alias_1 = aliased(Salle)
    salle_alias_2 = aliased(Salle)

    # q3 = session.query(Notifications.id,Notifications.content,Notifications.date,Notifications.image).\
    #     join(Evaluation, Notifications.id_exam == SurveillanceSuperviseur.id_eval). \
    #     join(Surveillant, Notifications.surveillant_id == Surveillant.user_id).\
    #     join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
    #     join(salle_alias_2, salle_alias_2.id == Surveillant.id_sal). \
    #     join(SurveillanceSuperviseur, Superviseur.user_id == SurveillanceSuperviseur.id_sup). \
    #     filter(Superviseur.user_id == id)
    q3 = session.query(Notifications.id, Notifications.content, Notifications.date, Notifications.image).\
        join(Evaluation, Notifications.id_exam == Evaluation.id). \
        join(Surveillant, Notifications.surveillant_id == Surveillant.user_id). \
        join(salle_alias_1, salle_alias_1.id.in_(func.SUBSTRING_INDEX(SurveillanceSuperviseur.id_sal, ';', -1))). \
        join(salle_alias_2, salle_alias_2.id == Surveillant.id_sal). \
        join(SurveillanceSuperviseur, SurveillanceSuperviseur.id_eval == Evaluation.id). \
        join(Superviseur, Superviseur.user_id == SurveillanceSuperviseur.id_sup). \
        filter(Superviseur.user_id == id)

    r3 = q3.all()
    results = []
    for row in r3:
        nom_fichier = os.path.basename(row[3])
        result = {
            "id": row[0],
            "content": row[1],
             "date": row[2],
            "image":nom_fichier,
        }
        results.append(result) 
    return results
@notification_router.get("/notifications/{level_name}")
def read_data_admin(level_name:str):
    engine = create_engine("mysql+pymysql://root@localhost:3306/db_mobile3")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        level = session.query(Filiere).filter(Filiere.libelle == level_name).first()
        if (level ):
            data = session.query(Notifications.id,Notifications.content,Notifications.date,Notifications.is_read,Notifications.image). \
                join(Evaluation, Notifications.id_exam == Evaluation.id).\
                join(Matiere, Matiere.id == Evaluation.id_mat).\
                join(Salle, Salle.id == Evaluation.id_sal).\
                join(Filiere, Filiere.id == Matiere.id_fil). \
                filter(Filiere.id == level.id).all()
            
            results = []
            for row in data:
                nom_fichier = os.path.basename(row[4])
      
                result = {
                        "id": row[0],
                        "content": row[1],
                        "date": row[2],
                        "is_read": row[3],
                        "image": nom_fichier,
                        }  # Créez un dictionnaire avec la clé "nom" et la valeur correspondante
                results.append(result)
            
            return results
    finally:
        session.close()
        
@notification_router.put("/{id}")
async def update_data(id:int):
    con.execute(Notifications.__table__.update().values(
        is_read=True
    ).where(Notifications.__table__.c.id==id))
    return await read_data()