from PIL import Image
from io import BytesIO
import deepface
from deepface import DeepFace
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer, String ,Sequence ,ForeignKey ,Date ,DateTime, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import relationship, mapper, sessionmaker
import os

from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from config.db import con
#from models.departement import Departements
#from models.filiere import Filieres
#from models.matiere import Matiere
from models.anne import Etudiant,Matiere,Surveillance
#from models.etudiermat import Etudiant
#from models.etudiermat import etudiermats
#from models.etudiermat import Matiere
#from models.semestre_etudiant import Semestres
#from models.semestre_etudiant import semestre_etudiants
# from models.semestre_etudiant import Etudiants
#from models.examun import examuns
from routes.historique import write_data_case_etudiant
from fastapi import APIRouter,Depends
from auth.authConfig import recupere_userid,create_user,UserResponse,UserCreate,get_db,authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,check_Adminpermissions,check_superviseurpermissions,check_survpermissions,User
from datetime import datetime, timedelta
from models.anne import Etudiant ,Evaluation
Base = declarative_base()

# Create a session factory
Session = sessionmaker(bind=con)
# Create a session
session = Session()



Base.metadata.create_all(con)
def get_etudiant(photo: str):
    # print(photo)
    # Retrieve the student's ID after verifying the image
    etudiants = session.query(Etudiant.id).filter(Etudiant.photo == photo).all()
    id_etu = etudiants[0][0]
    print(id_etu)
    return  id_etu
async def get_infoexamun(imagepath,image1: str,id_etu:int,user_id: int = Depends(recupere_userid),user: User = Depends(check_survpermissions)):
   
             #temps actuel
             now = datetime.now()
             #filere de l'etudiant 
             fil=session.query(Etudiant.id_fil).filter(Etudiant.id == id_etu).all()
             
             #recuperation des matires de filiere de l'etudiant
             subquery = session.query(Matiere.id).filter(Matiere.id_fil == fil[0][0])
             #recuperation de salle de surveillance de cette utilisateur a ce moment
             salle=session.query(Surveillance.id_sal).filter(and_(now >= Surveillance.date_debut, now <= Surveillance.date_fin, Surveillance.id_surv==user_id)).all()
             print("sal",salle[0][0])
             exams = session.query(Evaluation.id).filter(and_(now >= Evaluation.date_debut, now <= Evaluation.date_fin,Evaluation.id_sal==salle[0][0], Evaluation.id_mat.in_(subquery))).all()
             
             #timestamp = datetime.now().timestamp()

             if not exams:
                       timestamp = datetime.now().timestamp()
                       notification_filename = f"{timestamp}.jpg"
                       notification_folder = "C:/Users/hp/Desktop/PFE/PFE_FRONT/images/notifications"
                       notification_path = os.path.join(notification_folder, notification_filename)
                       os.rename(imagepath, notification_path)

            # Nouveau chemin de l'image
                       image_etu_path = notification_path.replace("\\", "/")        
           
   
                       #return "pas d'examen a ce moment"
                       return await write_data_case_etudiant(image_etu_path,id_etu, user_id, user)
             else:   
                   return "Rentrez"
    
  